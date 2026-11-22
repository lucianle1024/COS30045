"""Reproduce the Stand Up 2 audit and EDA from the supplied BITRE workbook.

AI prompt summary: reuse the workbook reader, preserve unknowns and zeros,
reconcile groupings and withhold unverified bed-day interpretations.
"""

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
from zipfile import ZipFile

from verify_data import ROOT, WORKBOOK, integer, sheet_rows

FIELDS = dict(zip("ABCDEFGHIJKLM", [
    "Calendar year", "Month", "ABS remoteness area", "Cause of injury", "Age group",
    "Sex", "Road user", "Counterparty", "Count of cases", "Bed days", "Died_cases",
    "Died_bed_days", "Hospitalisations",
]))
MONTHS = "January February March April May June July August September October November December".split()
AGES = ["0-7", "8-16", "17-25", "26-39", "40-64", "65-74", "75+", "Missing"]
OUTPUT = ROOT / "data/analysis"


def change_percent(before, after):
    return None if before == 0 else 100 * (after - before) / before


def profile(rows):
    result = {}
    for column, name in FIELDS.items():
        values = [r[column] for r in rows if r.get(column) not in (None, "")]
        item = {"blank_rows": len(rows) - len(values), "distinct_values": len(set(values))}
        if column in "AIJKLM":
            numbers = [integer(v) for v in values]
            assert all(v >= 0 for v in numbers), (name, "negative value")
            item.update(type="integer", zero_rows=numbers.count(0),
                        minimum=min(numbers, default=None), maximum=max(numbers, default=None))
        else:
            item.update(type="categorical", values=sorted(set(values)))
        result[name] = item
    return result


def analyse(rows):
    traffic = [r for r in rows if r.get("D") == "Traffic"]
    assert traffic, "No Traffic records"
    groups = {n: Counter() for n in ["road", "monthly", "counterparty", "age", "remoteness"]}
    quality = defaultdict(Counter)
    seen = set()
    identity_mismatches = bed_only_rows = 0
    for row in traffic:
        key = tuple(row.get(c, "") for c in "ABCDEFGH")
        assert all(key), ("Blank Traffic dimension", key)
        assert key not in seen, ("Duplicate Traffic record", key)
        seen.add(key)
        year, count = integer(row["A"]), integer(row["M"])
        assert 2011 <= year <= 2021 and count >= 0, (year, count)
        assert row["B"] in MONTHS and row["E"] in AGES, key
        # Arithmetic parity only: blank deaths are not zero-death observations.
        cases = integer(row["I"]) if row.get("I") else 0
        deaths = integer(row["K"]) if row.get("K") else 0
        identity_mismatches += count != cases - deaths
        quality[year]["rows"] += 1
        for column in "IJKLM":
            if row.get(column) in (None, ""):
                quality[year][FIELDS[column] + "_blank_rows"] += 1
        bed_only_rows += count == 0 and integer(row["J"]) > 0
        user = row["G"]
        groups["road"][year, user] += count
        groups["monthly"][year, MONTHS.index(row["B"]) + 1, user] += count
        groups["counterparty"][year, user, row["H"]] += count
        groups["age"][year, user, row["E"]] += count
        groups["remoteness"][year, row["C"]] += count
    annual = Counter()
    for (year, _), count in groups["road"].items():
        annual[year] += count
    for name in ["monthly", "counterparty", "age"]:
        check = Counter()
        for key, count in groups[name].items():
            pair = (key[0], key[2]) if name == "monthly" else key[:2]
            check[pair] += count
        assert dict(check) == dict(groups["road"]), (name, "Road-user totals differ")
    remoteness_totals = Counter()
    for (year, _), count in groups["remoteness"].items():
        remoteness_totals[year] += count
    assert dict(remoteness_totals) == dict(annual), "Remoteness totals differ"
    assert not identity_mismatches, "Workbook case subtraction mismatch"
    audit = {
        "source_rows": len(rows), "traffic_rows": len(traffic), "duplicate_traffic_keys": 0,
        "raw_fields": profile(rows), "traffic_fields": profile(traffic),
        "traffic_quality_by_year": {str(y): dict(v) for y, v in sorted(quality.items())},
        "annual_hospitalisations": dict(sorted(annual.items())),
        "hospitalisation_identity_mismatches": identity_mismatches,
        "zero_hospitalisations_positive_bed_days_rows_retained": bed_only_rows,
        "bed_day_ratio_status": "WITHHELD: missing death fields, transfer attribution and numerator scope need resolution",
    }
    return groups, audit


def controls(archive, name):
    rows = list(sheet_rows(archive, name))
    if name == "T1":
        return {integer(r["A"]): integer(r["B"]) for r in rows if r.get("A", "").isdigit()}
    header = next(r for r in rows if r.get("A") == "Calendar year")
    total_col = next(c for c, label in header.items() if label == "Total")
    for row in rows:
        if row.get("A", "").isdigit():
            assert integer(row[total_col]) == sum(integer(row[c]) for c in header if c not in ["A", total_col]), "T2 total mismatch"
    return {(integer(r["A"]), user): integer(r[col])
            for r in rows if r.get("A", "").isdigit()
            for col, user in header.items() if col != "A" and user != "Total"}


