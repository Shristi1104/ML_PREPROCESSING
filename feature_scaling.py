Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd 
... from sklearn.model_selection import train_test_split
... from sklearn.preprocessing import StandardScaler  
... 
... dataset = pd.read_csv('winequality-red.csv', delimiter=';')
... X = dataset.drop('quality', axis=1)
... y = dataset['quality']
... 
... X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
... sc = StandardScaler()
... X_train = sc.fit_transform(X_train)
... X_test = sc.transform(X_test)
... 
... print("Scaled training set:\n", X_train)
