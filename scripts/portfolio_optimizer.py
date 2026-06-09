import pandas as pd
import numpy as np
from scipy.optimize import minimize

df = pd.read_csv(
    "data/processed/dashboard_summary_final.csv"
)

returns = df["return_pct"].values

n = len(returns)

def objective(weights):
    return -np.dot(weights, returns)

constraints = ({
    "type": "eq",
    "fun": lambda x: np.sum(x) - 1
})

bounds = [(0,1)] * n

initial = np.ones(n) / n

result = minimize(
    objective,
    initial,
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

weights = result.x

portfolio = pd.DataFrame({
    "scheme_name": df["scheme_name"],
    "weight": weights
})

portfolio.to_csv(
    "data/processed/optimal_portfolio.csv",
    index=False
)

print(portfolio)