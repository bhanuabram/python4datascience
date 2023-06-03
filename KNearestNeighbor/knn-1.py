# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 18:09:49 2023

@author: 902544749
"""

# Predict whether someone will be inside that target class or not
# using K Nearest Neighbor Classifier

# Please place the input file in the same folder with this python
# file.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Read the input text file as a Dataframe
df = pd.read_csv('Classified Data')

# Standardize variables
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS',
                   axis = 1))
scaled_features = scaler.transform(df.drop('TARGET CLASS',
                                           axis = 1))

df_feat = pd.DataFrame(scaled_features,
                       columns = df.columns[:-1])

# Create train test split
X = df_feat
y = df['TARGET CLASS']
X_train, x_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size = 0.3,
                                                    random_state = 101)

# Call this function to generate Confusion Matrix and Classification
# Report on prediction.
def knn_classifier(n, x1, x2, y1, y2):
    knn = KNeighborsClassifier(n_neighbors = n)
    knn.fit(x1, y1)
    pred = knn.predict(x2)
    print(confusion_matrix(y2, pred))
    print(classification_report(y2, pred))

# Choose the best K Value with the lowest error rate
error_rate = []

for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train, y_train)
    pred_i= knn.predict(x_test)
    error_rate.append(np.mean(pred_i != y_test))

min_k = error_rate.index(min(error_rate))
print('Best K-Value is:', min_k)
print('\n')
knn_classifier(min_k, X_train, x_test, y_train, y_test)
