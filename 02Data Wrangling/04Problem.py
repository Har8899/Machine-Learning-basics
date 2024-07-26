# Selecting Rows Based on Conditionals

# Load the Library
import pandas as pd

# Create a url
url = 'Data/titanic.csv'

# Load the dataset
df = pd.read_csv(url)
print(df.head(3))

# show top two column where top two column of 'sex' ='female'
s = df[df['Sex'] == 'female']
print(s.head(2))

# Filter Rows
r = df[(df['Sex'] == 'female') & (df['Age'] >= 60)]

print(r.head(2))
