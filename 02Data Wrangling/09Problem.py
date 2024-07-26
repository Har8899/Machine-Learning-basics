# Handling Missing Values

# Load the library
import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('Data/titanic.csv')

# Finding missing value
print(df['Age'].isnull().head(2))
df['Age'] = df['Age'].replace(np.nan, df['Age'].mean())

print(df['Age'])

# Replace male with nan
df['Sex'] = df['Sex'].replace('male', np.nan)
print(df['Sex'])




