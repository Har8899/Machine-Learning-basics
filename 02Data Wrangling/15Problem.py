# Looping Over a Column

# Load the library
import pandas as pd

# load the data
df = pd.read_csv('Data/titanic.csv')

# print first two names uppercased
for name in df['Name'][0:2]:
    print(name.upper())

# Show two names uppercase in list
print([name.upper() for name in df['Name'][0:2]])
