#  Creating a Simulated Dataset
#Load the library
from sklearn.datasets import make_regression

# Generate the feature matrix, target vextor amd the true coefficients
feature, target, coefficients = make_regression(n_samples=100,
                                                n_features=3,
                                                n_informative=3,
                                                n_targets=1,
                                                noise=0.0,
                                                coef= True,
                                                random_state=1)

# View the feature matrix and target vector
print('Feature Matrix\m', feature[:3])
print('Target vector\n', target[:3])



