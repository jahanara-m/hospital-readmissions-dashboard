import pandas as pd
import psycopg2
from io import StringIO
import numpy as np

# USER CONFIGURATION: Set the path to your CSV file here
csv_file_path = '/Downloads/unplanned_hospital_visits.csv'  # <-- CHANGE THIS to desired file location

# 1. Read and clean the CSV
df = pd.read_csv(csv_file_path,
                 dtype={'Footnote': str}) 
print(f"Loaded {len(df)} rows")

# 2. Replace 'Not Available' with None 
df = df.replace('Not Available', None)

# 3. Connect to PostgreSQL
conn = psycopg2.connect("dbname=hospital_readmissions")
cur = conn.cursor()
print("Connected to database.")

# 4. Create table (drop if exists)
cur.execute("DROP TABLE IF EXISTS unplanned_visits;")

# Generate CREATE TABLE statement from DataFrame columns
columns = df.columns.tolist()
create_statement = "CREATE TABLE unplanned_visits (" + \
                   ", ".join([f'"{col}" TEXT' for col in columns]) + \
                   ");"
cur.execute(create_statement)
conn.commit()

# 5. Use COPY to insert data
buffer = StringIO()

df.to_csv(buffer, index=False, header=False, na_rep='\\N')  
buffer.seek(0)

cur.copy_expert("COPY unplanned_visits FROM STDIN WITH CSV", buffer)
conn.commit()

# 6. Verify row count
cur.execute("SELECT COUNT(*) FROM unplanned_visits")
count = cur.fetchone()[0]
print(f"Verified: {count} rows in table 'unplanned_visits'")

cur.close()
conn.close()