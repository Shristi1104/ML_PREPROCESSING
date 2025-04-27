Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np 
... import pandas as pd 
... from sklearn.model_selection import train_test_split
... dataset = pd.read_csv('iris.csv')
... X=dataset.iloc[:, :-1].values
... y=dataset.iloc[:, -1].values
... print(X)
