# Concatenating DataFrames

# Load the library
import pandas as pd

# data
d = {'id':[1, 2, 3, 4],
     'Name': ['Anna', 'Elsa','Rups','Hash'],
     'Age': [34, 23, 34, 35]}
df1 = pd.DataFrame(d, columns=['id', 'Name','Age'])

d2 = {'id': [5,6,7,8],
      'Name': ['riya', 'deepa', 'Priya', 'yash'],
      'Age': [43, 36, 23, 32]}
df2 = pd.DataFrame(d2, columns=['id','Name','Age'])


# concat dataframes by rows
print(pd.concat([df1,df2], axis=0))

# cocat dataframes by columns
print(pd.concat([df1,df2], axis=1))