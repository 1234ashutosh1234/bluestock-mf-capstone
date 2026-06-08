import pandas as pd

perf = pd.read_csv(
    "data/processed/fund_performance.csv"
)

risk = pd.read_csv(
    "data/processed/risk_analysis.csv"
)

summary = perf.merge(
    risk,
    on="amfi_code"
)

summary.to_csv(
    "data/processed/dashboard_summary.csv",
    index=False
)

print(summary)

print("\nDashboard dataset created.")