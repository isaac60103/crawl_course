#讀取資料
import pandas as pd

df = pd.read_csv('house.csv')

print(df.head())

#標準化 :為了避免偏向某個變數去做訓練
df = (df - df.mean()) / df.std()  

#分割資料
X = df.drop('price', axis=1)
y = df[['price']]

from sklearn.model_selection import train_test_split

# Split X and y into X_
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)


#代入模型training
from sklearn.linear_model import LinearRegression

regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

#印出各系數
for idx, col_name in enumerate(X_train.columns):
    print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0][idx]))

#截距
intercept = regression_model.intercept_[0]

print("The intercept for our model is {}".format(intercept))

#將測試資料代入得準確率
regression_model.score(X_test, y_test)

