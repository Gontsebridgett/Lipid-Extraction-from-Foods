# Extraction of Lipids from Foods (Soxhlet / Solvent Extraction)

A protocol for quantifying total fat content in a food sample using solvent
extraction, paired with a Python script that calculates percent fat content
from pre- and post-extraction sample weights.

## Overview

Total lipid (fat) content in food samples is commonly determined using
solvent extraction methods such as Soxhlet extraction, where an organic
solvent (typically petroleum ether or hexane) continuously washes over a dried
food sample, dissolving and extracting lipids over repeated cycles. After
extraction, the solvent is evaporated off, leaving the extracted fat, which is
weighed to determine the percentage of fat in the original sample.

## Principle

- **Sample preparation:** food sample is dried (to remove moisture, which
  would otherwise interfere with extraction) and finely ground to maximise
  surface area
- **Solvent extraction:** non-polar solvent dissolves lipids (which are
  non-polar) while leaving proteins, carbohydrates, and moisture largely
  unextracted
- **Solvent evaporation:** extracted solvent-fat mixture is evaporated,
  leaving behind only the fat residue
- **Calculation:** % Fat = (mass of extracted fat &divide; mass of original sample) &times; 100

## Materials & Reagents

- Dried, ground food sample
- Petroleum ether or hexane (extraction solvent)
- Soxhlet extraction apparatus (extraction chamber, condenser, solvent flask) or equivalent solvent extraction setup
- Analytical balance
- Drying oven
- Extraction thimbles (cellulose)
- Rotary evaporator or heating apparatus for solvent removal

## Method (Summary)

| Step | Action |
|---|---|
| 1 | Dry food sample in oven (~100&ndash;105&deg;C) to constant weight; record dry weight |
| 2 | Grind sample finely and place in a pre-weighed extraction thimble |
| 3 | Record thimble + sample weight |
| 4 | Load thimble into Soxhlet apparatus; add solvent to the flask |
| 5 | Reflux for 4&ndash;8 hours (solvent cycles repeatedly through the sample) |
| 6 | Remove thimble; evaporate residual solvent from the extraction flask |
| 7 | Weigh the flask + extracted fat; calculate fat mass by difference |
| 8 | Calculate % fat relative to original dry sample weight |

## Result Interpretation

| % Fat (dry weight basis) | Typical food category |
|---|---|
| &lt;5% | Low-fat foods (most vegetables, lean grains) |
| 5&ndash;20% | Moderate-fat foods (dairy, some meats) |
| &gt;20% | High-fat foods (nuts, oils, fatty meats) |

## Analysis Script

`lipid_extraction_analysis.py` calculates percent fat content for a set of
food samples from pre- and post-extraction weights recorded in
`sample_data/extraction_weights.csv`, and flags samples by fat category.

### Usage

```bash
pip install -r requirements.txt
python lipid_extraction_analysis.py
```

### Sample output

```
Sample         Dry Wt(g)   Fat Extracted(g)   % Fat     Category
------------------------------------------------------------------
Peanuts        5.02        2.41               48.0      High-fat
Oats           5.10        0.34               6.7       Moderate-fat
Spinach(dry)   5.00        0.08               1.6       Low-fat
Cheddar        5.05        1.68               33.3      High-fat
```

## Repository Structure

```
lipid-extraction-from-foods/
├── README.md
├── lipid_extraction_analysis.py
├── requirements.txt
└── sample_data/
    └── extraction_weights.csv
```

## Disclaimer

Sample values are illustrative and approximate typical published fat content
ranges for these food types; they were not obtained from an actual extraction
run.
