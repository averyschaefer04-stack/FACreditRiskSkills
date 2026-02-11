---
name: credit-risk-analyst
description: Autonomous credit risk analyst that assesses corporate creditworthiness using the "5 Cs" framework (Character, Capacity, Capital, Collateral, Conditions) and quantitative models (Altman Z-Score, Estimated PD/LGD/EL). Generates a professional credit memo with a final credit rating and recommendation.
version: 1.0.0
---

# Credit Risk Analyst Skill

## Quick Reference

```
/credit-risk-analyst BAC          # Assess Bank of America
/credit-risk-analyst F --full     # Full credit deep dive on Ford
```

---

## ORCHESTRATION OVERVIEW

This skill follows a linear DRIVER workflow to produce a comprehensive credit memo:

1.  **[DISCOVER] Data Collection**: Fetches financial statements, market data, news, and filings.
2.  **[PROCESS] Quantitative Analysis**: Calculates credit metrics (PD, LGD, EL, Leverage, Coverage) using Python.
3.  **[REPRESENT] Structural Design**: Prepares the data for the "5 Cs" qualitative assessment.
4.  **[IMPLEMENT] Credit Memo Drafting**: Uses GenAI to synthesize quantitative and qualitative factors into a memo.
5.  **[REFLECT] Final Review**: Outputs a structured markdown report.

---

## STEP 1: DATA COLLECTION

The skill utilizes the `financialdatasets-mcp` and `tavily-mcp` to gather necessary data.

### Data Requirements
-   **Financial Statements**: Annual and Quarterly Income Statement, Balance Sheet, Cash Flow (5 years).
-   **Market Data**: Current market cap, share price, volatility (for KMV-like models).
-   **News**: Recent news regarding management, litigation, and market conditions.
-   **Filings**: 10-K/10-Q for qualitative risk factors.

---

## STEP 2: QUANTITATIVE PROCESSING

Logic is implemented in `processing/metrics.py`.

### Key Metrics
-   **Probability of Default (PD)**:
    -   *Proxy*: Mapping Altman Z-Score and Ohlson O-Score to historical default rates.
-   **Loss Given Default (LGD)**:
    -   *Estimate*: (1 - Recovery Rate). Recovery Rate estimated based on Tangible Asset Coverage and industry averages (typically 45% LGD for unsecured senior debt).
-   **Exposure at Default (EAD)**:
    -   *Estimate*: Total Debt + (0.5 * Unused Credit Lines - estimated).
-   **Expected Loss (EL)**: `PD * LGD * EAD`.
-   **Capacity Ratios**:
    -   Debt / EBITDA
    -   EBITDA / Interest Expense
    -   Free Operating Cash Flow / Debt
-   **Capital Ratios**:
    -   Debt / Equity
    -   Tangible Net Worth

---

## STEP 3: QUALITATIVE ASSESSMENT (The "5 Cs")

The LLM is prompted to analyze the "5 Cs" based on the collected data and calculated metrics.

1.  **Character**: Management integrity, track record, transparency, litigation history.
2.  **Capacity**: Ability to repay based on cash flow stability and coverage ratios.
3.  **Capital**: Financial cushion, leverage, and skin in the game.
4.  **Collateral**: Quality and liquidity of assets backing the debt.
5.  **Conditions**: Macroeconomic environment, industry trends, and regulatory landscape.

---

## OUTPUT FORMAT

A standard Credit Memo format:

-   **Executive Summary**: Recommendation (Approve/Decline), Internal Rating.
-   **Credit Risk Dashboard**: Key metrics (PD, LGD, EL, Z-Score).
-   **5 Cs Analysis**: Detailed breakdown of each factor.
-   **Financial Analysis**: Trend analysis of ratios.
-   **Peer Comparison**: Benchmarking against key competitors.
-   **Risk Factors & Mitigants**: Specific risks and how they are addressed.
