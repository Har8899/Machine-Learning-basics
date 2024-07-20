#  Finding Eigenvalues and Eigenvectors
''' eigenvectors are vectors that, when that
transformation is applied, change only in scale (not direction).
'''

import numpy as np

# Create a Matrix
mat = np.array([[1, 2, 3],
                [2, 3, 4],
                [5, 6, 7]])

# Getting Eigenvalues and Eigenvectors
Eigenvalues, Eigenvectors = np.linalg.eig(mat)

# Eigenvalues
print(Eigenvalues)

# Eigenvectors
print(Eigenvectors)
