import pandas as pd

print("Program started")

df = pd.read_csv(
    "data/raw/online_retail.csv",
    encoding="ISO-8859-1"
)

df.columns = df.columns.str.strip()

print("Rows, Columns:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())
