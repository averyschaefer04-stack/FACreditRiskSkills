import sys
import os
import json

# Add current directory to path so we can import skills
sys.path.append(os.getcwd())

from skills.credit_risk_analyst.processing.orchestrator import run_credit_analysis

def test_bac_credit_analysis():
    print("Testing Credit Risk Analysis for BAC (Bank of America)...")
    
    # Mock Data (based on approximate recent BAC figures)
    # total Assets ~ $3.2T
    # total Debt ~ $290B (Long Term) 
    # EBITDA ~ ? for a bank it's tricky, let's use Net Income + Tax + Provision
    
    mock_balance_sheet = [{
        "totalAssets": 3200000000000,
        "totalLiabilities": 2900000000000,
        "totalCurrentAssets": 1000000000000, # Rough estimate
        "totalCurrentLiabilities": 900000000000,
        "retainedEarnings": 200000000000,
        "totalEquity": 300000000000,
        "totalDebt": 290000000000 
    }]
    
    mock_income_stmt = [{
        "revenue": 100000000000,
        "operatingIncome": 30000000000,
        "ebitda": 35000000000,
        "interestExpense": 15000000000,
        "netIncome": 25000000000
    }]
    
    mock_cash_flow = [{
        "freeCashFlow": 20000000000
    }]
    
    mock_market_data = {
        "marketCap": 250000000000,
        "price": 34.50
    }
    
    result = run_credit_analysis(
        ticker="BAC",
        income_statements=mock_income_stmt,
        balance_sheets=mock_balance_sheet,
        cash_flows=mock_cash_flow,
        market_data=mock_market_data
    )
    
    print("\nanalysis Result:")
    print(json.dumps(result, indent=2, default=str))
    
    # Assertions
    z_score = result['quantitative_scores']['altman_z_score'].value
    pd = result['quantitative_scores']['pd_1yr']
    
    print(f"\nCalculated Z-Score: {z_score}")
    print(f"Estimated PD: {pd:.2%}")
    
    if z_score > 0:
        print("✅ Z-Score calculation successful")
    else:
        print("❌ Z-Score calculation failed")

if __name__ == "__main__":
    test_bac_credit_analysis()
