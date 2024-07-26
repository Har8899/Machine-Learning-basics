# Rename Column
# Load the library
import pandas as pd
# load data
df = pd.read_csv('Data/titanic.csv')
print(df.columns)
print(df.rename(columns={'Pclass':'Passanger Class','Sex':'Gender'}).head(2))
