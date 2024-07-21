# Loading JSON file
# load the library
import pandas as pd

df = pd.read_json('data.jsom', orient='colomns')

# view the first two rows
print(df.head(2))
