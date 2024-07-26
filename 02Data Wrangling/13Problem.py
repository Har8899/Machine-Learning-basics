#  Grouping Rows by Values

# Load the library
import pandas as pd

# load the data
df = pd.read_csv('Data/titanic.csv')

# Group by rows
print(df.groupby('Sex').mean())

# Group by name
print(df.groupby('Survived')['Name'].count())

# Group rows, calculate mean
print(df.groupby(['Sex', 'Survived'])['Age'].mean())
