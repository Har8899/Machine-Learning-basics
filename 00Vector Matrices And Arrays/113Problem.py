#   Calculating the Trace of a Matrix
''' The trace of a matrix is the sum of the diagonal elements and is often used under the
hood in machine learning methods. Given a NumPy multidimensional array, we can
calculate the trace using trace. '''
# Load the Library
import numpy as np

# Create a Matrix
mat = np.array([[1, 2, 3],
                [2, 3, 4],
                [5, 6, 7]])

# Getting trace of a matrix
print( mat.trace())
