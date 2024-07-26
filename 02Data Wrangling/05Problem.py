# Replacing Values

# Load the library
import pandas as pd

# Load data
df = pd.read_csv('Data/titanic.csv')
print(df.columns)

# Replace two values show to rows
print(df['Sex'].replace('female','Women').head(2))

# Replace 'female' and 'male' with 'women' and 'man'
print(df['Sex'].replace(['female','male'],['Woman', 'Man']).head(3))

# Replacing values show to rows
print(df.replace(1, 'One').head(3))

# Replacing values, show two rows
print(df.replace('1st', 'First', regex=True).head(3))
