# import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
import matplotlib.pylab as plt

# load dataset
iris=load_iris()
X=iris.data[:,:2]
print(X)
# model training
kmeans=KMeans(n_clusters=3,random_state=42)
kmeans.fit(X)
# prediction
y_kmeans=kmeans.predict(X)
centers=kmeans.cluster_centers_
# graph

plt.scatter(X[:,0],X[:,1],c=y_kmeans,cmap='viridis')
plt.scatter(centers[:,0],centers[:,1],c='red',s=200,marker='X')
plt.title('KMeans Graph')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
          