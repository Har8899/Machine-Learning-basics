# Applying a Function Over All Elements in a Column

# Load the library
import pandas as pd

# load the data
df = pd.read_csv('Data/titanic.csv')

# Create a function
def uppercase(x):
    return x.upper()

# Apply fuction show two rows
a= df['Name'].apply(uppercase)[3:5]
print(a)