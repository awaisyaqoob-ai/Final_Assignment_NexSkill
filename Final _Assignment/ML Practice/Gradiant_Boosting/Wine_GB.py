# import libraries
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import accuracy_score,mean_absolute_error,mean_squared_error
# load dataset
wine=load_wine()
# x and y 
X=wine.data
y=wine.target
print(X)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

# model tranining
model=GradientBoostingRegressor(n_estimators=100,random_state=42,learning_rate=0.1,max_depth=3)
model.fit(X_train,y_train)
# prediction
y_pred=model.predict(X_test)
print(y_pred)
# accuracy
