#!/usr/bin/env python
# coding: utf-8

# Import necessary libraries
import kaggle
import zipfile
import pandas as pd
import sqlalchemy as sal
import pyodbc

# Download the dataset from Kaggle
!kaggle datasets download ankitbansal06/retail-orders -f orders.csv

# Extract the file from the zip archive
with zipfile.ZipFile('orders.csv.zip', 'r') as zip_ref:
    zip_ref.extractall()

# Read the data into a DataFrame, handling null values
df = pd.read_csv('orders.csv', na_values=['Not Available', 'unknown'])

# Display unique values in the 'Ship Mode' column
print(df['Ship Mode'].unique())

# Rename columns: make them lowercase and replace spaces with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Display the first 5 rows to check the renaming
print(df.head(5))

# Derive new columns for discount, sale price, and profit
df['discount'] = df['list_price'] * df['discount_percent'] * 0.01
df['sale_price'] = df['list_price'] - df['discount']
df['profit'] = df['sale_price'] - df['cost_price']

# Display the DataFrame to check the new columns
print(df)

# Convert 'order_date' from object data type to datetime
df['order_date'] = pd.to_datetime(df['order_date'], format="%Y-%m-%d")

# Drop 'list_price', 'cost_price', and 'discount_percent' columns
df.drop(columns=['list_price', 'cost_price', 'discount_percent'], inplace=True)

# Establish a connection to SQL Server using pyodbc
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=ANKIT\SQLEXPRESS;'
    r'DATABASE=master;'
    r'Trusted_Connection=yes;'
)
conn = pyodbc.connect(conn_str)
engine = sal.create_engine('mssql+pyodbc://', creator=lambda: conn)

# Load the data into SQL Server using the 'append' option
df.to_sql('df_orders', con=engine, index=False, if_exists='append')

# Close the connection
conn.close()
