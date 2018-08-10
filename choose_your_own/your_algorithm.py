#!/usr/bin/python3
import sys
from time import time
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

### Random Forest (Def case accuracy 92 and max when n_estimators=15 at 92.8)
"""
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators = 15,)

t0 = time()
clf.fit(features_train,labels_train)
print("Training time: ",round(time()-t0,3),"s")

t1 = time()
pred = clf.predict(features_test)
print("Testing time: ",round(time()-t1,3),"s")
"""
### Naive Bayes (Accuracy 88.4%)

"""
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
t0 = time()
clf.fit(features_train,labels_train)
print("Training time:", round(time()-t0, 3), "s")

t1 = time()
pred = clf.predict(features_test)
print("Testing time:", round(time()-t1, 3), "s")
"""

from sklearn.svm import SVC
clf = SVC(kernel="rbf",C=10000,gamma=0.6)
t0 = time()
clf.fit(features_train,labels_train)
print("Training time:", round(time()-t0, 3), "s")

t1 = time()
pred = clf.predict(features_test)
print("Testing time:", round(time()-t1, 3), "s")

from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test,pred)

print("Accuracy is ",acc)

### ACCURACY for Random Forest Classifier with all default values is ->

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
