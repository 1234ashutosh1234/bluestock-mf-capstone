import pandas as pd

summary = pd.read_csv(
    "data/processed/dashboard_summary.csv"
)

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

final_df = summary.merge(
    fund_master[
        ["amfi_code", "scheme_name"]
    ],
    on="amfi_code",
    how="left"
)

final_df.to_csv(
    "data/processed/dashboard_summary_final.csv",
    index=False
)

print(final_df.head())