"""Check KNIME exports against the original workbook using Python's standard library.

AI prompt summary: independently reconcile all three chart datasets with the
Traffic rows and the published T1 totals, retaining unknown categories and zeros.
"""

from collections import Counter
from decimal import Decimal
from pathlib import Path
from xml.etree import ElementTree as E
from zipfile import ZipFile
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
WORKBOOK = ROOT / "data/raw/hospitalisation_injury_publication_sep2023.xlsx"
PROCESSED = ROOT / "data/processed"
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"


def integer(value):
    number = Decimal(str(value))
    assert number.is_finite() and number == number.to_integral_value(), value
    return int(number)


def sheet_rows(archive, name):
    relationships = {
        e.attrib["Id"]: e.attrib["Target"]
        for e in E.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    }
    sheets = E.fromstring(archive.read("xl/workbook.xml")).find("m:sheets", NS)
    sheet = next(s for s in sheets if s.attrib["name"] == name)
    target = relationships[sheet.attrib[REL]]
    target = target.lstrip("/") if target.startswith("/") else "xl/" + target
    strings = ["".join(item.itertext()) for item in E.fromstring(archive.read("xl/sharedStrings.xml"))]
    with archive.open(target) as stream:
        for _, row in E.iterparse(stream, events=("end",)):
            if row.tag != "{" + NS["m"] + "}row":
                continue
            values = {}
            for cell in row.findall("m:c", NS):
                value = cell.find("m:v", NS)
                text = value.text if value is not None else None
                if cell.attrib.get("t") == "s" and text is not None:
                    text = strings[int(text)]
                if text is not None:
                    column = "".join(c for c in cell.attrib["r"] if c.isalpha())
                    values[column] = text
            if values:
                yield values
            row.clear()


def check_export(filename, dimensions, expected):
    assert (PROCESSED / filename).read_bytes() == (ROOT / "web/data" / filename).read_bytes(), (
        filename, "The web copy differs from data/processed"
    )
    actual = {}
    with (PROCESSED / filename).open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        assert reader.fieldnames == dimensions + ["hospitalisations"], reader.fieldnames
        for row in reader:
            key = tuple(integer(row[k]) if k == "year" else row[k] for k in dimensions)
            assert key not in actual, (filename, "duplicate key", key)
            value = integer(row["hospitalisations"])
            assert value >= 0, (filename, key, value)
            actual[key] = value
    assert actual == dict(expected), (
        filename,
        "Export differs from the raw Traffic data",
        "missing keys", list(set(expected) - set(actual))[:3],
        "extra keys", list(set(actual) - set(expected))[:3],
        "wrong values", [(k, actual.get(k), v) for k, v in expected.items() if actual.get(k) != v][:3],
    )
    return len(actual)


def main():
    annual, road, demographic = Counter(), Counter(), Counter()
    seen = set()
    total_rows = traffic_rows = 0
    missing_age = other_sex = 0
    with ZipFile(WORKBOOK) as workbook:
        rows = iter(sheet_rows(workbook, "raw"))
        assert next(rows)["M"] == "Hospitalisations"
        for row in rows:
            if "A" not in row:
                continue
            total_rows += 1
            if row.get("D") != "Traffic":
                continue
            traffic_rows += 1
            key = tuple(row.get(column, "") for column in "ABCDEFGH")
            assert key not in seen, ("Duplicate Traffic record", key)
            seen.add(key)
            year = integer(row["A"])
            count = integer(row["M"])
            assert 2011 <= year <= 2021 and count >= 0
            annual[(year,)] += count
            road[(year, row["G"])] += count
            demographic[(year, row["G"], row["E"], row["F"])] += count
            missing_age += count if row["E"] == "Missing" else 0
            other_sex += count if row["F"] not in ["Male", "Female"] else 0
        controls = {}
        for row in sheet_rows(workbook, "T1"):
            if row.get("A", "").isdigit() and "B" in row:
                controls[(integer(row["A"]),)] = integer(row["B"])
        assert dict(annual) == controls, "Raw Traffic totals do not match the published T1 controls"

    output_rows = {
        "annual_totals.csv": check_export("annual_totals.csv", ["year"], annual),
        "road_user_by_year.csv": check_export("road_user_by_year.csv", ["year", "road_user"], road),
        "age_sex_by_road_user.csv": check_export("age_sex_by_road_user.csv", ["year", "road_user", "age_group", "sex"], demographic),
    }
    report = {
        "status": "PASS", "source_rows": total_rows, "traffic_rows": traffic_rows,
        "duplicate_traffic_keys": 0, "matched_annual_controls": len(controls),
        "export_rows": output_rows, "unknown_age_hospitalisations_retained": missing_age,
        "other_or_not_stated_sex_hospitalisations_retained": other_sex,
        "annual_totals": {str(year): count for (year,), count in sorted(annual.items())},
        "metric": "Sum of Hospitalisations for Cause of injury = Traffic",
        "notes": "Counts are not population-adjusted risk. The source has recording breaks in 2012 and 2017.",
    }
    (PROCESSED / "verification.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
