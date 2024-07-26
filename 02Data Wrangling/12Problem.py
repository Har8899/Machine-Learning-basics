# Droping the Duplicates
#load the library
import pandas as pd

# load the data
df = pd.read_csv('Data/titanic.csv')

# drop duplicates show first two rows
print(df.drop_duplicates().head(2))

# show the length of original data and data after removing duplicates
print('Original data', len(df))
print('data after removing duplicates', len(df.drop_duplicates()))

#Drop dupilates
print(df.drop_duplicates(subset='Sex').head(5))

#Droping duplicates
print((df.drop_duplicates(subset='Sex', keep='last').head(5)))
