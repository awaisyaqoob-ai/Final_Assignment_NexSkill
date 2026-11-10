# import libraries
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

# load dataset
wine=load_wine()

# x and y divid
X=wine.data
y=wine.target

# train test split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2,stratify=y)

# model training
model = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)
model.fit(X_train,y_train)
# prediction
y_pred=model.predict(X_test)
print(y_pred)
# accuracy
