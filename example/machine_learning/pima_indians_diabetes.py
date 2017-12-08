#此dataset為Pima印第安人5年內糖尿病的發病情況，這邊我們取病人的懷孕情況(pregnant)、體內胰島素含量(insulin)、
#BMI值(bmi)、年齡(age)，來判斷是否發病(label)
import pandas as pd
import numpy as np
from sklearn import preprocessing, linear_model

#讀取資料
pima = pd.read_csv('pima-indians-diabetes.csv')
#用'pregnant','insulin','bmi', 'age' 三個變數預測'label'(是否發病)
df=pima[['pregnant', 'insulin', 'bmi', 'age', 'label']]

#切分訓練 測試資料
from sklearn.model_selection import train_test_split

x=df[['pregnant', 'insulin', 'bmi', 'age']]
y=df[['label']]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1) #random_state 種子值


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
#印出準確率
print(accuracy)


