# import libraries
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay
import matplotlib.pylab as plt


# load dataset
wine=load_wine()
print(wine)

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
model=LogisticRegression()
model.fit(X_train,y_train)

# prediction
y_pred=model.predict(X_test)

# accuracy
acurracy=accuracy_score(y_test,y_pred)
cm=confusion_matrix(y_test,y_pred)
cr=classification_report(y_test,y_pred)

print("accuracy is :",acurracy)
print(cm)
print(cr)

# graph
disp=ConfusionMatrixDisplay(confusion_matrix=cm,
                            display_labels=wine.target_names)
disp.plot()
plt.title('Graph')
plt.show()