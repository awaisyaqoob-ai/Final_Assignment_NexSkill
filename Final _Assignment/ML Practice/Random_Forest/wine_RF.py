# import libraries
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
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
model=RandomForestClassifier(criterion="gini",max_depth=3,n_estimators=100)
model.fit(X_train,y_train)
# predict 
y_pred=model.predict(X_test)
# accuracy
acc=accuracy_score(y_test,y_pred)
cr=classification_report(y_test,y_pred)
cm=confusion_matrix(y_test,y_pred)
print(acc)
print(cr)
print(cm)
# graph