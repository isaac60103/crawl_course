#讀取資料
import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql

#從CSV讀取
df = pd.read_csv('../data/fp_demo3.csv')

#從sqLite讀取
#conn = sql.connect("../data/twse.db")
#df = pd.read_sql_query("select * from demo3;", conn)

df.sort_index(ascending=False).head()

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
    return x.head(60) #不取最後一筆

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
        if y.loc[i, '漲跌價差'] >= 0:
            y.loc[i, '漲跌價差'] = 1
        else:
            y.loc[i, '漲跌價差'] = 0
    return y['漲跌價差']
    
#取得必要欄位，以前40筆作為training data
X = df[['成交股數', '成交筆數', '美元／新台幣']].head(61)
X = regData(X)

y = linReg(df[['收盤價']].head(61)) #LinearRegression
#y = logReg(df[['漲跌價差']].head(61)) #LogisticRegression

#分割資料
from sklearn.model_selection import train_test_split

# Split X and y into X_
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

#建立LinearRegression模型
from sklearn.linear_model import LinearRegression, LogisticRegression

regression_model = LinearRegression() #LinearRegression
#regression_model = LogisticRegression() #LogisticRegression
regression_model.fit(X_train, y_train)

#各data係數
for idx, col_name in enumerate(X_train.columns):
    print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0][idx]))


#截距
intercept = regression_model.intercept_[0]

print("The intercept for our model is {}".format(intercept))

#使用testing data準確率
predictions = regression_model.predict(X_test)
#印出testing data之預測結果
print(predictions)
#準確率
regression_model.score(X_test, y_test)

import pickle

#保存訓練好的Model
with open('../data/lin_r_model.pickle', 'wb') as f: #LinearRegression
#with open('../data/log_r_model.pickle', 'wb') as f: #LogisticRegression
    pickle.dump(regression_model, f)

