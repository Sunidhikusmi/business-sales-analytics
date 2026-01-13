import pandas as pd

print("Cleaning started")

# Load raw data
df = pd.read_csv(
    "data/raw/online_retail.csv",
    encoding="ISO-8859-1"
)

# Clean column names
df.columns = df.columns.str.strip().str.lower()

print("Columns:", df.columns.tolist())
print("Before cleaning:", df.shape)

# 1. Remove cancelled invoices (invoice starts with 'c')
df = df[~df['invoice'].astype(str).str.startswith('c')]

# 2. Remove missing customer id
df = df.dropna(subset=['customer id'])

# 3. Remove invalid quantity
df = df[df['quantity'] > 0]

# 4. Remove invalid price
df = df[df['price'] > 0]

# 5. Convert invoice date
df['invoicedate'] = pd.to_datetime(df['invoicedate'], errors='coerce')

# 6. Create revenue column
df['revenue'] = df['quantity'] * df['price']

print("After cleaning:", df.shape)

# Save cleaned data
df.to_csv(
    "data/processed/cleaned_online_retail.csv",
    index=False
)

print("Cleaning completed successfully")
