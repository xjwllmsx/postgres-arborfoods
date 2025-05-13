# export_postgres_tables.py

import os
import pandas as pd
from sqlalchemy import create_engine, inspect

# Configure this based on your docker-compose settings
DB_USER = ""  # Add username to the database
DB_PASSWORD = ""   # Add the password to the database
DB_HOST = ""   # Add the container address, typically localhost
DB_PORT = ""    # Add the container's port number
DB_NAME = ""   # Add the database name

# Output folder for CSVs
EXPORT_DIR = "binder/data"
os.makedirs(EXPORT_DIR, exist_ok=True)

# Create SQLAlchemy engine
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Use inspector to get table names
inspector = inspect(engine)
tables = inspector.get_table_names()

# Export each table to CSV
for table in tables:
    print(f"Exporting {table}...")
    df = pd.read_sql_table(table, con=engine)
    df.to_csv(os.path.join(EXPORT_DIR, f"{table}.csv"), index=False)

print(f"\n Exported {len(tables)} tables to {EXPORT_DIR}")
