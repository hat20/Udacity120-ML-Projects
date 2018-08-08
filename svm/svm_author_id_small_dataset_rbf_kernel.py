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

features_train = features_train[:len(features_train)//100]
labels_train = labels_train[:len(labels_train)//100]

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
print("Answer to the 10th,26th and 50th element is {}, {} and {} respectively".format(pred[10],pred[26],pred[50]))
#########################################################
## ACCURACY - 61.60%
## Now, changing the value of C in factors of 10
## ACCURACY for C =10 -> 61.60%
## ACCURACY for C =100 -> 61.60%
## ACCURACY for C =1000 -> 82.13%
## ACCURACY for C =10000 -> 89.24%
## ACCURACY for C =100000 -> 86.006%
## ACCURACY for C =50000 -> 86.006%
