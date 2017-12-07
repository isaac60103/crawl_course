import requests as req
import pandas as pd

html = req.get('https://isaac60103.github.io/crawl_course/static_page/taifex.html')
#注意網頁編碼
html.encoding = 'utf-8'
df = pd.read_html(html.text)
df = df[2]
df.columns = df.iloc[0]
df = df.reindex(df.index.drop(0))

#輸出HTML
df.to_html('taifex_out.html')

#查看剛剛轉存的Html
df2 = pd.read_html('taifex_out.html', encoding='utf-8')
df2

