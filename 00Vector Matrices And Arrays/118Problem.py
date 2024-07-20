#  Inverting a Matrix
'''
The inverse of a square matrix, A, is a second matrix A–1, such that:
AA^-1 = I
'''

# Load the Library
import numpy as np

# Create a matrix
mat = np.array([[1, 2],
                [3, 4]])

# inverting
print(np.linalg.inv(mat))

# Multiply matrix and its inverse
print(mat @ np.linalg.inv(mat))
