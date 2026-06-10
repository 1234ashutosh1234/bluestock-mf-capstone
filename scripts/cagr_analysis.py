import pandas as pd

nav_df = pd.read_csv(
    "data/processed/nav_history_processed.csv"
)

nav_df["date"] = pd.to_datetime(nav_df["date"])

results = []

for code in nav_df["amfi_code"].unique():

    temp = nav_df[
        nav_df["amfi_code"] == code
    ].copy()

    temp = temp.sort_values("date")

    start_nav = temp["nav"].iloc[0]
    end_nav = temp["nav"].iloc[-1]

    total_days = (
        temp["date"].max()
        - temp["date"].min()
    ).days

    years = total_days / 365.25

    cagr = (
        (end_nav / start_nav)
        ** (1 / years)
        - 1
    ) * 100

    results.append([
        code,
        start_nav,
        end_nav,
        round(cagr, 2)
    ])

result_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "start_nav",
        "end_nav",
        "cagr"
    ]
)

result_df.to_csv(
    "data/processed/cagr_report.csv",
    index=False
)

print(result_df)
print("\nCAGR Report Saved.")