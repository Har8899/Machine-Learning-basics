# Applying a Function Over All Elements in a Column

# Load the library
import pandas as pd

# load the data
df = pd.read_csv('Data/titanic.csv')

# group rows apply funtion to the group
print(df.groupby('Sex').apply(lambda x : x.count()))