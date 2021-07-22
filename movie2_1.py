# create table movie(
#     title char(50),
#     score char(10),
#     rate char(10),
#     playtime char(10)
# );
# .table
import re
import requests
import sqlite3
con = sqlite3.connect("e:\\sqlite\\pythondb")
cur = con.cursor()
url="https://movie.naver.com/movie/running/current.nhn"
# f=open("data\\movie.csv","w",encoding="utf-8")
# 영화제목,점수,예매율,상영시간
result=requests.get(url)
titles=re.findall(r'<dt class="tit">.+?<a href="/movie/bi/mi/basic.+?">(.+?)</a>',result.text,re.DOTALL)
scores=re.findall(r'<div class="star_t1">.+?<span class="num">(.+?)</span>',result.text,re.DOTALL)
rates=re.findall(r'<span class="num2">참여.+?</em>명</span></a><!-- N=a:nol.urating -->.+?</div>(.+?)<dl class="info_txt1">',result.text,re.DOTALL)
final_rates=[]
for i in range(len(rates)):
    temp=re.findall(r'<span class="num">(.+?)</span>',rates[i],re.DOTALL)
    if len(temp)<1:
        final_rates.append('0.0')
    else:
        final_rates.append(temp[0])
times=re.findall(r'<dl class="info_txt1">.+?<!-- N=a:nol.genre,r:1 -->(.+?)201',result.text,re.DOTALL)
final_times=[]
for i in range(len(times)):
    temp=re.findall(r'<span class="split">.</span>(.+?)분',times[i],re.DOTALL)
    if len(temp)<1:
        final_times.append('확인중')
    else:
        final_times.append(temp[0].strip()+'분')
# print(final_times)
items=list(zip(titles,scores,final_rates,final_times))
for item in items: #item=items[0],items[1],..
    sql="insert into movie values('"+item[0]+"','"+item[1]+"','"+item[2]+"','"+item[3]+"')"
    cur.execute(sql)
con.commit()
con.close()






