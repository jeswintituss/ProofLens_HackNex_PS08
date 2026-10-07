import pandas as pd
from agent.code_generator import generate_code
from execution.runner import execute_code

def test_total_revenue():
    df = pd.read_csv("data/sales.csv")
    code, _ = generate_code("What is the total revenue?", df)
    result = execute_code(code, df)
    assert result["success"]
    assert "615,000.00" in result["output"]

def test_profit_refusal():
    df = pd.read_csv("data/sales.csv")
    code, explanation = generate_code("What was our profit?", df)
    assert code is None
    assert "profit" in explanation.lower()
