import pandas as pd

perf = pd.read_csv(
    "data/processed/dashboard_summary_final.csv"
)

perf["score"] = (
    perf["return_pct"].rank()
    +
    perf["sharpe_ratio"].rank()
)

perf = perf.sort_values(
    "score",
    ascending=False
)

perf.to_csv(
    "data/processed/fund_scorecard.csv",
    index=False
)

print(perf)