# import libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix , classification_report,ConfusionMatrixDisplay
import matplotlib.pylab as plt
import pandas as pd

# load data set
df=pd.read_csv('titanic_logistic_practice.csv')
print(df)

# divid x and y
X=df.drop("Survived",axis=1)
y=df["Survived"]

# train test split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)

# scaling
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)


# model traininng
model=LogisticRegression()
model.fit(X_train,y_train)

# prediction
y_pred=model.predict(X_test)
print(y_pred)
# accuracy
# graph