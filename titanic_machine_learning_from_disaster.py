# -*- coding: utf-8 -*-
"""Titanic_Machine Learning from Disaster.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aGlZDc1mDkbsipM_sdrOuLr4_eb-85ij
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
 import numpy as np
 import matplotlib.pyplot as pyplot
 import seaborn as sns
 from sklearn.preprocessing import StandardScaler, MinMaxScaler, OrdinalEncoder
 from sklearn.compose import make_column_transformer

data_train = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Data/train.csv")
data_test = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Data/test.csv")

data_train = data_train.drop(['Name','Ticket','Cabin','Embarked'],axis=1)
data_test = data_test.drop(['Name','Ticket','Cabin','Embarked'],axis=1)

data_train['Age'] = data_train['Age'].fillna(data_train['Age'].mean())
gender_labels = {'male':0, 'female':1}
data_train['Sex'] = data_train['Sex'].replace({'male':0, 'female':1})

data_test['Age'] = data_test['Age'].fillna(data_test['Age'].mean())
data_test['Fare'] = data_test['Fare'].fillna(data_test['Fare'].mean())
gender_labels = {'male':0, 'female':1}
data_test['Sex'] = data_test['Sex'].replace({'male':0, 'female':1})

x_train = data_train.drop(['Survived'],axis=1)
y_train = data_train['Survived']
x_test = data_test

num_columns = list(x_test.columns)

# make_column_transformer: 더미변수 치환기, 클래스 이름을 기반으로 각 단계에 이름을 자동부여
# MinMaxScaler: 모든 특성이 0과 1사이에 위치하도록 데이터 변경
# StandardScaler: 각 특성의 평균을 0, 분산을 1로 변경
# remainder: drop(변환한 열을 제외한 모든 열을 삭제), passthrough
ct = make_column_transformer(
    (MinMaxScaler(), num_columns),
    (StandardScaler(), num_columns),  
    remainder = 'passthrough'
)

x_train = ct.fit_transform(x_train)
x_test = ct.fit_transform(x_test)

from sklearn.linear_model import LogisticRegression

# solver: 최적화에 사용할 알고리즘 결정
log_reg = LogisticRegression(solver='liblinear')

log_reg.fit(x_train, y_train)
y_test = log_reg.predict(x_test)

y_test

ids = data_test['PassengerId'].tolist()

preds = list(y_test)

submission = {
    "PassengerID":[],
    "Survived": []
}

from tqdm import tqdm

for id, pred in zip(tqdm(ids),preds):
  submission['PassengerID'].append(id)
  submission['Survived'].append(pred)

submission = pd.DataFrame(submission)

submission.iloc[:10]

submission.to_csv("/content/drive/MyDrive/Colab Notebooks/Data/Final.csv",index=False)