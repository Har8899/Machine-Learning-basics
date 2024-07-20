# Create a matrix

# Load the Library
import numpy as np
from scipy import sparse

# Create a matrix
mat_1 = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])
print(mat_1)

# Create a sparse matrix
mat = np.array([[0, 0],
                [0, 1],
                [3, 0]])
sparse_mat = sparse.csr_matrix(mat)
print(sparse_mat)

# Create a Large Sparse Matrix
mat2 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
sparse_Mat2 = sparse.csr_matrix(mat2)
print('Large Sparse Matrix :', sparse_Mat2)

