import pandas as pd
from pathlib import Path

folder = Path("data/raw/live_nav")

all_data = []

fund_codes = {
    "HDFC_Top100_NAV.csv": "125497",
    "SBI_Bluechip.csv": "119551",
    "ICICI_Bluechip.csv": "120503",
    "Nippon_LargeCap.csv": "118632",
    "Kotak_Bluechip.csv": "120841"
}

for file in folder.glob("*.csv"):

    print("Reading:", file.name)

    if file.name not in fund_codes:
        print("Skipping:", file.name)
        continue

    df = pd.read_csv(file)

    df["amfi_code"] = fund_codes[file.name]

    all_data.append(df[["amfi_code", "date", "nav"]])

merged = pd.concat(all_data, ignore_index=True)

merged.to_csv(
    "data/raw/02_nav_history_real.csv",
    index=False
)

print("Merged Shape:", merged.shape)
print("File Saved Successfully")