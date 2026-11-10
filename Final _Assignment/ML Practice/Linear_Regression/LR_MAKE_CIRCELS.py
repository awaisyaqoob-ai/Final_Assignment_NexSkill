# 1. import libraries

import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
from sklearn.datasets import make_circles


# 2. load data

mc=make_circles()
print(mc)

# 3. dived to X and Y

# X,y=make_circles(
#     n_samples=100,
#     noise=0.05,
#     random_state=42
# )

X,y=make_circles(
    n_samples=100,
    random_state=42,
    noise=0.2
)

# 4. make graph

plt.scatter(X[:,0],X[:,1],c=y)
plt.title("Make Circle dataset")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()









# plt.scatter(X[:,0],X[:,1],c=y)
# plt.title(" Make Circles")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()