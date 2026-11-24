# Build the Power BI version

Power BI Desktop is free for Windows: search "Power BI Desktop" in the Microsoft Store, install it and sign in (a work or school account may be requested; a personal Microsoft account often works for Desktop).

Data file: `data/scored_banks.csv` from this repository.

## 1. Load the data
1. Open Power BI Desktop and click **Get data -> Text/CSV**.
2. Select `scored_banks.csv` and click **Load**. The table is called `scored_banks`.
3. Click **Table view** (left side) and check that `Score`, `NPA_Percent`, `CET1_Percent` and `ROA_Percent` show as decimal numbers.

## 2. Add helper columns
In Table view choose **New column** and enter each formula (also in `dax_measures.md`):
```
Grade No = VALUE(MID(scored_banks[Grade], 7, 1))
Grade Short = "Grade " & scored_banks[Grade No]
```
Select the `Grade Short` column, then **Column tools -> Sort by column -> Grade No**, so grades appear in order 1 to 4.

## 3. Add measures
Select the table, click **New measure**, and add the five measures from `dax_measures.md` (Banks, Average Score, Average NPL, Average CET1, High Risk Banks).

## 4. Build the report page (Report view)
| Visual | Fields | Notes |
|---|---|---|
| 4 **Card** visuals (top row) | Banks, Average Score, Average CET1 %, High Risk Banks | One measure per card |
| **Clustered bar chart** | Y-axis: Bank_Name; X-axis: Score; Legend: Grade Short | Sort by Score descending |
| **Column chart** | X-axis: Grade Short; Y-axis: Count of Bank_Name | Shows banks per grade |
| **Scatter chart** | X: NPA_Percent; Y: CET1_Percent; Legend: Grade Short; Details: Bank_Name | Asset quality vs capital |
| 2 **Slicers** | Country; Grade Short | Lets viewers filter the whole page |
| **Table** (optional) | Bank_Name, Country, Score, Grade, Data_Check | Detail at the bottom |

Colours (set under **Format -> Visual -> Colors**, per legend value): Grade 1 `#2E7D32`, Grade 2 `#9CCC65`, Grade 3 `#FFB300`, Grade 4 `#C62828`.

Add a title text box: **FI Credit Risk Dashboard - Internal Scorecard**, and a footer text box: *Illustrative scorecard on public data. Not an official credit rating. NPL definitions differ by bank.*

## 5. Save and publish to GitHub
1. **File -> Save as** `fi_credit_risk_dashboard.pbix`.
2. Take a screenshot of the finished page and save it as `powerbi/powerbi_dashboard.png`.
3. On GitHub open the `powerbi` folder -> **Add file -> Upload files**, and upload the `.pbix` and the screenshot.
4. In the main `README.md`, add under the Python picture: `![Power BI dashboard](powerbi/powerbi_dashboard.png)`.

Only describe the project as having a Power BI dashboard after step 5 is done.

## 6. Be ready to explain
- What each measure calculates and why you made `Grade No` (sorting).
- Why a slicer is useful for a risk team.
- How you would refresh the dashboard when new bank results are published (update the CSV and click Refresh).
