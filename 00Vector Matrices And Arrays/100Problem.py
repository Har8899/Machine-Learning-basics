# 1.1 Creating a Vector

# Load the library
import numpy as np

# Create a vector as a row
vec_row = np.array([1,2,3])

print(vec_row)
print(type(vec_row))
print(vec_row.shape)

# Create a vector as a column

vec_col = np.array([[1,
                     2,
                     3]])

print(vec_col)
print(type(vec_col))
print(vec_col.shape)