def records(groups):
    national = Counter()
    for (year, _), count in groups["road"].items():
        national[year] += count
    tables = {}
    for name, dimensions in {
        "monthly": ["year", "month", "road_user"],
        "counterparty": ["year", "road_user", "counterparty"],
        "age": ["year", "road_user", "age_group"],
        "remoteness": ["year", "remoteness"],
    }.items():
        tables[name] = []
        for key, count in sorted(groups[name].items()):
            row = dict(zip(dimensions, key))
            row["hospitalisations"] = count
            if name in ["age", "counterparty", "remoteness"]:
                denominator = national[key[0]] if name == "remoteness" else groups["road"][key[:2]]
                column = "national_share_pct" if name == "remoteness" else "within_road_user_pct"
                row[column] = round(100 * count / denominator, 6) if denominator else None
            tables[name].append(row)
    tables["changes"] = []
    for user in ["All road users"] + sorted({u for _, u in groups["road"]}):
        before = national[2019] if user == "All road users" else groups["road"][2019, user]
        after = national[2020] if user == "All road users" else groups["road"][2020, user]
        pct = change_percent(before, after)
        tables["changes"].append({"road_user": user, "hospitalisations_2019": before,
            "hospitalisations_2020": after, "absolute_change": after - before,
            "change_pct": round(pct, 6) if pct is not None else None})
    return tables


def write_csv(path, rows):
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def plot_summaries(tables):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    folder = ROOT / "docs/figures/eda"
    folder.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                        "svg.fonttype": "none", "svg.hashsalt": "cos30045-eda"})
    users = ["Car driver", "Car passenger", "Motorcyclist", "Pedal cyclist", "Pedestrian"]
    rows = [r for r in tables["changes"] if r["road_user"] in users]
    fig, ax = plt.subplots(figsize=(10, 4.8), layout="constrained")
    for i, row in enumerate(rows):
        a, b = row["hospitalisations_2019"], row["hospitalisations_2020"]
        ax.plot([a, b], [i, i], color="#9aa5a8", linewidth=3)
        ax.scatter(a, i, color="#244d68", s=65, label="2019" if i == 0 else None, zorder=3)
        ax.scatter(b, i, color="#a74527", marker="D", s=65, label="2020" if i == 0 else None, zorder=3)
        ax.text(max(a, b) + 230, i, f'{row["change_pct"]:+.1f}%', va="center", fontsize=10)
    ax.set(yticks=range(len(rows)), yticklabels=[r["road_user"] for r in rows], xlim=(0, 15500),
           xlabel="Hospitalisations (counts)", title="The national decline hid a different pattern for cyclists")
    ax.invert_yaxis()
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="lower right")
    fig.text(.02, -.025, "EDA, not the D3 website. Selected groups only; all categories remain in the CSV. Source: BITRE September 2023.", fontsize=8)
    fig.savefig(folder / "road_user_change.svg", bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    values = {(r["road_user"], r["age_group"]): r["within_road_user_pct"] for r in tables["age"] if r["year"] == 2021}
    matrix = np.array([[values.get((u, age), 0) for age in AGES] for u in users])
    fig, ax = plt.subplots(figsize=(10, 4.7), layout="constrained")
    picture = ax.imshow(matrix, cmap="Blues", vmin=0, vmax=50, aspect="auto")
    for i in range(len(users)):
        for j in range(len(AGES)):
            ax.text(j, i, f"{matrix[i,j]:.1f}", ha="center", va="center", color="white" if matrix[i,j] >= 30 else "#142b3d")
    ax.set(xticks=range(len(AGES)), xticklabels=[a if a != "Missing" else "Unknown" for a in AGES],
           yticks=range(len(users)), yticklabels=users, xlabel="Age group (unequal widths)",
           title="Road users have different age compositions in 2021")
    fig.colorbar(picture, ax=ax, label="% within each road-user group")
    fig.text(.02, -.025, "EDA, not individual risk. All sexes included. Absent aggregate cells shown as zero. Source: BITRE September 2023.", fontsize=8)
    fig.savefig(folder / "age_composition.svg", bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    for name in ["road_user_change.svg", "age_composition.svg"]:
        path = folder / name
        path.write_text("\n".join(line.rstrip() for line in path.read_text(encoding="utf-8").splitlines()) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plots", action="store_true", help="Also regenerate EDA figures; requires matplotlib and numpy")
    args = parser.parse_args()
    with ZipFile(WORKBOOK) as archive:
        source = iter(sheet_rows(archive, "raw"))
        assert next(source) == FIELDS, "Unexpected raw columns"
        groups, audit = analyse([r for r in source if "A" in r])
        assert set(audit["annual_hospitalisations"]) == set(range(2011, 2022)), "Missing year"
        assert audit["annual_hospitalisations"] == controls(archive, "T1"), "T1 mismatch"
        assert dict(groups["road"]) == controls(archive, "T2"), "T2 mismatch"
        t4 = [r for r in sheet_rows(archive, "T4") if r.get("A", "").isdigit()]
        assert len(t4) == 11, "Missing T4 year"
        for row in t4:
            for col, label in zip("BCDE", ["Major Cities", "Regional", "Remote", "Missing"]):
                assert groups["remoteness"][integer(row["A"]), label] == integer(row[col]), "T4 mismatch"
    tables = records(groups)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for name, filename in {
        "changes": "road_user_changes_2019_2020.csv", "monthly": "monthly_by_road_user.csv",
        "counterparty": "counterparty_by_road_user.csv", "age": "age_by_road_user.csv",
        "remoteness": "remoteness_by_year.csv",
    }.items():
        write_csv(OUTPUT / filename, tables[name])
    audit.update(status="PASS", source_sha256=hashlib.sha256(WORKBOOK.read_bytes()).hexdigest(),
        matched_controls={"T1_years": 11, "T2_road_user_years": len(groups["road"]), "T4_remoteness_years": 44},
        export_rows={k: len(v) for k, v in tables.items()})
    (OUTPUT / "audit.json").write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    if args.plots:
        plot_summaries(tables)
    print(json.dumps({k: audit[k] for k in ["status", "source_rows", "traffic_rows", "matched_controls", "export_rows", "bed_day_ratio_status"]}, indent=2))


if __name__ == "__main__":
    main()
