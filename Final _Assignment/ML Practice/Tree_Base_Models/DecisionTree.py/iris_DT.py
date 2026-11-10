# import libraries
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib.pylab as plt

# load daraset
iris=load_iris()
print(iris)
# divid x and y
X=iris.data
y=iris.target

# train test split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)
# scaliing
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

# model training
model=DecisionTreeClassifier(criterion='gini',max_depth=3,random_state=42)
model.fit(X_train,y_train)
# prediction
y_pred=model.predict(X_test)
print(y_pred)
# accuracy
cm=confusion_matrix(y_test,y_pred)
accuracy=accuracy_score(y_test,y_pred)
cf=classification_report(y_test,y_pred)

print(cm)
print(accuracy)
print(cf)


# graph

plt.figure(figsize=(5,5))
plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    fontsize=8
)
plt.title("Tree")
plt.show()