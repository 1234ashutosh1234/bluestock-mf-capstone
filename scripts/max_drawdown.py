import pandas as pd

df = pd.read_csv(
    "data/processed/nav_history_processed.csv"
)

results = []

for code in df["amfi_code"].unique():

    temp = df[
        df["amfi_code"] == code
    ].copy()

    temp["rolling_max"] = (
        temp["nav"].cummax()
    )

    temp["drawdown"] = (
        temp["nav"]
        - temp["rolling_max"]
    ) / temp["rolling_max"]

    results.append([
        code,
        temp["drawdown"].min()
    ])

result_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "max_drawdown"
    ]
)

result_df.to_csv(
    "data/processed/max_drawdown.csv",
    index=False
)

print(result_df)