#  Finding Unique Values

# Load the library
import pandas as pd

# Load the data
df = pd.read_csv('Data/titanic.csv')

# show unique values
print(df['Sex'].unique())

# show value_counts
print(df['Sex'].value_counts())

# show value_count of PClass
print(df['Pclass'].value_counts())

# show no. of unique values
print(df['Pclass'].nunique())

