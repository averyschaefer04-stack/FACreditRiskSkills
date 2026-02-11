"""
Credit Risk Metrics Calculator
"""
import math
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional

@dataclass
class CreditMetricResult:
    value: float
    interpretation: str
    components: Dict[str, Any] = field(default_factory=dict)
    flags: List[str] = field(default_factory=list)

def safe_div(a, b, default=0.0):
    return a / b if b and b != 0 else default

def calculate_altman_z_score(
    working_capital: float,
    retained_earnings: float,
    ebit: float,
    market_cap: float,
    revenue: float,
    total_assets: float,
    total_liabilities: float,
    is_manufacturing: bool = True
) -> CreditMetricResult:
    """
    Calculates Altman Z-Score.
    """
    flags = []
    if total_assets == 0:
        return CreditMetricResult(0.0, "Cannot calculate - no assets", flags=["Missing data"])

    x1 = safe_div(working_capital, total_assets)
    x2 = safe_div(retained_earnings, total_assets)
    x3 = safe_div(ebit, total_assets)
    x4 = safe_div(market_cap, total_liabilities)
    x5 = safe_div(revenue, total_assets)

    if is_manufacturing:
        z = 1.2*x1 + 1.4*x2 + 3.3*x3 + 0.6*x4 + 0.999*x5
        if z > 2.99:
            interpretation = "Safe Zone"
        elif z > 1.81:
            interpretation = "Grey Zone"
            flags.append("Grey Zone - Moderate Risk")
        else:
            interpretation = "Distress Zone"
            flags.append("DISTRESS - High Bankruptcy Risk")
    else:
        # Z'' model for non-manufacturing
        z = 6.56*x1 + 3.26*x2 + 6.72*x3 + 1.05*x4
        if z > 2.60:
            interpretation = "Safe Zone"
        elif z > 1.10:
            interpretation = "Grey Zone"
            flags.append("Grey Zone - Moderate Risk")
        else:
            interpretation = "Distress Zone"
            flags.append("DISTRESS - High Bankruptcy Risk")

    components = {
        "x1_working_capital": x1,
        "x2_retained_earnings": x2,
        "x3_ebit": x3,
        "x4_market_cap_to_liab": x4,
        "x5_asset_turnover": x5
    }
    
    return CreditMetricResult(round(z, 2), interpretation, components, flags)

def estimate_pd_from_z_score(z_score: float) -> float:
    """
    Rough mapping of Z-Score to 1-year Probability of Default.
    Based on historical mappings (e.g., Altman 2005).
    """
    if z_score > 3.0:
        return 0.001  # AAA/AA (~0.1%)
    elif z_score > 2.5:
        return 0.005  # A/BBB (~0.5%)
    elif z_score > 2.0:
        return 0.015  # BB (~1.5%)
    elif z_score > 1.5:
        return 0.05   # B (~5%)
    elif z_score > 1.0:
        return 0.15   # CCC (~15%)
    else:
        return 0.30   # D (<30% - Distressed)

def calculate_lgd(
    total_assets: float,
    total_liabilities: float,
    intangible_assets: float = 0.0,
    secured_debt: float = 0.0
) -> CreditMetricResult:
    """
    Estimates Loss Given Default (LGD).
    Base assumption: Unsecured Senior Debt often has ~45% LGD.
    Adjust based on Tangible Asset Coverage.
    """
    tangible_assets = total_assets - intangible_assets
    
    # Coverage Ratio for Total Liabilities
    asset_coverage = safe_div(tangible_assets, total_liabilities)
    
    # Simple heuristic model for LGD
    # If assets cover liabilities 2x, LGD is low.
    # If assets < liabilities, LGD is high.
    
    base_lgd = 0.45 # Industry standard base
    
    if asset_coverage > 2.0:
        estimated_lgd = 0.10 # Very high recovery expected
        interpretation = "Very High Recovery Expected"
    elif asset_coverage > 1.5:
        estimated_lgd = 0.25 # High recovery
        interpretation = "High Recovery Expected"
    elif asset_coverage > 1.0:
        estimated_lgd = 0.45 # Average recovery (Base)
        interpretation = "Average Recovery Expected"
    elif asset_coverage > 0.8:
        estimated_lgd = 0.60 # Low recovery
        interpretation = "Low Recovery (Assets < Liab buffer)"
    else:
        estimated_lgd = 0.80 # Very low recovery
        interpretation = "Very Low Recovery (Deeply Insolvent)"
        
    return CreditMetricResult(
        estimated_lgd,
        interpretation,
        {"asset_coverage": asset_coverage, "tangible_assets": tangible_assets}
    )

def calculate_expected_loss(
    pd: float,
    lgd: float,
    ead: float
) -> CreditMetricResult:
    """
    EL = PD * LGD * EAD
    """
    el = pd * lgd * ead
    return CreditMetricResult(
        el,
        f"Expected Loss: ${el:,.2f}",
        {"PD": pd, "LGD": lgd, "EAD": ead}
    )

def calculate_credit_ratios(
    total_debt: float,
    ebitda: float,
    interest_expense: float,
    free_cash_flow: float,
    total_equity: float
) -> Dict[str, CreditMetricResult]:
    """
    Calculates key credit ratios.
    """
    # Leverage
    debt_to_ebitda = safe_div(total_debt, ebitda)
    debt_to_equity = safe_div(total_debt, total_equity)
    
    # Coverage
    interest_coverage = safe_div(ebitda, interest_expense)
    
    # FCF to Debt
    fcf_to_debt = safe_div(free_cash_flow, total_debt)
    
    results = {}
    
    # Interpretations
    # Debt/EBITDA
    if debt_to_ebitda < 2.0:
        interp = "Conservative Leverage (<2.0x)"
    elif debt_to_ebitda < 4.0:
        interp = "Moderate Leverage (2.0x - 4.0x)"
    else:
        interp = "High Leverage (>4.0x)"
    results["Debt/EBITDA"] = CreditMetricResult(debt_to_ebitda, interp)
    
    # Interest Coverage
    if interest_coverage > 10.0:
        interp = "Excellent Coverage (>10x)"
    elif interest_coverage > 5.0:
        interp = "Strong Coverage (5x - 10x)"
    elif interest_coverage > 2.0:
        interp = "Adequate Coverage (2x - 5x)"
    else:
        interp = "Weak Coverage (<2x) - Risk of Default"
    results["Interest Coverage"] = CreditMetricResult(interest_coverage, interp)
    
    results["Debt/Equity"] = CreditMetricResult(debt_to_equity, "Capital Structure")
    results["FCF/Debt"] = CreditMetricResult(fcf_to_debt, "Ability to Paydown Debt")
    
    return results
