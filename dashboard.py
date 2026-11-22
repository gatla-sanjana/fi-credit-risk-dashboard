"""
FI Credit Risk Dashboard (Python / matplotlib)
----------------------------------------------
Reads data/scored_banks.csv (produced by the fi-counterparty-credit-rating-model
project) and draws a 4-panel dashboard: scores, grade distribution,
asset quality vs capital, and headline numbers.

Run:  python dashboard.py
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GRADES = ["Grade 1 - Very Low Risk", "Grade 2 - Low Risk", "Grade 3 - Medium Risk", "Grade 4 - High Risk"]
colors = {GRADES[0]: "#2E7D32", GRADES[1]: "#9CCC65", GRADES[2]: "#FFB300", GRADES[3]: "#C62828"}

df = pd.read_csv("data/scored_banks.csv").sort_values(["Score", "Bank_Name"], ascending=[False, True]).reset_index(drop=True)

fig, ax = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle("FI Credit Risk Dashboard - Internal Scorecard (15 banks)", fontsize=16, fontweight="bold")

d = df.sort_values("Score")
ax[0, 0].barh(d.Bank_Name, d.Score, color=[colors[g] for g in d.Grade])
ax[0, 0].set_title("Bank score (higher = lower risk)"); ax[0, 0].set_xlim(0, 100)
ax[0, 0].set_xlabel("Score out of 100")
for y, s in enumerate(d.Score): ax[0, 0].text(s + 1, y, f"{s:.0f}", va="center", fontsize=8)

counts = df.Grade.value_counts().reindex(GRADES).fillna(0).astype(int)
ax[0, 1].bar([g.split(" - ")[0] for g in GRADES], counts.values, color=[colors[g] for g in GRADES])
ax[0, 1].set_title("Banks per internal grade"); ax[0, 1].set_ylabel("Number of banks")
ax[0, 1].set_ylim(0, counts.max() + 1)
for i, v in enumerate(counts.values): ax[0, 1].text(i, v + 0.1, str(v), ha="center")

for g in GRADES:
    s = df[df.Grade == g]
    ax[1, 0].scatter(s.NPA_Percent, s.CET1_Percent, s=90, color=colors[g], label=g.split(" - ")[0], edgecolor="k")
for _, r in df.iterrows():
    ax[1, 0].annotate(r.Bank_Name.replace(" International", "").replace(" Group", ""),
                      (r.NPA_Percent, r.CET1_Percent), fontsize=7, xytext=(4, 3), textcoords="offset points")
ax[1, 0].set_title("Asset quality vs CET1 capital")
ax[1, 0].set_xlabel("NPL / NPA ratio (%) - lower is better (definitions differ by bank)")
ax[1, 0].set_ylabel("CET1 ratio (%)"); ax[1, 0].legend(title="Grade", fontsize=8)

ax[1, 1].axis("off")
hi, lo = df.Score.max(), df.Score.min()
best = ", ".join(df[df.Score == hi].Bank_Name)
worst = ", ".join(df[df.Score == lo].Bank_Name)
text = (f"Average score: {df.Score.mean():.1f} / 100\n\n"
        f"Highest score: {best} ({hi:.0f})\n\n"
        f"Lowest score: {worst} ({lo:.0f})\n\n"
        f"Grade 3-4 (Medium/High): {int(counts.iloc[2] + counts.iloc[3])} of {len(df)} banks")
ax[1, 1].text(0.02, 0.95, text, fontsize=13, va="top", linespacing=1.15)
ax[1, 1].text(0.02, 0.0, "Illustrative scorecard on public data.\nNot an official credit rating.\n"
              "NPL definitions and reporting years differ by bank.", fontsize=9, style="italic", color="#555")
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("dashboard.png", dpi=150)
print("Saved dashboard.png")
