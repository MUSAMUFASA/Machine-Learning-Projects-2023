# -*- coding: utf-8 -*-
"""Breast Cancer Wisnconsin (Diagnostic) Data Set [Kawu Musa "Mufasa", 07.07.2023].ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Uu9FiF7NiPwLqekoVnTZ-fVo8KYZkDny

# Machine Learning Project - Breast Cancer Wisconsin (Diagnostic) Data Set [By Mufasa; (Currently Learning from Udemy)]

Link: https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data

#Part 1 - Data Pre-processing

## Step 1 - Importing Libraries and Dataset
"""

import numpy as np
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt

#reading csv file using pandas and saving into a variable called 'data'
data = pd.read_csv('/content/data.csv')

#previewing the top 5 rows in the dataset
data.head()

"""## Step 2 - Data Exploration"""

#Finding out the number of rows and columns in the dataset
data.shape

#Obtaining basic information about the dataset
data.info()

#Finding the column that has categorical (Non-numerical) data.
data.select_dtypes(include='object').columns

#Finding the number of column(s) that have/has categorical (Non-numerical) data.
len(data.select_dtypes(include='object').columns)

#Finding the column(s) that have / has numerical data.
data.select_dtypes(include=['float64','int64']).columns

#Finding the number of column(s) that have / has numerical data.
len(data.select_dtypes(include=['float64','int64']).columns)

#Summarising statistical information about the columns in the dataset.
data.describe()

"""## Step 3 - Dealing with the missing values"""

#Are there null values in the dataset?
data.isnull().values.any()

#The number of null values in the dataset?
data.isnull().values.sum()

#What column has the null values?
data.columns[data.isnull().any()]

#The number of columns with null values.
len(data.columns[data.isnull().any()])

data['Unnamed: 32'].count()

#drop the column with the null values
data = data.drop(columns='Unnamed: 32')

#Find the shape after dropping that column
data.shape

#are there any more null values in the data
data.isnull().values.any()

"""## Step 4 - Dealing with categorical data"""

#Identify the column with categorical data
data.select_dtypes(include='object').columns

#Identify unique values in the 'diagnosis' column
data['diagnosis'].unique()

#The number of unique values in the 'diagnosis' column
data['diagnosis'].nunique()

#Encode categorical data as 0 and 1
#One hot encoding
data = pd.get_dummies(data=data,drop_first=True)

#Show the top 5 rows
data.head()

"""##Step 5 - Correlation Matrix and Heatmap"""

#Dropping the column 'Diagnosis_M' from the entire dataset
dataset_min_diagnosis = data.drop(columns='diagnosis_M')

#Plotting a bar plot showing how other columns correlate with the column, Diagnosis_M.
dataset_min_diagnosis.corrwith(data['diagnosis_M']).plot.bar(figsize = (20,10), title = "Correlation with diagnosis_M",rot=45, grid = True)

"""###Step 5a - Correlation Matrix"""

#Developing a correlation matrix
correlation = data.corr()

correlation

"""###Step 5b - Heat Map"""

#Plotting a heatmap using the correlation matrix above
plt.figure(figsize=(20,10))
sbn.heatmap(correlation,annot=True)

"""## Step 6 - Splitting the Dataset into Training set and Test set"""

data.head()

#Developing a matrix containing all independent variables and saving it as 'x'
x = data.iloc[:,1:-1].values

#Obtaining the shape of x
x.shape

##Developing a single-column-matrix containing the dependent variable and saving it as 'y'
y = data.iloc[:,-1].values

#Obtaining the shape of y
y.shape

#Importing train_test_split to split the dataset into random train and test subsets.[Testset is to be 25% of all data]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25,random_state = 0)

#The training set of the independent variables is confirmed to be 426 rows and 30 columns.

x_train.shape

#The test set of independent variables is confirmed to be 143 rows and 30 columns.
x_test.shape

#The training set of the dependent variable is confirmed to be 426 rows and 1 column.
y_train.shape

#The training set of the dependent variable is confirmed to be 143 rows and 1 column.
y_test.shape

"""##Step 7 - Feature Scaling"""

#Importing standard scaling to scale independent features.
from sklearn.preprocessing import StandardScaler

#Creating an instance of StandardScaler()

standard_scale = StandardScaler()

#Performing feature scaling on training and test datasets of independent variables. Using mean and standard deviation for training set, but not for test set.
x_train = standard_scale.fit_transform(x_train)
x_test = standard_scale.transform(x_test)

x_train

x_test

"""#Part 2 - Building the Model

## 1) Logistic Regression
"""

#Importing LogisticRegression Class

from sklearn.linear_model import LogisticRegression

#Creating an instance of LogisticRegression Class and then training the model

classifier_lr = LogisticRegression(random_state=0)
classifier_lr.fit(x_train, y_train)

#Generating predicted values and storing in variable pred_y
pred_y  = classifier_lr.predict(x_test)

#Importing accuracy, confusion matrix, f1 score, precision score and recall score functions for susbequent use.
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score

accuracy = accuracy_score(y_test,pred_y )
f1_score = f1_score(y_test,pred_y )
precision = precision_score(y_test,pred_y )
recall_score = recall_score(y_test,pred_y )

# Summarising metrics results

metric_results = pd.DataFrame([['Logistic Regression',accuracy,f1_score,precision,recall_score]],columns=['Model','Accuracy','F1 Score','Precision','Recall'])
metric_results

# Obtaining confusion matrix

cm = confusion_matrix(y_test,pred_y)
print(cm)

"""### 1a - Cross Validation"""

#Importing cross_val_score for cross validation
from sklearn.model_selection import cross_val_score

#Computing for the mean and standard deviation for accuracies of 20 random selections
accuracies = cross_val_score(estimator=classifier_lr,X=x_train,y=y_train,cv=20)
print("Accuracy is {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation is {:.2f} %".format(accuracies.std()*100))

"""## 2) Random Classifier"""

#Importing RandomClassifer Class

from sklearn.ensemble import RandomForestClassifier

#Creating an instance of the RandomForestClassifer Class and then training the model

classifier_rf = RandomForestClassifier(random_state=0)
classifier_rf.fit(x_train, y_train)

#Generating predicted values and storing in variable pred_y
pred_y_rf  = classifier_rf.predict(x_test)

#Importing accuracy, confusion matrix, f1 score, precision score and recall score functions for susbequent use.
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score

accuracy_rf = accuracy_score(y_test,pred_y_rf)
f1_score_rf = f1_score(y_test,pred_y_rf)
precision_rf = precision_score(y_test,pred_y_rf)
recall_score_rf = recall_score(y_test,pred_y_rf)

# Summarising metrics results

metric_results_rf = pd.DataFrame([['Random Forest Classifier',accuracy_rf,f1_score_rf,precision_rf,recall_score_rf]],columns=['Model','Accuracy','F1 Score','Precision','Recall'])
metric_results_rf

comb_results = metric_results.append(metric_results_rf,ignore_index = True)
comb_results

# Obtaining confusion matrix

cm_rf = confusion_matrix(y_test,pred_y_rf)
print(cm_rf)

"""### 2a - Cross Validation"""

#Importing cross_val_score for cross validation
from sklearn.model_selection import cross_val_score

#Computing for the mean and standard deviation for accuracies of 20 random selections
accuracies_rf = cross_val_score(estimator=classifier_rf,X=x_train,y=y_train,cv=20)
print("Accuracy is {:.2f} %".format(accuracies_rf.mean()*100))
print("Standard Deviation is {:.2f} %".format(accuracies_rf.std()*100))