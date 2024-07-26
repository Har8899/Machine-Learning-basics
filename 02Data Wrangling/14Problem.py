# Grouping Rows by Time

# Load the Library
import pandas as pd
import numpy as np

# Create date ramge
time_index = pd.date_range('06/06/2018', '04/04/2024', periods=100000)

# create dataframe
df = pd.DataFrame(index=time_index)

# Create a coulumn of random values
df['Sales_Amt'] = np.random.randint(1, 10, 100000)

# group rows by week
'''
Using resample we can group the rows by a wide array of
 time periods (offsets)
'''
d = df.resample('W').sum()

print(d)