# coding: utf-8
import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql

#從CSV載入資料
df1 = pd.read_csv('fp_demo.csv')
df2 = pd.read_csv('fp_demo2.csv')

#從SqLite載入資料
#conn = sql.connect("../data/twse.db")
#df1 = pd.read_sql_query("select * from demo1;", conn)
#df2 = pd.read_sql_query("select * from demo2;", conn)

#以'日期'為index合併Dataframe
result = pd.merge(df1, df2, on='日期')

#存入CSV
result.to_csv('../data/fp_demo3.csv', sep=',', encoding='utf-8-sig', index=False)

#存入SqLite
#result.to_sql("demo3", conn, if_exists="replace")

print('Done!')

