import pandas as pd

url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"

df = pd.read_csv(url)

print("First 10 rows:")
print(df.head(10))

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Info:")
df.info()

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())
