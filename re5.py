import re
import requests
url="https://comic.naver.com/webtoon/list.nhn?titleId=682637&weekday=tue"
f=open("data\webtoon.csv","w",encoding="utf-8")   #w쓰기모드
result=requests.get(url)
print(result)
items=re.findall\
(r'<td>.+?<a href="/webtoon/.+?<img src="(.+?)" title="(.+?)" alt=".+?<strong>(.+?)</strong>.+?<td class="num">(.+?)</td>',
 result.text,re.DOTALL)
# print(len(items))
# print(items)
for i in items:    #i=items[0],items[1],
    s="{},{},{},{}\n".format(i[0],i[1],i[2],i[3])
    f.write(s)












