# Finding the Minimum, Maximum, Sum, Average, and
# Count

# Load the library
import pandas as pd

# Load the data
df = pd.read_csv('Data/titanic.csv')

# Calculate Statistics
print('Minimum', df['Age'].min())
print('Maximum', df['Age'].max())
print('Sum', df['Age'].sum())
print('Count', df['Age'].count())

'''
 pandas offers variance (var), stan‐
dard deviation (std), kurtosis (kurt), skewness (skew), standard error of the mean
(sem), mode (mode), median (median), a
'''