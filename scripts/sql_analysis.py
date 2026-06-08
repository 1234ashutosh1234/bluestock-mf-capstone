import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

query = """
SELECT
    amfi_code,
    MAX(nav) AS highest_nav
FROM nav_history
GROUP BY amfi_code
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()