# Deleting a Column

# Load the library
import numpy as np
import pandas as pd

# Load the data
df = pd.read_csv('Data/titanic.csv')

# Delete a column
# print(df.drop('Sex', axis=1).head(2))

# Delete 2 columns
print(df.drop(['Sex','Age'], axis=1).head(2))

# Drop column
print(df.drop(df.columns[1], axis=1).head(2))

# Create a new dataframe
df2 = df.drop(df.columns[-1],axis=1).head(3)
print(df2)
