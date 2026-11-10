# import libraies
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pylab as plt

# load dataset
iris=load_iris()

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
model=RandomForestClassifier(n_estimators=100,random_state=42,max_depth=5)
model.fit(X_train,y_train)
# prediction
y_pred=model.predict(X_test)
# accuracy
acc=accuracy_score(y_test,y_pred)
cm=confusion_matrix(y_test,y_pred)
cr=classification_report(y_test,y_pred)

print("Accuracy is:",acc*100)
print(cm)
print(cr)
# graph