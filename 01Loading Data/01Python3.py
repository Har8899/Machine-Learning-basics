# Load the library
from sklearn.datasets import make_blobs

# Generate feature matrix and target vectir
features, target = make_blobs(n_samples=100,
                              n_features=2,
                              centers=3,
                              cluster_std=0.5,
                              shuffle= True,
                              random_state= 1)

# View feature matrix and target vector
print('feature Matrix\n', features[:3])
print('target vector\n', target[:3])

# Load library
import matplotlib.pyplot as plt
# View scatterplot
plt.scatter(features[:,0], features[:,1], c=target)
plt.show()