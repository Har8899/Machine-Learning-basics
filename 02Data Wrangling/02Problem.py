# Describing the Data
# load the library
import pandas as pd

# load the data
df = pd.read_csv('Data/Dataset.csv')

# show the data
print(df.head(3))

# Size of the data
print('Size of the data\n', df.size)

# Shape of the data
print('Shape of the data\n', df.shape)
# Show Statistics
print('Describe the data : \n', df.describe())
