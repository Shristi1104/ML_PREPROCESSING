Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd 
... import numpy as np 
... from sklearn.compose import ColumnTransformer
... from sklearn.preprocessing import OneHotEncoder
... from sklearn.preprocessing import LabelEncoder
... 
... dataset=pd.read_csv('titanic.csv')
... categorical_features = ['Sex','Embarked','Pclass']
... 
... ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),categorical_features)], remainder='passthrough')
... X = ct.fit_transform(dataset)
... X=np.array(X)
... le=LabelEncoder()
... y = le.fit_transform(dataset['Survived'])
... print("Updated matrix of features: \n", X)
