#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 1 (Naive Bayes) mini-project 

    use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1

"""
    
import sys
impoty numpy as np
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
#clf = GaussianNB()
#clf.fit(features_test,features_train);
#GaussianNB()
#print clf.predict([-0.8,-1])

def Accuracy(features_train,labels_train,features_test,labels_test):

    clf = GaussianNB()

    clf.fit(features_train,labels_train)

    pred = clf.predict(features_test)

    return clf.score(features_test,labels_test)    
#########################################################


