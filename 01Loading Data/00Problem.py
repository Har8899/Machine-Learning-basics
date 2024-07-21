# LOADING a Sample data set

# Load the Library
from sklearn import datasets

# Load the data
digits = datasets.load_digits()

# Create a feature matrix
feature = digits.data

# Create target vector
target = digits.target

# View first observation
print(feature[0])
print(target[0])

'''
load_boston
Contains 503 observations on Boston housing prices. It is a good dataset for
exploring regression algorithms.
load_iris
Contains 150 observations on the measurements of Iris flowers. It is a good data‐
set for exploring classification algorithms.
load_digits
Contains 1,797 observations from images of handwritten digits. It is a good data‐
set for teaching image classification.
'''