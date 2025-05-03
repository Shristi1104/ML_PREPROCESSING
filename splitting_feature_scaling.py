Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sklearn.model_selection import train_test_split  
... from sklearn.preprocessing import StandardScaler
... import pandas as pd  
... 
... dataset = pd.read_csv('iris.csv')
... X = dataset.drop('target', axis=1)
... y = dataset['target']
... X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
... 
... sc = StandardScaler()
... X_train = sc.fit_transform(X_train)
... X_test = sc.transform(X_test)
... print("Scaled Training Set:")
... print(X_train)
... print("\nScaled Test Set:")
