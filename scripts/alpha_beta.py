import pandas as pd
import numpy as np

df = pd.read_csv("data/processed/dashboard_summary_final.csv")

# Simple placeholder benchmark
benchmark_return = df["return_pct"].mean()

alpha_beta = []

for _, row in df.iterrows():
    fund_return = row["return_pct"]

    beta = fund_return / benchmark_return if benchmark_return != 0 else 0
    alpha = fund_return - (beta * benchmark_return)

    alpha_beta.append([
        row["amfi_code"],
        row["scheme_name"],
        round(alpha, 4),
        round(beta, 4)
    ])

result = pd.DataFrame(
    alpha_beta,
    columns=["amfi_code", "scheme_name", "alpha", "beta"]
)

result.to_csv(
    "data/processed/alpha_beta.csv",
    index=False
)

print(result)
print("\nAlpha Beta report saved.")