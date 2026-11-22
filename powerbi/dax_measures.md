# DAX formulas for the Power BI dashboard

## Calculated columns (table: scored_banks)
```
Grade No = VALUE(MID(scored_banks[Grade], 7, 1))
Grade Short = "Grade " & scored_banks[Grade No]
```

## Measures
```
Banks = COUNTROWS(scored_banks)

Average Score = ROUND(AVERAGE(scored_banks[Score]), 1)

Average NPL % = ROUND(AVERAGE(scored_banks[NPA_Percent]), 2)

Average CET1 % = ROUND(AVERAGE(scored_banks[CET1_Percent]), 2)

High Risk Banks =
CALCULATE(
    COUNTROWS(scored_banks),
    scored_banks[Grade] = "Grade 4 - High Risk"
)
```

## What they do
- `MID(text, 7, 1)` takes the 7th character of "Grade 1 - Very Low Risk", which is the grade number.
- `CALCULATE` counts rows after applying a filter, here only Grade 4 banks.
- Measures react to slicers, so the cards change when the viewer picks a country.
