# Week 3 Homework Assignment: Introduction to Databases with SQLite
# Loading Packages
import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import re
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
    
# Loading Datasets
sbm = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/sqlite_database_operations/main/datasets/113243405_StonyBrookUniversityHospital_standardcharges.csv')
sbm

# Load the dataset from the URL with specified encoding
url = "https://raw.githubusercontent.com/Alyssasorensen/sqlite_database_operations/main/datasets/596014973_Memorial_Hospital_Miramar_StandardCharges.csv"
memorial = pd.read_csv(url, encoding="ISO-8859-1")

# Now we can work with the 'memorial' DataFrame
memorial

# 1. Data Exploration and Analysis 
print("Dataset 1 Overview:")
print(sbm.head())
print("Dataset 2 Overview")
print(memorial.head)
    
print("Summary Statistics for Dataset 1:")
print(sbm.describe())
print("Summary Statistics for Dataset 2:")
print(memorial.describe())

# Cleaning Data and Handling Missing Values 
def clean_column_names(sbm):
    # Define a helper function to clean column names
    def clean_name(name):
        cleaned_name = re.sub(r'[^a-zA-Z0-9]', '', name)
        return cleaned_name.lower()

    # Rename columns using the helper function
    # This is using a list comprehend - e.g., we have a list to the right of the equals sign,
    # and inside the list, we are applying our function, for every col (or X) that exists in df.columns
    sbm.columns = [clean_name(col) for col in sbm.columns]
    return sbm

# Apply the clean_value function to all columns
sbm = clean_column_names(sbm)

sbm

def clean_column_names(memorial):
    # Define a helper function to clean column names
    def clean_name(name):
        cleaned_name = re.sub(r'[^a-zA-Z0-9]', '', name)
        return cleaned_name.lower()

    # Rename columns using the helper function
    # This is using a list comprehend - e.g., we have a list to the right of the equals sign,
    # and inside the list, we are applying our function, for every col (or X) that exists in df.columns
    memorial.columns = [clean_name(col) for col in memorial.columns]
    return memorial

# Apply the clean_value function to all columns
memorial = clean_column_names(memorial)

memorial

print("Missing Values in Dataset 1:")
print(sbm.isnull().sum())

print("Missing Values in Dataset 2:")
print(memorial.isnull().sum())

# Basic Statistics SBM
# Example: Frequency counts for a categorical column 'description' in Dataset 1
print("Frequency Counts for 'description' in Dataset 1:")
print(sbm['description'].value_counts())

# List of numerical columns to calculate measures of central tendency, measures of variability (spread), and frequency distribution
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

    # Calculate frequency distribution
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

# Display the analysis results
for column, results in analysis_results.items():
    print(f"Analysis for column: {column}")
    print(results)
    print("\n")

    # List of numerical columns to calculate measures of central tendency, measures of variability (spread), and frequency distribution
numerical_columns = [
    "empirehealthmedicareadvantagehmo",
    "empirehealthmedicaidhmo",
    "evernorthcommercialother",
    "fideliscommercialother",
    "fidelismedicareadvantagehmo",
    "fidelismedicaidhmo",
    "ghicommercialother",
    "healthfirstcommercialother",
    "healthfirstmedicareadvantagehmo",
    "healthfirstmedicaidhmo",
    "healthplushpmedicaidhmo",
    "healthplushpcommercialother",
    "healthplushpmedicareadvantagehmo",
    "humanacommercialother",
    "humanacommercialhmopos",
    "humanacommercialppoopenaccess",
    "meritainhealthcommercialother",
    "molinacommercialother",
    "optumcommercialother",
    "oxfordcommercialother",
    "oxfordcommercialhmopos",
    "tricarecommercialother",
    "unitedhealthcarecommercialother",
    "unitedhealthcaremedicareadvantagehmo",
    "unitedhealthcarecommercialhmopos",
    "unitedhealthcaremedicaidhmo",
    "unitedhealthcarecommercialppoopenaccess",
    "veteranfamilycommercialother",
]
analysis_results = {}
for column in numerical_columns:
    mean = sbm[column].mean()
    median = sbm[column].median()
    mode = sbm[column].mode()
    std_dev = sbm[column].std()
    min_value = sbm[column].min()
    max_value = sbm[column].max()

    # Calculate frequency distribution
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

