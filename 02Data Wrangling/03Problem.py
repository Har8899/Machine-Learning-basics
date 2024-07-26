#  Navigating DataFrames

# Load the Library
import pandas as pd

# Load the data
df = pd.read_csv('Data/titanic.csv')

print(df.head(5))

# select first row
fr = df.iloc[0]
print('First Row :\n', fr)

# Select 3 rows
Tr = df.iloc[1:4]
print('three rows:\n', Tr)

# Set index
df = df.set_index(df['Name'])

print(df.loc['Braund, Mr. Owen Harris'])

