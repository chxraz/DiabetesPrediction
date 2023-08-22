# -*- coding: utf-8 -*-
"""diabetes prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1emMGv2EsPHXJgyI55vuar5unZBAJfMQ8
"""

# importing Important Liberaries
import pandas as pd
import numpy as np
import seaborn as sns

# Loading data
from google.colab import drive

drive.mount('/content/gdrive')
data = pd.read_csv('gdrive//My Drive/PMSI 6B Kel 2 P2/diabetes.csv')
data

# Shape check
data.shape

# Check info data
data.info()

# Statistics Summary
data.describe()

# Check Missing Values
data.isna().sum()

# Correlation Matrix
sns.heatmap(data.corr(),annot = True, cmap = 'crest')

# Visualizations
sns.pairplot(data, hue="Outcome", palette="viridis");

"""# Modeling"""

features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age']
x = pd.get_dummies(data[features])

# Target
y = data['Outcome']

# Split data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 1/11, random_state = 242)

# Fitting model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression


model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

data_input = (6,148,72,35,0,33.6,0.627,50)
data_input_array = np.array(data_input)
data_input_reshape = data_input_array.reshape(1, -1)

prediction = model.predict(data_input_reshape)
print(prediction)

if(prediction[0] == 0):
  print('Pasien tidak terkena diabetes')
else:
  print('Pasien terkena diabetes')

import pickle
filename = 'model_diabetes.sav'
pickle.dump(model, open(filename, 'wb'))