# Display the analysis results
for column, results in analysis_results.items():
    print(f"Analysis for column: {column}")
    print(results)
    print("\n")

sbm_grosscharge_mean = sbm['grosscharge'].mean()
sbm_grosscharge_median = sbm['grosscharge'].median()
sbm_grosscharge_mode = sbm['grosscharge'].mode().values[0]

sbm_grosscharge_range = sbm['grosscharge'].max() - sbm['grosscharge'].min()
sbm_grosscharge_var = sbm['grosscharge'].var()
sbm_grosscharge_std= sbm['grosscharge'].std()
sbm_grosscharge_iqr = sbm['grosscharge'].quantile(0.75) - sbm['grosscharge'].quantile(0.25)
     
print("Measures of Central Tendency:")
print(f"Mean: {sbm_grosscharge_mean}")
print(f"Median: {sbm_grosscharge_median}")
print(f"Mode: {sbm_grosscharge_mode}")
print("\nMeasures of Spread:")
print(f"Range: {sbm_grosscharge_range}")
print(f"Variance: {sbm_grosscharge_var}")
print(f"Standard Deviation: {sbm_grosscharge_std}")
print(f"IQR (Interquartile Range): {sbm_grosscharge_iqr}")

sbm_aetnacommercialhmopos_mean = sbm['aetnacommercialhmopos'].mean()


sbm_aetnacommercialhmopos_median = sbm['aetnacommercialhmopos'].median()


sbm_aetnacommercialhmopos_mode = sbm['aetnacommercialhmopos'].mode().values[0]


sbm_aetnacommercialhmopos_range = sbm['aetnacommercialhmopos'].max() - sbm['aetnacommercialhmopos'].min()
sbm_aetnacommercialhmopos_var = sbm['aetnacommercialhmopos'].var()
sbm_aetnacommercialhmopos_std= sbm['aetnacommercialhmopos'].std()
sbm_aetnacommercialhmopos_iqr = sbm['aetnacommercialhmopos'].quantile(0.75) - sbm['aetnacommercialhmopos'].quantile(0.25)


print("Measures of Central Tendency:")
print(f"Mean: {sbm_aetnacommercialhmopos_mean}")
print(f"Median: {sbm_aetnacommercialhmopos_median}")
print(f"Mode: {sbm_aetnacommercialhmopos_mode}")
print("\nMeasures of Spread:")
print(f"Range: {sbm_aetnacommercialhmopos_range}")
print(f"Variance: {sbm_aetnacommercialhmopos_var}")
print(f"Standard Deviation: {sbm_aetnacommercialhmopos_std}")
print(f"IQR (Interquartile Range): {sbm_aetnacommercialhmopos_iqr}")

print (sbm['code'].value_counts())

print (sbm['description'].value_counts())

print (sbm['type'].value_counts())

print (sbm['packagelinelevel'].value_counts())

# Basic Statistics for Memorial
# Example: Frequency counts for a categorical column 'proceduredescription' in Dataset 2
print("Frequency Counts for 'proceduredescription' in Dataset 2:")
print(memorial['proceduredescription'].value_counts())

import pandas as pd

# Assuming you have a DataFrame named 'memorial'
numerical_columns = [
    "defaultcharge",
    "ercharge",
    "inpatienttherapy",
    "cashcharge"
]

