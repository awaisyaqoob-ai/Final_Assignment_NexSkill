# import libraries
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import matplotlib.pylab as plt


# load dataset
wine=load_wine()

# divid x and y
X=wine.data
y=wine.target

# train test split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)

# scaling
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

# model training
model=DecisionTreeClassifier(criterion='gini',random_state=42,max_depth=3)
model.fit(X_train,y_train)
# prediction
y_pred=model.predict(X_test)
# accuracy
acc=accuracy_score(y_test,y_pred)
cm=confusion_matrix(y_test,y_pred)
cf=classification_report(y_test,y_pred)
print(acc)
print(cm)
print(cf)
# graph

plt.figure(figsize=(5,5))
plot_tree(
    model,
    feature_names=wine.feature_names,
    class_names=wine.target_names,
    filled=True,
    fontsize=8
)
plt.title("Tree Graph")
plt.show()

