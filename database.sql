# 2. SQLite Database Operations

import sqlite3
# Connect to the SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('health.db')
conn.close()  # Close the connection when done

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('health.db')
cursor = conn.cursor()

# Create the 'memorial' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS memorial
    (
        [cdmgrosschargeandcashpaysection] TEXT, 
        [procedurecode] INTEGER, 
        [proceduredescription] TEXT, 
        [lawsonnumber] INTEGER, 
        [ndc] TEXT, 
        [revenuecode] INTEGER, 
        [cptcode] INTEGER,
        [unnamed8] TEXT,
        [defaultcharge] REAL,
        [ercharge] REAL,
        [inpatienttherapy] REAL,
        [cashcharge] REAL
    )
''')

# Insert sample data into the 'memorial' table
cursor.execute('''
    INSERT INTO memorial
    VALUES
        ('11000004', 11000004, 'HC Private Most Common', 90006297, 'NaN', 110.0, 'NaN', 'NaN', 2445.0, 'NaN', 'NaN', 978.0),
        ('12000005', 12300001, 'HC Semi-Private Obstetrics', 90006306, 'NaN', 120.0, 'NaN', 'NaN', 2311.0, 'NaN', 'NaN', 924.0)
''')

# Commit the changes 
conn.commit()

# Execute a query to fetch table names and print them
cursor.execute('''
    SELECT name
    FROM sqlite_master
    WHERE type= 'table'
''')

tables = cursor.fetchall()

for value in tables:
    print(value)

cursor.execute('''
  SELECT * FROM memorial;
''')

print(cursor.fetchall())

engine = create_engine('sqlite:///health.db')

memorial = pd.read_sql("select * from memorial;", conn)
memorial

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('health.db')

# Assuming you have a DataFrame named 'example_data'
memorial.to_sql('memorial', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
