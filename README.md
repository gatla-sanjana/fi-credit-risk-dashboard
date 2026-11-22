# FI Credit Risk Dashboard

A Python (matplotlib) dashboard that visualises an internal credit-risk scorecard of 15 large banks (India, Europe, UK, US).

> **Illustrative learning project. Grades are an internal, relative scorecard, not official credit ratings. This is a Python dashboard, not a Power BI report.**

![Dashboard](dashboard.png)

## What it shows
1. **Bank score** - every bank's score out of 100, coloured by internal grade.
2. **Banks per grade** - how many banks fall in Grade 1 (very low risk) to Grade 4 (high risk).
3. **Asset quality vs CET1 capital** - NPL ratio against CET1 ratio, one dot per bank.
4. **Headline numbers** - average, highest and lowest scores.

## Where the data comes from
`data/scored_banks.csv` is produced by the companion project **fi-counterparty-credit-rating-model**, which holds the raw data (company annual results, with source links), the scoring method and the Excel report. Please read its README for the method and limitations.

## Run it
```
pip install -r requirements.txt
python dashboard.py
```

## Limitations
- Small sample of 15 banks; grades are relative to this sample only.
- NPL definitions differ by bank (Gross NPA, NPL, NPE, Stage 3, non-accrual), so the horizontal axis is not perfectly comparable.
- HDFC and Axis are FY2025; the other banks are FY2024. Currency amounts are converted approximately.
- Simple three-factor scorecard with judgement-based thresholds; not validated or back-tested.

## Power BI version
The `powerbi/` folder contains a step-by-step build guide and the DAX formulas for recreating this dashboard as an interactive Power BI report from `data/scored_banks.csv`. Once built, the `.pbix` file and a screenshot are added to that folder.

## Skills demonstrated
Python (pandas, matplotlib) for the dashboard; data visualisation and communication of bank credit-risk results; Power BI and DAX once the `.pbix` is added.
