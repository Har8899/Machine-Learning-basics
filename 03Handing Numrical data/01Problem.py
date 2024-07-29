# Standardizing a Feature

# Load the Libraries
import numpy as np
from sklearn.preprocessing import *

# Create feature
x = np.array([[-1000.1],
              [-200.2],
              [500.3],
              [600.6],
              [9000.9]])

# Create Feature
scaler = StandardScaler()

# Transform the feature
standardized = scaler.fit_transform(x)

# show the feature
print(standardized)

# print mean and std
print('mean :', round(standardized.mean()))
print('Std', standardized.std())


'''
If our data has significant outliers, it can negatively impact our standardization by
affecting the feature’s mean and variance. In this scenario, it is often helpful to instead
rescale the feature using the median and quartile range. In scikit-learn, we do this
using the RobustScaler method
'''
# Create scaler
robust_scaler = RobustScaler()

# Transform Feature
tf = robust_scaler.fit_transform(x)
# show the feature
print(tf)
