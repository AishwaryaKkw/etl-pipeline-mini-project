import pandas as pd
import sqlite3
from pathlib import Path

#Extract
csv_file = Path("sales_data.xlsx")
df = pd.read_excel(csv_file)



#Transform
df["total"] = df["quantity"] * df["price"]

summary = df.groupby("product", as_index=False)["total"].sum()
#grouping by product

# Load
db_file = Path("sales.db")
conn = sqlite3.connect(db_file)

df.to_sql("sales_raw", conn, if_exists="replace", index=False)
summary.to_sql("sales_summary", conn, if_exists="replace", index=False)
# raw data ---- sales_raw & sales_summary


print("Sales Summary from DB:")
query = "SELECT * FROM sales_summary ORDER BY total DESC;"
print(pd.read_sql(query, conn))

conn.close()
