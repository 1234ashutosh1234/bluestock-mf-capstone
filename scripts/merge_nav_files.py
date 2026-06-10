import pandas as pd

# Load raw NAV data
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

processed = []

for code in df["amfi_code"].unique():

    temp = df[df["amfi_code"] == code].copy()

    temp = temp.sort_values("date")

    # Create complete date range
    full_dates = pd.date_range(
        start=temp["date"].min(),
        end=temp["date"].max(),
        freq="D"
    )

    temp = (
        temp.set_index("date")
        .reindex(full_dates)
    )

    temp["amfi_code"] = code

    # Fill weekends/holidays
    temp["nav"] = temp["nav"].ffill()

    temp = temp.reset_index()

    temp.rename(
        columns={"index": "date"},
        inplace=True
    )

    processed.append(temp)

final_df = pd.concat(processed)

# Daily return calculation
final_df["daily_return"] = (
    final_df.groupby("amfi_code")["nav"]
    .pct_change()
)

final_df.to_csv(
    "data/processed/nav_history_processed.csv",
    index=False
)

print("Processed NAV file saved.")