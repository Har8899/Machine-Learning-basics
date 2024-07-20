# calculating average, variance and Standard Deviation

import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Return average
print(np.mean(matrix))

# Return Variance
print(np.var(matrix))

# return Standard deviation
print(np.std(matrix))

# Find the mean value in each column
print(np.mean(matrix, axis=0))
