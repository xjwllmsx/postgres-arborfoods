import sqlite3
import pandas as pd
import os

# Set paths
DATA_DIR = "binder/data"
DB_PATH = "binder/arborfoods.db"

# Tables to load
tables = [
            'suppliers',
            'customers',
            'territories',
            'region',
            'us_states',
            'customer_demographics',
            'customer_customer_demo',
            'employees',
            'employee_territories',
            'orders',
            'order_details',
            'products',
            'shippers',
            'categories'
        ]

# Create SQLite database
conn = sqlite3.connect(DB_PATH)

for table in tables:
    csv_path = os.path.join(DATA_DIR, f"{table}.csv")
    df = pd.read_csv(csv_path)
    df.to_sql(table, conn, if_exists='replace', index=False)

conn.close()
