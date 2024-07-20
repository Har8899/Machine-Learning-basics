#  Getting the Diagonal of a Matrix

# Load the Library
import numpy as np

# Create a Matrix
mat = np.array([[1, 2, 3],
                [2, 3, 4],
                [5, 6, 7]])

# Getting a diagonal
d = mat.diagonal()
print(d)

# above diagonal
d1 = mat.diagonal(offset=1)
print(d1)

# diagonal below
d2 = mat.diagonal(offset=-1)
print(d2)
