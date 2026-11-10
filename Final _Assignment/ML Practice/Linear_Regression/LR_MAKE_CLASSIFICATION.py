# 1. import libraries

import matplotlib.pylab as plt
from sklearn.datasets import make_classification

# 2. load data

mc=make_classification()

# 3. divid to x and y

X,y=make_classification(
    n_classes=2,
    n_samples=100,
    random_state=42
)

# 4. make graph

plt.scatter(X[:,0],X[:,1],c=y)
plt.show()