# import libraries
import matplotlib.pylab as plt
from scipy.cluster import hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs


X,_=make_blobs(random_state=42,n_samples=50,cluster_std=0.6,centers=3)

plt.figure(figsize=(10,5))
dandogram=sch.dendrogram(sch.linkage(X,method='ward'))
plt.title('Dandogram')
plt.xlabel('X')
plt.ylabel("Y")
plt.show()


model=AgglomerativeClustering(n_clusters=3,linkage="ward")
y_pred=model.fit_predict(X)
plt.scatter(X[:,0],X[:,1],c=y_pred,cmap='rainbow',s=50)
plt.title("Hierarchial Cluster")
plt.show()