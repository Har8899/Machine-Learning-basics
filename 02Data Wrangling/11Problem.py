# Deleting a row

# Load the library
import pandas as pd

# load the data
df = pd.read_csv('Data/titanic.csv')

# Deleting a row
print(df[df['Sex'] != 'female'].head(2))

# Deleting row
print(df[df.index != 0].head(3))
