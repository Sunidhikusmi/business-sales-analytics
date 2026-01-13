import sqlite3
import pandas as pd

# load cleaned data
df = pd.read_csv("data/processed/cleaned_online_retail.csv")

# connect to sqlite database
conn = sqlite3.connect("data/sales.db")

# load data into sql table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data loaded into SQL successfully")

conn.close()
