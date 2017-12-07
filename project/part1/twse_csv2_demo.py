# coding: utf-8
import requests as req
import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql

payload = {'download':'','hdn_gostartdate':'2017/09/1','hdn_goenddate':'2017/10/31','syear':'2017','smonth':'09','sday':'1','eyear':'2017','emonth':'10','eday':'31','datestart':'2017/09/1','dateend':'2017/10/31'}
html = req.post('http://www.taifex.com.tw/chinese/3/3_5.asp', data=payload)
#注意網頁編碼
html.encoding = 'utf-8'
df = pd.read_html(html.text)
df = df[2]
df.columns = df.iloc[0]
df = df.reindex(df.index.drop(0))

#存成CSV
df.to_csv('../data/fp_demo2.csv', sep=',', encoding='utf-8-sig', index=False)


#存入SqLite
#連線至sqlite檔案，若無該檔案sql，則會建立一個新的
#conn = sql.connect("../data/twse.db")
#將Dataframe資料寫入sql檔中的'demo2'表中，無該資料表則會自動建立
#df.to_sql("demo2", conn, if_exists="replace")

print('Done!')