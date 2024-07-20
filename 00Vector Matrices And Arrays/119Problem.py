#  Generating Random Values
'''
By specifying a seed value, the function ensures that the sequence of random numbers
generated remains the same across multiple runs, providing deterministic behavior and
allowing reproducibility in random number generation
'''

# load the library
import numpy as np

# set seed
np.random.seed(0)

# Generate three random float between 0.0 and 1.0
print(np.random.random(3))

# Generate three random integer between 1 and 11
print(np.random.randint(0, 11, 3))

# Draw three numbers from normal distribution  where mean is 0.0 and std is 1.0
print(np.random.normal(0.0, 1.0, 3))

# Draw three numbers from a logistic distribution with mean 0.0 and scale of 1.0
print(np.random.logistic(0.0, 1.0, 3))

# Draw three numbers greater than or equal to 1.0 and less than 2.0
print(np.random.uniform(1.0, 2.0, 3))
