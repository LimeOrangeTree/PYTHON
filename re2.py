import re
import requests    #웹페이지접속패키지 #파일-셋팅즈-프로젝트-인터프리터-+
url="https://comic.naver.com/webtoon/list.nhn?titleId=682637&weekday=tue"
# 웹페이지접속 requests.get(접속경로)
result=requests.get(url)
print(result)   #200 접속성공, 404 없는페이지
print(result.text)
titles=re.findall(r'<td class="title">.+?<a href=".+?">(.+?)</a>.+?</td>',result.text,re.DOTALL)
print(titles)
print(len(titles))

scores=re.findall(r'<div class="rating_type">.+?<strong>(.+?)</strong>.+?</div>',result.text,re.DOTALL)
print(scores)
print(len(scores))

regdates=re.findall(r'<td class="num">(.+?)</td>',result.text,re.DOTALL)
print(regdates)
print(len(regdates))
