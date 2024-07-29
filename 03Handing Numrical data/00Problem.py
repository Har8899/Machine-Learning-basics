# ReScaling a feature

# Load the Library
import numpy as np
from sklearn import preprocessing

# Create Feature
feature = np.array([[-900.5],
                    [-300.1],
                    [0],
                    [300.1],
                    [900.9]])

# Create Scaler
minmax_Scale = preprocessing.MinMaxScaler(feature_range=(0, 1))
# Scale feature
scaled_feature = minmax_Scale.fit_transform(feature)

# show feature
print(scaled_feature)