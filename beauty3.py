from bs4 import BeautifulSoup
import re
html=open('second.html','r',encoding='utf-8').read()
# print(html)
dom=BeautifulSoup(html,'lxml')
# 선택자 사용하기
# dom.select_one(선택자)
# dom.select(선택자)
h1=dom.select_one('body > h1').text
print(h1)
lidom=dom.select('#bible > li')
# print(lidom)
for li in lidom:
    print(li.string)

