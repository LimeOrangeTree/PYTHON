import re
import requests

# page 적용하여 실행하세요
url="https://comic.naver.com/webtoon/list.nhn?titleId=682637&weekday=tue"
f=open("data\webtoon.csv","w",encoding="utf-8")   #w쓰기모드
result=requests.get(url)
items=re.findall\
(r'<td>.+?<a href="/webtoon/.+?<img src="(.+?)" title="(.+?)" alt=".+?<strong>(.+?)</strong>.+?<td class="num">(.+?)</td>', result.text,re.DOTALL)
for i in items:
    s="{} ,{},{},{}\n".format(i[0],i[1],i[2],i[3])
    f.write(s)












