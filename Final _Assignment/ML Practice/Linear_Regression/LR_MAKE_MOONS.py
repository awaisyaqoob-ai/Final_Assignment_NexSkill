# 1. import libraries

import seaborn as sns
import matplotlib.pylab as plt
from sklearn.datasets import make_moons


# 2. load data

mm=make_moons()

# 3. divid x and y
X,y=make_moons(
    n_samples=100,
    random_state=42,
    noise=0.2
)

# 4. graph

plt.scatter(X[:,0],X[:,1],c=y)
plt.title("Make Moon Dataset")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()