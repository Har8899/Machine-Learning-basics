# Normalizing Observation

# Load the libraries
import numpy as np
from sklearn.preprocessing import Normalizer

# Crate a featture matrix
features = np.array([[0.5, 0.5],
                    [1.1, 3.5],
                    [1.5, 20.2],
                    [1.64, 34.5],
                    [10.9, 3.3]])

# create normalizer
normalizer = Normalizer(norm='l2')

'''
s. Normalizer
rescales the values on individual observations to have unit norm (the sum of their
lengths is 1). This type of rescaling is often used when we have many equivalent fea‐
tures (e.g., text classification when every word or n-word group is a feature).
'''
# Transform feature matrix
print(normalizer.transform(features))

'''
Normalizer provides three norm options with
Euclidean norm (often called L2)

'''

# Transform feature matrix
f_l1_norm = Normalizer(norm='l1').transform(features)
print(f_l1_norm)