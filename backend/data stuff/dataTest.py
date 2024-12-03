import pandas as pd

# Load the dataset
# for using the dataset here, paste **YOUR** ABSOLUTE FILE PATH into the read_csv function argument
data = pd.read_csv("/Users/angielaptop/PycharmProjects/dsaproject3/maxai-excel-to-csv-converted.csv")

# Get basic information
print(data.info())    # Column names, data types, missing values
print(data.head())    # First 5 rows
print(data.describe())  # Summary statistics (numerical columns)

# dropping data that doesn't have value (3 perfume names not included)
data.dropna(subset=["perfume"], inplace=True)

data["notes"] = data["notes"].str.split(", ")

#for testing whether notes are split up accurately
print(data["notes"].head())
print(data.loc[7000, "notes"])  # Replace 0 with any row index

#testing failed rows
#failed_rows = data[data["notes"].apply(type) != list]
#print(failed_rows)
