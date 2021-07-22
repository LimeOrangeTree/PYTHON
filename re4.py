import re
import requests
url="https://comic.naver.com/webtoon/list.nhn?titleId=682637&weekday=tue"
f=open("data\webtoon.csv","w")   #w쓰기모드
# f=open("data\webtoon.csv","w",encoding="utf-8")   #w쓰기모드
result=requests.get(url)
print(result)
items=re.findall\
(r'<td class="title">.+?<a href=".+?">(.+?)</a>.+?<strong>(.+?)</strong>.+?<td class="num">(.+?)</td>',
 result.text,re.DOTALL)
for i in items:    #i=items[0],items[1],
    s="{},{},{}\n".format(i[0],i[1],i[2])
    f.write(s)
    # print(s)


# re5.py
#이미지경로,제목,점수,날짜











