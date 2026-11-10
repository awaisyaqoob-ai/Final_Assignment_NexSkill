# import libraries
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score,ConfusionMatrixDisplay
import matplotlib.pylab as plt

# load data
bc=load_breast_cancer()
print(bc)

# divid x and y
X=bc.data
y=bc.target

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
accuracy=accuracy_score(y_test,y_pred)
cr=classification_report(y_test,y_pred)
cf=confusion_matrix(y_test,y_pred)

print(accuracy)
print(cr)
print(cf)

# graph
disp=ConfusionMatrixDisplay(confusion_matrix=cf,
                            display_labels=bc.target_names)
disp.plot()
plt.title("Graph")
plt.show()


#----#
