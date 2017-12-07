#此dataset為鐵達尼號生還者之資訊，用'Sex','Pclass','Age' 三個變數預測'Survived'(存活率)
import pandas as pd
import numpy as np
from sklearn import preprocessing, linear_model

#讀取資料
titanic_train = pd.read_csv('kaggle_titanic_train.csv')
df=titanic_train[['Sex','Pclass','Age','Survived']]  #用'Sex','Pclass','Age' 三個變數預測'Survived'(存活率)


# 創造 dummy variables   將SEX轉換成 0，1
pd.options.mode.chained_assignment = None
df.loc[df["Sex"] == "male", "Sex"] = 0
df.loc[df["Sex"] == "female", "Sex"] = 1

#Age無資料以median填補
df['Age'] = df['Age'].fillna(df['Age'].median())

#切分訓練 測試資料
from sklearn.model_selection import train_test_split

x=df[['Sex','Pclass','Age']]
y=df[['Survived']]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=20170816) #random_state 種子值


#標準化 :為了避免偏向某個變數去做訓練
from sklearn.preprocessing  import StandardScaler
sc=StandardScaler()

sc.fit(x_train)

x_train_nor=sc.transform(x_train)
x_test_nor=sc.transform(x_test)


#訓練資料分類效果(3個參數)
from sklearn.linear_model  import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train_nor,y_train)

# 印出係數
print(lr.coef_)
# 印出截距
print(lr.intercept_ )

# 計算準確率
survived_predictions = lr.predict(x_test_nor)
#印出以testing data預測之結果
print(survived_predictions)
accuracy = lr.score(x_test_nor, y_test)
#準確率
print(accuracy)

