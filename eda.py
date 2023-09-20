# Week 3 Homework Assignment: Introduction to Databases with SQLite

# 1. Data Exploration and Analysis:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/sqlite_database_operations/main/datasets/113243405_StonyBrookUniversityHospital_standardcharges.csv')

print("Dataset 1 Overview:")
print(df1.head())

print("Summary Statistics for Dataset 1:")
print(df1.describe())

# Example histogram for a numerical column 'Gross charge' in Dataset 1
plt.hist(df1['Gross charge'], bins=20)
plt.xlabel('Gross charge')
plt.ylabel('Frequency')
plt.title('Gross Charge Distribution in Dataset 1')
plt.show()

# Another example histogram for a numerical column 'Aetna-Commercial HMO/POS' in Dataset 1
plt.hist(df1['Aetna-Commercial HMO/POS'], bins=20)
plt.xlabel('Aetna-Commercial HMO/POS')
plt.ylabel('Frequency')
plt.title('Aetna-Commercial HMO/POS Distribution in Dataset 1')
plt.show()

print("Missing Values in Dataset 1:")
print(df1.isnull().sum())

# Example: Frequency counts for a categorical column 'Description' in Dataset 1
print("Frequency Counts for 'Description' in Dataset 1:")
print(df1['Description'].value_counts())

# 2. SQLite Database Operations:

import sqlite3
# Create or connect to the SQLite database
conn = sqlite3.connect('health.db')