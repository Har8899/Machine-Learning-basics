# Rank of the Matrix

# Load library
import numpy as np
# Create matrix
matrix = np.array([[1, 9, 1],
                   [5, 6, 10],
                   [1, 8, 15]])
# Return rank
'''Rank of a Matrix. The rank of a matrix is equal to the number of linearly independent 
rows (or columns) in it. Hence, it cannot more than its number of rows and columns. 
For example, if we consider the identity matrix of order 3 × 3
, all its rows (or columns) are linearly independent and hence its rank is 3.'''

print(np.linalg.matrix_rank(matrix))
