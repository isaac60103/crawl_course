# coding: utf-8
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

import math
import numpy as np
import pandas as pd

df = pd.read_csv('auto-mpg.csv')

df = df.drop('name', axis=1)

df['origin'] = df['origin'].replace({1: 'america', 2: 'europe', 3: 'asia'})

df = pd.get_dummies(df, columns=['origin'])

df = df.replace('?', np.nan)
df = df.dropna()

X = df.drop('mpg', axis=1)
y = df[['mpg']]

# Split X and y into X_
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

for idx, col_name in enumerate(X_train.columns):
    print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0][idx]))

intercept = regression_model.intercept_[0]

print("The intercept for our model is {}".format(intercept))

regression_model.score(X_test, y_test)

y_predict = regression_model.predict(X_test)

regression_model_mse = mean_squared_error(y_predict, y_test)

regression_model_mse

math.sqrt(regression_model_mse)

result = regression_model.predict([[4, 121, 110, 2800, 15.4, 81, 0, 1, 0]])

print(result)

