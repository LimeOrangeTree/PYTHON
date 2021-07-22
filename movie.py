import re
import requests
url="https://movie.naver.com/movie/running/current.nhn"
# 영화제목,점수,예매율,상영시간
result=requests.get(url)
print(result)
titles=re.findall(r'<dt class="tit">.+?<a href="/movie/bi/mi/basic.+?">(.+?)</a>',result.text,re.DOTALL)
print(len(titles))
print(titles)
scores=re.findall(r'<div class="star_t1">.+?<span class="num">(.+?)</span>',result.text,re.DOTALL)
print(len(scores))
print(scores)
rates=re.findall\
(r'<span class="num2">참여.+?</em>명</span></a><!-- N=a:nol.urating -->.+?</div>(.+?)<dl class="info_txt1">',result.text,re.DOTALL)
print(len(rates))
print(rates)
final_rates=[]
for i in range(len(rates)):
    # print('-'*50)
    # print(rates[i])
    temp=re.findall(r'<span class="num">(.+?)</span>',rates[i],re.DOTALL)
    # print(temp[0])
    # print(temp)
    if len(temp)<1:
        final_rates.append('0.0')
    else:
        final_rates.append(temp[0])
print(final_rates)
print(len(final_rates))
# times=re.findall(r'<span class="link_txt">.+?<span class="split">.</span>(.+?)201',result.text,re.DOTALL)
times=re.findall(r'<dl class="info_txt1">.+?<!-- N=a:nol.genre,r:1 -->(.+?)201',result.text,re.DOTALL)
print(len(times))
final_times=[]
for i in range(len(times)):
    temp=re.findall(r'<span class="split">.</span>(.+?)분',times[i],re.DOTALL)
    if len(temp)<1:
        final_times.append('확인중')
    else:
        final_times.append(temp[0].strip()+'분')
print(final_times)












