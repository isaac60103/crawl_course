from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

import math
import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql

#定義準備train data方法
def regData(x):
    #格式化數字
    for i, row in x.iterrows():
        x.loc[i, '成交股數'] = row['成交股數'].replace(',', '')
        x.loc[i, '成交筆數'] = row['成交筆數'].replace(',', '')
    #做normalization(第i天資料/i-1天資料)
    for i, row in X.iterrows():
        if i <= len(X)-2:
            x.loc[i, '成交股數'] = int(x.loc[i+1, '成交股數'])/int(x.loc[i, '成交股數'])
            x.loc[i, '成交筆數'] = int(x.loc[i+1, '成交筆數'])/int(x.loc[i, '成交筆數'])
            x.loc[i, '美元／新台幣'] = x.loc[i+1, '美元／新台幣']/x.loc[i, '美元／新台幣']
    return x.head(30) #不取最後一筆

#定義LinearRegression對應data
def linReg(y):
    y.drop(0, axis=0, inplace=True)
    y = y.reset_index(drop=True)
    return y

#定義LogisticRegression對應data
def logReg(y):
    #將價差=0定義為 1 (漲), 價差<=0定義為 0 (跌)
    y.drop(0, axis=0, inplace=True)
    y = y.reset_index(drop=True)
    for i, row in y.iterrows():
        if y.loc[i, '漲跌價差'] == 0:
            y.loc[i, '漲跌價差'] = 1
        else:
            y.loc[i, '漲跌價差'] = 0
    return y['漲跌價差']

#讀取資料
#從CSV讀取
df = pd.read_csv('fp_demo3.csv')

#從sqLite讀取
#conn = sql.connect("twse.db")
#df = pd.read_sql_query("select * from demo3;", conn)
    
#取得必要欄位，以前30筆作為training data
X = df[['成交股數', '成交筆數', '美元／新台幣']].head(31)
X = regData(X)

#y = linReg(df[['收盤價']].head(31)) #LinearRegression
y = logReg(df[['漲跌價差']].head(31)) #LogisticRegression

#分割資料
# Split X and y into X_
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=1)

#建立LinearRegression模型
#regression_model = LinearRegression() #LinearRegression
regression_model = LogisticRegression() #LogisticRegression
regression_model.fit(X_train, y_train)

#各data係數
for idx, col_name in enumerate(X_train.columns):
    print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0][idx]))

#截距
intercept = regression_model.intercept_[0]

print("The intercept for our model is {}".format(intercept))

#用training data算準確率
predictions = regression_model.predict(X_train)
regression_model.score(X_train, y_train) #資料零散程度大且資料量不夠可能造成準確率較低

#用testing data計算平方誤差
y_predict = regression_model.predict(X_test)
regression_model_mse = mean_squared_error(y_predict, y_test)
regression_model_mse

#將誤差開平方根
math.sqrt(regression_model_mse)

#使用未引入data做測試(取任兩相鄰資料做normalize)
t1 = df.loc[df['日期'] == '2017/10/17'][['成交股數', '成交筆數', '美元／新台幣']]
t2 = df.loc[df['日期'] == '2017/10/16'][['成交股數', '成交筆數', '美元／新台幣']]

#重設資料index
t1.reset_index(drop=True,inplace=True)
t2.reset_index(drop=True,inplace=True)

#格式化資料
t1.loc[0, '成交股數'] = int(t1.loc[0, '成交股數'].replace(',', ''))/int(t2.loc[0, '成交股數'].replace(',', ''))
t1.loc[0, '成交筆數'] = int(t1.loc[0, '成交筆數'].replace(',', ''))/int(t2.loc[0, '成交筆數'].replace(',', ''))
t1.loc[0, '美元／新台幣'] = float(t1.loc[0, '美元／新台幣'])/float(t2.loc[0, '美元／新台幣'])

#預測結果
int(regression_model.predict([t1.loc[0].tolist()]))
