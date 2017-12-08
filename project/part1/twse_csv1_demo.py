import requests
import json
import pandas as pd
from time import sleep

err_count = 0
while err_count < 3:
    try:
        #小心requrest太過頻繁IP會被對方封鎖
        res1 = requests.get('http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20170901&stockNo=2330')
        sleep(5)
        res2 = requests.get('http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20171001&stockNo=2330')
        sleep(5)
        res3 = requests.get('http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20171101&stockNo=2330')
        break
    except:
        sleep(5)
        err_count += 1
        continue
if err_count == 3:
    print('連線失敗')

json1 = res1.json()
json2 = res2.json()
json3 = res3.json()

header = json1['fields']

data = json1['data']
data.extend(json2['data'])
data.extend(json3['data'])


df = pd.DataFrame.from_records(data, columns=header)
df.sort_index(ascending=False).head()

for i, row in df.iterrows():
    #print(row[0])
    strDate = row[0]
    DateArr = strDate.split("/")
    DateArr[0] = str(int(DateArr[0])+1911)
    DateArr[1] = str(int(DateArr[1]))
    DateArr[2] = str(int(DateArr[2]))
    #df.set_value(i,'日期','/'.join(DateArr))
    df.loc[i, '日期'] = '/'.join(DateArr)
df.sort_index(ascending=False).head()

df.to_csv('../data/fp_demo.csv', sep=',', encoding='utf-8-sig', index=False)



import sqlite3 as sql

#連線至sqlite檔案，若無該檔案sql，則會建立一個新的
conn = sql.connect("../data/twse.db")
#將Dataframe資料寫入sql檔中的'demo1'表中，無該資料表則會自動建立
df.to_sql("demo1", conn, if_exists="replace", index=False)

pd.read_sql_query("select * from demo1;", conn).sort_index(ascending=False)
