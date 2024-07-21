# loading the csv file
import pandas as pd

# Load data
df = pd.read_excel('data.excel', sheet_name=0, header=1)

print(df.head(2))
