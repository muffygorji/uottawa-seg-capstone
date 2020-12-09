"""
program: svm.py
author: Tyler Tsang
created: 2-12-2020

description: This program was created based on an online tutorial:
https://www.datacamp.com/community/tutorials/svm-classification-scikit-learn-python#algorithm
to learn about random forest classifiers in python

"""

# Import scikit-learn dataset library
from sklearn import datasets

# Import train_test_split function
from sklearn.model_selection import train_test_split

# Import svm model
from sklearn import svm

# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Load dataset
cancer = datasets.load_breast_cancer()

# Print the names of the 13 features
#print("Features: ", cancer.feature_names)

# Print the label type of cancer('malignant' 'benign')
#print("Labels: ", cancer.target_names)

# Print data(feature) shape
#cancer.data.shape

# Print the cancer data feature (top 5 records)
#print(cancer.data[0:5])

# Print the cancer labels (0:malignant, 1:benign)
print(cancer.target)

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3, random_state=109) # 70% training 30% test

# Create a svm Classifier
# Other types of kernel: Linear, Polynomial, Radial Basis Function
clf = svm.SVC(kernel='linear') # Linear Kernal

# Train the model using the training sets
clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy: how often is the calssifier correct?
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Model Precision: what percentage of positive tuples are labelled as such?
print("Precision:", metrics.precision_score(y_test, y_pred))

# Model Recall: what percentage of positive tuples are labelled as such?
print("Recall:", metrics.recall_score(y_test, y_pred))





