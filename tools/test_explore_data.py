"""AI prompt summary: test EDA edge cases and independent export reconciliation."""

from collections import Counter
import csv
import json
import unittest

from explore_data import OUTPUT, ROOT, analyse, change_percent, profile


def row(**changes):
    values = dict(zip("ABCDEFGHIJKLM", ["2021", "April", "Major Cities", "Traffic", "17-25",
        "Male", "Pedal cyclist", "Non-collision transport accident", "5", "12", "", "", "5"]))
    values.update(changes)
    return values


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


class EdgeCases(unittest.TestCase):
    def test_missing_and_zero_are_different(self):
        fields = profile([row(K=""), row(K="0")])
        self.assertEqual(fields["Died_cases"]["blank_rows"], 1)
        self.assertEqual(fields["Died_cases"]["zero_rows"], 1)
        self.assertIsNone(profile([row()])["Died_cases"]["minimum"])

    def test_bed_only_rows_and_unknown_categories_are_retained(self):
        groups, audit = analyse([row(I="", M="0", J="20", E="Missing", F="intersex or indeterminate or missing")])
        self.assertEqual(audit["traffic_rows"], 1)
        self.assertEqual(audit["zero_hospitalisations_positive_bed_days_rows_retained"], 1)
        self.assertIn((2021, "Pedal cyclist", "Missing"), groups["age"])
        self.assertEqual(groups["counterparty"][2021, "Pedal cyclist", "Non-collision transport accident"], 0)

    def test_duplicate_dimension_keys_are_rejected(self):
        with self.assertRaises(AssertionError):
            analyse([row(), row()])

    def test_invalid_counts_and_dates_are_rejected(self):
        for changes in [{"M": ""}, {"M": "-1"}, {"M": "1.5"}, {"A": "2022"},
                        {"B": "Not a month"}, {"H": ""}, {"J": "-2"}]:
            with self.subTest(changes=changes), self.assertRaises((AssertionError, ArithmeticError)):
                analyse([row(**changes)])

    def test_percent_change_has_an_explicit_zero_baseline(self):
        self.assertIsNone(change_percent(0, 10))
        self.assertIsNone(change_percent(0, 0))
        self.assertEqual(change_percent(20, 10), -50)
        self.assertEqual(change_percent(10, 20), 100)


class SavedAnalysis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.road = {(int(r["year"]), r["road_user"]): int(r["hospitalisations"])
                    for r in read_csv(ROOT / "data/processed/road_user_by_year.csv")}

    def test_month_counterparty_and_age_match_existing_road_totals(self):
        for name in ["monthly_by_road_user.csv", "counterparty_by_road_user.csv", "age_by_road_user.csv"]:
            totals, keys = Counter(), set()
            for r in read_csv(OUTPUT / name):
                key = tuple(v for k, v in r.items() if k not in ["hospitalisations", "within_road_user_pct"])
                self.assertNotIn(key, keys, name)
                keys.add(key)
                self.assertGreaterEqual(int(r["hospitalisations"]), 0)
                totals[int(r["year"]), r["road_user"]] += int(r["hospitalisations"])
            self.assertEqual(dict(totals), self.road, name)

    def test_percentages_include_all_recorded_categories(self):
        for name in ["counterparty_by_road_user.csv", "age_by_road_user.csv"]:
            totals = Counter()
            for r in read_csv(OUTPUT / name):
                key = int(r["year"]), r["road_user"]
                self.assertAlmostEqual(float(r["within_road_user_pct"]),
                    100 * int(r["hospitalisations"]) / self.road[key], places=5)
                totals[key] += float(r["within_road_user_pct"])
            for value in totals.values():
                self.assertAlmostEqual(value, 100, places=4)

    def test_key_findings_and_quality_gate(self):
        changes = {r["road_user"]: r for r in read_csv(OUTPUT / "road_user_changes_2019_2020.csv")}
        self.assertEqual(int(changes["Pedal cyclist"]["absolute_change"]), 1030)
        self.assertAlmostEqual(float(changes["Pedal cyclist"]["change_pct"]), 14.105724, places=5)
        self.assertEqual(int(changes["All road users"]["absolute_change"]), -1900)
        cell = next(r for r in read_csv(OUTPUT / "counterparty_by_road_user.csv")
            if r["year"] == "2021" and r["road_user"] == "Pedal cyclist"
            and r["counterparty"] == "Non-collision transport accident")
        self.assertEqual(int(cell["hospitalisations"]), 3705)
        audit = json.loads((OUTPUT / "audit.json").read_text())
        self.assertEqual(audit["traffic_rows"], 86140)
        q = audit["traffic_quality_by_year"]["2021"]
        self.assertEqual(q["Died_cases_blank_rows"], q["rows"])
        self.assertEqual(q["Died_bed_days_blank_rows"], q["rows"])
        self.assertTrue(audit["bed_day_ratio_status"].startswith("WITHHELD"))

    def test_remoteness_matches_annual_controls(self):
        annual = {int(r["year"]): int(r["hospitalisations"])
                  for r in read_csv(ROOT / "data/processed/annual_totals.csv")}
        totals = Counter()
        for r in read_csv(OUTPUT / "remoteness_by_year.csv"):
            totals[int(r["year"])] += int(r["hospitalisations"])
        self.assertEqual(dict(totals), annual)


if __name__ == "__main__":
    unittest.main()
