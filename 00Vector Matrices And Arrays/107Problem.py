# Reshaping Arrarys
# load the library
import numpy as np

# Create a Matrix
mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12]])

# reshape the matrix
m = mat.reshape(2, 6)
print(m)
