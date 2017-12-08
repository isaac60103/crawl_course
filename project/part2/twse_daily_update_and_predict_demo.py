import requests
import datetime
import pandas as pd

#取得當天日期
today = datetime.date.today().strftime("%Y%m%d")
today2 = datetime.date.today().strftime("%Y/%m/%d")
today_y = today2.split('/')[0]
today_m = today2.split('/')[1]
today_d = today2.split('/')[2]
today3 = '/'.join([today_y, today_m.lstrip('0'), today_d.lstrip('0')])
#準備URL
url1 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=%s&stockNo=2330' % today
url2 = 'http://www.taifex.com.tw/chinese/3/3_5.asp'
payload = {'download':'','hdn_gostartdate':today3,'hdn_goenddate':today3,'syear':today_y,'smonth':today_m,'sday':today_d,'eyear':today_y,'emonth':today_m,'eday':today_d,'datestart':today2,'dateend':today2}

#取得資料
err_count = 0
while err_count < 3:
    try:
        res1 = requests.get(url1)
        res2 = requests.post(url2, data=payload)
        #注意編碼
        res2.encoding = 'utf-8'
        break
    except:
        sleep(5)
        err_count += 1
        continue
if err_count == 3:
    print('連線失敗')

#準備TWSE資料
json = res1.json()
header = json['fields']
data = json['data']
#取最新一筆資料
df1 = pd.DataFrame.from_records(data, columns=header).sort_index(ascending=False).head(1).reset_index(drop=True)
#修正日期格式
df1.iloc[0]['日期'] = today3

#準備匯率資料
df2 = pd.read_html(res2.text)
df2 = df2[2]
df2.columns = df2.iloc[0]
df2 = df2.drop(0).reset_index(drop=True).sort_index(ascending=False).head(1)

#合併DF
df3 = pd.merge(df1, df2, on='日期')


#更新資料至
#讀取CSV
#df4 = pd.read_csv('../data/fp_demo3.csv')

#讀取SqLite
import pandas.io.sql as pd_sql
import sqlite3 as sql
conn = sql.connect("../data/twse.db")
df4 = pd.read_sql_query("select * from demo3;", conn)

#檢查日期是否重複
if not ((df4['日期'] == today3)).any():
    df4 = df4.append(df3, ignore_index=True)
    #df4.to_csv('../data/fp_demo3.csv', sep=',', encoding='utf-8-sig', index=False) #回存CSV
    df4.to_sql("demo3", conn, if_exists="replace", index=False) #回存SqLite
df4.sort_index(ascending=False).head()

#定義nomalize方法
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
            x.loc[i, '美元／新台幣'] = float(x.loc[i+1, '美元／新台幣'])/float(x.loc[i, '美元／新台幣'])
    return x
#對預測資料做nomalize
X = df4[['成交股數', '成交筆數', '美元／新台幣']]
X = regData(X.sort_index(ascending=False))
X = X.sort_index(ascending=True)
X.columns = ['成交股數[Normalize]', '成交筆數[Normalize]', '美元／新台幣[Normalize]']
df4 = pd.concat([df4, X.shift()], axis=1)

#開始執行預測
#準備預測資料(今日nomalized資料)
df5 = df4.sort_index(ascending=False).head(2).reset_index(drop=True)
pred1 = float(df5.loc[0, '成交股數[Normalize]'])
pred2 = float(df5.loc[0, '成交筆數[Normalize]'])
pred3 = float(df5.loc[0, '美元／新台幣[Normalize]'])

#使用訓練好的Model預測
import pickle
#with open('../data/lin_r_model.pickle', 'rb') as f: #LinearRegression
with open('../data/log_r_model.pickle', 'rb') as f: #LogisticRegression
    regression_model = pickle.load(f)
    pred_result = regression_model.predict([[pred1, pred2, pred3]])
    print('預測結果: %f' % pred_result)


#建立結果網頁
from datetime import timedelta

#計算明天日期
tomorrow = (datetime.date.today() + timedelta(days=1)).strftime("%Y/%m/%d")
tomorrow_y = tomorrow.split('/')[0]
tomorrow_m = tomorrow.split('/')[1]
tomorrow_d = tomorrow.split('/')[2]
today5 = '/'.join([tomorrow_y, tomorrow_m.lstrip('0'), tomorrow_d.lstrip('0')])
#建立預測欄位(非預測欄位填入空值)
#pred_col = [today5, '', '', '', '', '', float(pred_result), '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''] #LinearRegression
pred_col = [today5, '', '', '', '', '', '', int(pred_result), '', '', '', '', '', '', '', '', '', '', '', '', '', ''] #LogisticRegression
pred_col = pd.DataFrame(pred_col).T
pred_col.columns = list(df5.columns)

#將預測欄位加入更新過的DF
df6 = df4.append(pred_col, ignore_index=True)

#輸出結果HTML(避免資料過於龐大，只取前30筆作顯示)
#df6.sort_index(ascending=False).head(30).to_html('../data/lin_daily_result.html', index=False) #LinearRegression
df6.sort_index(ascending=False).head(30).to_html('../data/log_daily_result.html', index=False) #LogisticRegression

