import pandas as pd

# Load the dataset
data = pd.read_csv("/Users/angielaptop/PycharmProjects/dsaproject3/maxai-excel-to-csv-converted.csv")

# Get basic information
print(data.info())    # Column names, data types, missing values
print(data.head())    # First 5 rows
print(data.describe())  # Summary statistics (numerical columns)

print(data.isnull().sum())  # Count missing values in each column
