#  Calculating Dot Products

# Load the library
import numpy as np

# Create 2 vectors
vec_1 = np.array([1, 3, 4, 5])
vec2 = np.array([5, 6, 7 ,8])

# Dot product
print(np.dot(vec_1, vec2))

# 2nd way
print(vec_1 @ vec2)
