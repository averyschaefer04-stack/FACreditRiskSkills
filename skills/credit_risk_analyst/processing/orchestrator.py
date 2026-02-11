"""
Credit Risk Orchestrator
"""
from typing import Dict, List, Any
from .metrics import (
    calculate_altman_z_score,
    estimate_pd_from_z_score,
    calculate_lgd,
    calculate_expected_loss,
    calculate_credit_ratios,
    CreditMetricResult
)

# Helper to safely extract value from financial statements
def get_latest_value(stmts: List[Dict], key: str, default=0.0):
    if not stmts:
        return default
    # stmts are usually sorted desc by date, so first is latest
    return stmts[0].get(key, default) or default

def get_ttm_value(stmts: List[Dict], key: str, default=0.0):
    # Sum last 4 quarters if available, else use latest annual
    if not stmts:
        return default
    
    val = 0.0
    count = 0
    for stmt in stmts[:4]:
        v = stmt.get(key, 0.0)
        if v is not None:
            val += v
            count += 1
    return val if count > 0 else default

def run_credit_analysis(
    ticker: str,
    income_statements: List[Dict[str, Any]],
    balance_sheets: List[Dict[str, Any]],
    cash_flows: List[Dict[str, Any]],
    market_data: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Runs the full credit risk analysis pipeline.
    """
    
    # 1. Extract Data
    # Balance Sheet (Point in Time - Latest)
    bs = balance_sheets[0] if balance_sheets else {}
    total_assets = bs.get('totalAssets', 0)
    total_liabilities = bs.get('totalLiabilities', 0)
    current_assets = bs.get('totalCurrentAssets', 0)
    current_liabilities = bs.get('totalCurrentLiabilities', 0)
    retained_earnings = bs.get('retainedEarnings', 0)
    total_equity = bs.get('totalEquity', 0)
    total_debt = bs.get('totalDebt', 0)
    working_capital = current_assets - current_liabilities
    
    # Income Statement (TTM or Latest Annual)
    # Ideally TTM, but for simplicity taking latest annual or simplistic TTM if quarterly passed
    # Assuming the passed list is Annual or we just take latest. 
    # For more robustness, we should handle TTM calculation if quarterly list provided.
    is_stmt = income_statements[0] if income_statements else {}
    revenue = is_stmt.get('revenue', 0)
    ebit = is_stmt.get('operatingIncome', 0) # proxy for EBIT
    ebitda = is_stmt.get('ebitda', 0)
    interest_expense = is_stmt.get('interestExpense', 0)
    
    # Cash Flow
    cf_stmt = cash_flows[0] if cash_flows else {}
    fcf = cf_stmt.get('freeCashFlow', 0)

    # Market Data
    market_cap = market_data.get('marketCap', 0)
    current_price = market_data.get('price', 0)

    # 2. Calculate Metrics
    
    # Altman Z-Score
    is_manufacturing = True # Default assumption, can be refined with sector data
    z_score_result = calculate_altman_z_score(
        working_capital=working_capital,
        retained_earnings=retained_earnings,
        ebit=ebit,
        market_cap=market_cap,
        revenue=revenue,
        total_assets=total_assets,
        total_liabilities=total_liabilities,
        is_manufacturing=is_manufacturing
    )
    
    # PD
    pd_1yr = estimate_pd_from_z_score(z_score_result.value)
    
    # LGD
    lgd_result = calculate_lgd(
        total_assets=total_assets,
        total_liabilities=total_liabilities
    )
    
    # EAD (Estimate)
    # Simple assumption: EAD ~ Total Debt (ignoring undrawn lines for now)
    ead = total_debt
    
    # EL
    el_result = calculate_expected_loss(pd_1yr, lgd_result.value, ead)
    
    # Ratios
    ratios = calculate_credit_ratios(
        total_debt=total_debt,
        ebitda=ebitda,
        interest_expense=interest_expense,
        free_cash_flow=fcf,
        total_equity=total_equity
    )

    # 3. Format Output
    return {
        "ticker": ticker,
        "market_data": {
            "price": current_price,
            "market_cap": market_cap
        },
        "quantitative_scores": {
            "altman_z_score": z_score_result,
            "pd_1yr": pd_1yr,
            "lgd": lgd_result,
            "expected_loss": el_result
        },
        "ratios": ratios,
        "raw_data_summary": {
            "total_assets": total_assets,
            "total_debt": total_debt,
            "ebitda": ebitda,
            "leverage": ratios["Debt/EBITDA"].value,
            "interest_coverage": ratios["Interest Coverage"].value
        }
    }
