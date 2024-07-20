# Applying operations to elements

# Load the Library
import numpy as np

# Create a matrix

mat = np.array([[1, 2, 3],
                [4, 5, 6]])

# Create a function that adds 100 to something
add_100 = lambda i: i + 100

# create vectorized function
'''NumPy’s vectorize class converts a function into a function that can apply to all ele‐
ments in an array or slice of an array'''
vec = np.vectorize(add_100)

# apply function to all elements in matrix
print(vec(mat))