#!/usr/bin/python3

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

### make sure you use // when dividing for integer division


#########################################################
### your code goes here ###
from sklearn.svm import SVC
clf = SVC(kernel="rbf",C=10000)
t0 = time()
clf.fit(features_train,labels_train)
print("Training time:", round(time()-t0, 3), "s")

t1 = time()
pred = clf.predict(features_test)
print("Testing time:", round(time()-t1, 3), "s")

from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test,pred)
print("Accuracy is ",acc) 

#Counting the number of Chris labels in prediction
from collections import Counter
print("Number of Chris prediction in the result is ",Counter(pred)[1])
#########################################################

## ACCURACY when kernel= linear and C = default i.e. 1 --> 98.4%
## ACCURACY when kernel= rbf and C=10000 --> 99.08%