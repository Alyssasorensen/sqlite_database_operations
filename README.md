# sqlite_database_operations
## HHA 504 Homework Assignment 3

### Details on the Datasets I Selected
I selected datasets from Stony Brook Medicine and Memorial Healthcare System - Miramar Hospital. Both of the datasets focus on the hospital's standard charges for services. Both of the datasets were CSV files. The dataset from Stony Brook Medicine includes columns such as code, description, type, package/line_level, gross charge, discounted cash price, and other columns that focused on the standard charges of certain insurance providers and plan types. Stony Brook Medicine had a wide variety of insurance providers. The other dataset was focused on Memorial Hospital Miramar. The dataset from Memorial Hospital Miramar included columns such as CDM gross charge, procedure code, procedure description, lawson number, revenue code, and default charge. Both datasets had varying standard charges and categorical and numerical values.         

### Account of the Exploratory Data Analysis Process
Before beginning the EDA process, I had to load in the packages. After loading the packages, I loaded the datasets from Stony Brook Medicine and Memorial Hospital Miramar. To start the EDA process, I printed the heads of both datasets to show an overview of each. I then printed summary statistics for both of the datasets. This included the count, mean, standard deviation, minimum value, 25% quartile, 50% quartile, 75% quartile, and maximum value for each of the columns. Following this, I cleaned the data and handled missing values. I did this by entering the following code. 
```
 def clean_column_names(sbm):

   def clean_name(name):
        cleaned_name = re.sub(r'[^a-zA-Z0-9]', '', name)
        return cleaned_name.lower()

    sbm.columns = [clean_name(col) for col in sbm.columns]
    return sbm

 sbm = clean_column_names(sbm)
 sbm
```
This was done for both datasets. Then I did the following code for the number of missing values. 
```
print("Missing Values in Dataset 1:")
print(sbm.isnull().sum())
```
Then I found the basic statistics for Stony Brook Medicine. I started with founding the frequency counts for the categorial column "description." I then listed the numerical columns to calculate measures of central tendency, measures of variability, and frequency distribution. 
```
numerical_columns = [
    "grosscharge",
    "discountedcashprice",
    "deidentifiedmincontractedrate",
    "deidentifiedmaxcontractedrate",
    "derivedcontractedrate", 
    "1199commercialother",                         
    "aetnamedicareadvantagehmo",                  
    "aetnacommercialhmopos",                      
    "aetnacommercialppoopenaccess",               
    "aetnacommercialother",                     
    "empirehealthcommercialother",               
    "empirehealthcommercialppoopenaccess",       
    "bluecrossblueshieldcommercialother",       
    "beaconhealthcommercialother",                
    "carelonhealthcommercialother",               
    "cignacommercialppoopenaccess",               
    "cignacommercialother",                
    "cignacommercialhmopos",                     
    "ehfacetcommercialother",                    
    "emblemhealthcommercialppoopenaccess",        
    "emblemhealthcommercialother",               
    "emblemhealthcommercialhmopos",               
    "emblemhealthmedicaidhmo",                   
    "emblemhealthmedicareadvantagehmo",           
    "empirehealthcommercialhmopos",           
]

analysis_results = {}
for column in numerical_columns:
    mean = sbm[column].mean()
    median = sbm[column].median()
    mode = sbm[column].mode()
    std_dev = sbm[column].std()
    min_value = sbm[column].min()
    max_value = sbm[column].max()
    
    frequency_distribution = sbm[column].value_counts().reset_index()
    frequency_distribution.columns = [column, "Frequency"]
    
    analysis_results[column] = {
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Standard Deviation": std_dev,
        "Min Value": min_value,
        "Max Value": max_value,
        "Frequency Distribution": frequency_distribution
    }

for column, results in analysis_results.items():
    print(f"Analysis for column: {column}")
    print(results)
    print("\n")
```
After this I showed an example of finding the measures of central tendency of an individual column, it is based on "gross charge" and "aetnacommercialhmopos" at Stony Brook Medicine. I then printed the value counts for the categorical columns for the Stony Brook Medicine dataset. After completing the basic statistics for Stony Brook Medicine, I followed the same steps for the basic statistics of Memorial Health Miramar Hospital. I started with the frequency counts of "proceduredescription." I then found the measures of central tendency for default charge, er charge, inpatient therapy, and cash charge. I then printed a column labeled default charge to show the measures of central tendency for one column from the dataset. Following this, I printed the value counts for the categorical columns on the Memorial Health Miramar Hospital dataset. 
After doing basic statistics and value counts for both datasets, I completed data distributions for both datasets.    
```
plt.figure(figsize=(9,9))
plt.hist(sbm['grosscharge'], bins=20, color='skyblue', edgecolor='black')
plt.title('Frequency of Stony Brook Medicine Gross Charge')
plt.xlabel('Gross Charge')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
```
I did two column types from Stony Brook Medicine and Memorial Health Miramar Hospital to display the data distribution of certain standard charges. 
### Instructions to Replicate my SQLite Database Setup
First, I had to import sqlite3. Following this, I connected to the SQLite Database. This was done by using the following code. 
```
conn = sqlite3.connect('health.db')
cursor = conn.cursor()
conn.close()  # Close the connection when done
```
After this I created a table based on the Memorial Health Miramar Hospital as an example. 
I did this by using the following code. 
```
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
```
I then inserted sample data into the "memorial" table. 
```
cursor.execute('''
    INSERT INTO memorial
    VALUES
        ('11000004', 11000004, 'HC Private Most Common', 90006297, 'NaN', 110.0, 'NaN', 'NaN', 2445.0, 'NaN', 'NaN', 978.0),
        ('12000005', 12300001, 'HC Semi-Private Obstetrics', 90006306, 'NaN', 120.0, 'NaN', 'NaN', 2311.0, 'NaN', 'NaN', 924.0)
''')
```
I committed the changes using "conn.commit()." I then executed a query to fetch table names and print them.
```
cursor.execute('''
    SELECT name
    FROM sqlite_master
    WHERE type= 'table'
''')

tables = cursor.fetchall()

for value in tables:
    print(value)
```
This resulted in "('memorial',)"
After this, I ran the following code to display all of the values I inserted. 
```
cursor.execute('''
  SELECT * FROM memorial;
''')

print(cursor.fetchall())
```
After this I created the health.db file using the code below.
```
engine = create_engine('sqlite:///health.db')
```
To read the SQL database that I created, I inputted this code. 
```
memorial = pd.read_sql("select * from memorial;", conn)
memorial
```
Lastly, I automatically created tables by implmenting the to_sql function from Pandas, using the example data from Part 1, into the SQLite database. 
```
# Connect to the SQLite database
conn = sqlite3.connect('health.db')

memorial.to_sql('memorial', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
```
