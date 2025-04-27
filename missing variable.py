Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np 
... import pandas as pd 
... from sklearn.impute import SimpleImputer
... dataset = pd.read_csv('pima-indians-diabetes.csv')
... missing_data = dataset.isnull().sum()
... print("Missing data: \n", missing_data)
... imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
... imputer.fit(dataset)
... dataset_imputed = imputer.transform(dataset)
... print("Updated matrix of features: \n", dataset_imputed)
