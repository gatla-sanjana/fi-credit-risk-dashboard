# Credit risk concepts used in this project

A one-page note on three ideas behind the scorecard: CAMELS, CET1 and IFRS 9 stages, and how each connects to the model.

## 1. CAMELS - a framework for judging a bank
CAMELS is a supervisory rating framework from US bank regulators. Each letter is one area an analyst looks at:

| Letter | Area | Question it answers |
|---|---|---|
| **C** | Capital adequacy | Does the bank have enough capital to absorb losses? |
| **A** | Asset quality | How much of its lending is going bad? |
| **M** | Management | Is the bank well run, with good risk controls? |
| **E** | Earnings | Is it profitable enough to build capital? |
| **L** | Liquidity | Can it meet withdrawals and payments when due? |
| **S** | Sensitivity to market risk | How exposed is it to interest-rate and market moves? (added in 1997) |

Supervisors score each area from 1 (strongest) to 5 (weakest). Credit analysts use the same headings as a checklist when reviewing a bank counterparty.

**In this project:** CET1 covers **C**, the NPL ratio covers **A**, and ROA covers **E**. The model does **not** cover M, L or S, which is a stated limitation and a natural next step (for example, adding a liquidity ratio).

## 2. CET1 - the quality of a bank's capital
- **CET1 ratio = Common Equity Tier 1 capital / risk-weighted assets (RWA).**
- CET1 is the highest-quality capital: mainly shareholders' equity and retained earnings, which can absorb losses straight away.
- RWA are the bank's assets weighted by how risky they are, so a loan to a risky borrower counts for more than a government bond.
- Under Basel III the minimum is 4.5%, plus a 2.5% capital conservation buffer (7% in total). Banks also have extra buffers and requirements set by their supervisor.
- A higher CET1 ratio means a thicker cushion against losses.
- **Caution:** banks calculate RWA in different ways, so CET1 ratios are comparable only roughly across countries.

**In this project:** CET1 is used for every bank, because "total capital ratio" is reported on different bases in different countries.

## 3. IFRS 9 stages - how loans are classified for expected losses
IFRS 9 makes banks recognise **expected credit losses (ECL)** early, based on three stages:

| Stage | Meaning | Loss provision |
|---|---|---|
| **1** | Performing; no significant rise in credit risk | 12-month expected loss |
| **2** | Significant increase in credit risk since the loan was made (for example, 30+ days overdue is a common trigger) | Lifetime expected loss |
| **3** | Credit-impaired / in default (commonly 90+ days overdue, or unlikely to pay) | Lifetime expected loss |

Stage 3 loans are the closest IFRS 9 match to "non-performing loans".

**Why NPL ratios differ between banks:**
- European banks often report an NPL / NPE ratio or Stage 3 ratio.
- Indian banks report gross NPA under the central bank's asset classification rules (loan overdue more than 90 days).
- US banks use a different accounting model (CECL) and often report non-accrual or nonperforming loans.

**In this project:** this is why the README lists the NPL definition used for each bank and why the model's asset-quality scores are only approximately comparable.

## Be ready to answer
1. **Why do you use CET1 rather than total capital?** It is the highest-quality loss-absorbing capital and is reported more consistently across jurisdictions.
2. **What is a Stage 3 loan?** A loan in default or credit-impaired, for which the bank recognises lifetime expected losses.
3. **Which CAMELS areas does your model cover, and what is missing?** Capital, Asset quality and Earnings are covered. Management, Liquidity and Sensitivity to market risk are not. Liquidity would be the first addition.

*This note is a study summary for a learning project, not regulatory advice.*
