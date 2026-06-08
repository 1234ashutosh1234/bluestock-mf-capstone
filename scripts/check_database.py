import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

query = """
SELECT COUNT(*) AS total_rows
FROM nav_history
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()