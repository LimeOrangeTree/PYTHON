import re
import requests
url="https://comic.naver.com/webtoon/list.nhn?titleId=682637&weekday=tue"
f=open("data\webtoon.csv","w",encoding="utf-8")   #w쓰기모드
result=requests.get(url)
items=re.findall\
(r'<td>.+?<a href="/webtoon/.+?<img src="(.+?)" title="(.+?)" alt=".+?<strong>(.+?)</strong>.+?<td class="num">(.+?)</td>', result.text,re.DOTALL)
for i in items:
    s="{} ,{},{},{}\n".format(i[0],i[1],i[2],i[3])
    f.write(s)
    print(s)
    # 1.해당경로i[0]접속 2.저장(img\title.확장자)
    temp=requests.get(i[0])
    # print(temp)
    ext=i[0][-4:]
    # print(ext)
    # filename="img\\"+i[1]+ext
    filename="img\\"+i[1].replace("?","")+ext
    print(filename)
    f1=open(filename,"wb")
    f1.write(temp.content)



# a="do it! python"
# print(a[1:3])
# print(a[-4:])