analysis_results = {}
for column in numerical_columns:
    # Convert the column to numeric, and handle non-numeric values by setting them to NaN
    memorial[column] = pd.to_numeric(memorial[column], errors='coerce')

    # Filter out NaN values and calculate statistics
    valid_values = memorial[column].dropna()

    mean = valid_values.mean()
    median = valid_values.median()
    mode = valid_values.mode()
    std_dev = valid_values.std()
    min_value = valid_values.min()
    max_value = valid_values.max()

    # Calculate frequency distribution for valid values
    frequency_distribution = valid_values.value_counts().reset_index()
    frequency_distribution.columns = [column, "Frequency"]

    analysis_results[column] = {
        "Mean": str(mean),
        "Median": str(median),
        "Mode": str(mode),
        "Standard Deviation": str(std_dev),
        "Min Value": str(min_value),
        "Max Value": str(max_value),
        "Frequency Distribution": frequency_distribution
    }

# Display the analysis results
for column, results in analysis_results.items():
    print(f"Analysis for column: {column}")
    for key, value in results.items():
        print(f"{key}: {value}")
    print("\n")

memorial_defaultcharge_mean = memorial['defaultcharge'].mean()
memorial_defaultcharge_median = memorial['defaultcharge'].median()
memorial_defaultcharge_mode = memorial['defaultcharge'].mode().values[0]

memorial_defaultcharge_range = memorial['defaultcharge'].max() - memorial['defaultcharge'].min()
memorial_defaultcharge_var = memorial['defaultcharge'].var()
memorial_defaultcharge_std= memorial['defaultcharge'].std()
memorial_defaultcharge_iqr = memorial['defaultcharge'].quantile(0.75) - memorial['defaultcharge'].quantile(0.25)

print("Measures of Central Tendency:")
print(f"Mean: {memorial_defaultcharge_mean}")
print(f"Median: {memorial_defaultcharge_median}")
print(f"Mode: {memorial_defaultcharge_mode}")
print("\nMeasures of Spread:")
print(f"Range: {memorial_defaultcharge_range}")
print(f"Variance: {memorial_defaultcharge_var}")
print(f"Standard Deviation: {memorial_defaultcharge_std}")
print(f"IQR (Interquartile Range): {memorial_defaultcharge_iqr}")

print (memorial['cdmgrosschargeandcashpaysection'].value_counts())

print (memorial['procedurecode'].value_counts())

print (memorial['proceduredescription'].value_counts())

print (memorial['lawsonnumber'].value_counts())

print (memorial['ndc'].value_counts())

print (memorial['revenuecode'].value_counts())

print (memorial['cptcode'].value_counts())

print (memorial['unnamed8'].value_counts())

# Observations
# When observing both of the datasets I noticed how much missing data there was from both dataset 1 and dataset 2. There was a lot of missing data from both the numerical columns and the categorical columns. Both hospitals also had a lot of variety when it came to naming the columns and how they categorized each standard charge. For example, Stony Brook Medicine had a gross charge column and other charge columns based on the insurance provider and type of plan. Memorial hospital had a default charge column and a cash charge column.

# SBM Data Distribution

plt.figure(figsize=(9,9))
plt.hist(sbm['grosscharge'], bins=20, color='skyblue', edgecolor='black')
plt.title('Frequency of Stony Brook Medicine Gross Charge')
plt.xlabel('Gross Charge')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

plt.figure(figsize=(9,7))
plt.hist(sbm['discountedcashprice'], bins=20, color='red', edgecolor='black')
plt.title('Frequency of Discounted Cash Price')
plt.xlabel('Discounted Cash Price')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Memorial Data Distribution

plt.figure(figsize=(9,9))
plt.hist(memorial['defaultcharge'], bins=20, color='Green', edgecolor='black')
plt.title('Frequency of Default Charge')
plt.xlabel('Default Charge')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

plt.figure(figsize=(9,9))
plt.hist(memorial['cashcharge'], bins=20, color='Purple', edgecolor='black')
plt.title('Frequency of Cash Charge')
plt.xlabel('Cash Charge')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
