"""
lipid_extraction_analysis.py

Calculates percent fat content of food samples from pre- and post-extraction
weights (Soxhlet/solvent extraction method) and classifies each sample by
fat category.
"""

import csv
from pathlib import Path

DATA_PATH = Path(__file__).parent / "sample_data" / "extraction_weights.csv"


def load_data(path: Path):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["dry_weight_g"] = float(row["dry_weight_g"])
            row["fat_extracted_g"] = float(row["fat_extracted_g"])
            rows.append(row)
    return rows


def percent_fat(dry_weight: float, fat_extracted: float) -> float:
    return round((fat_extracted / dry_weight) * 100, 1)


def categorize(pct_fat: float) -> str:
    if pct_fat < 5:
        return "Low-fat"
    elif pct_fat <= 20:
        return "Moderate-fat"
    return "High-fat"


def main():
    rows = load_data(DATA_PATH)

    print(f"{'Sample':<15}{'Dry Wt(g)':<12}{'Fat Extracted(g)':<19}{'% Fat':<10}{'Category'}")
    print("-" * 68)

    for row in rows:
        pct = percent_fat(row["dry_weight_g"], row["fat_extracted_g"])
        category = categorize(pct)
        print(f"{row['sample_id']:<15}{row['dry_weight_g']:<12}{row['fat_extracted_g']:<19}{pct:<10}{category}")


if __name__ == "__main__":
    main()
