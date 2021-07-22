# beautifulsoup4 설치
from bs4 import BeautifulSoup
html=open("one.html",'r',encoding='utf-8').read()
# print(html)
#BeautifulSoup(웹페이지,파싱방식)
# 파싱=html.parse, lxml, html5lib
dom=BeautifulSoup(html,"lxml")
# print(dom)
# dom객체.find("태그")
# dom객체.태그
# dom객체.find_all("태그")
# divdom=dom.find("div")
# divdom=dom.div
# print(divdom)
# divsdom=dom.find_all("div")
# print(divsdom)
# print(len(divsdom))
# -------------------------------
# 첫번째 div 요소안의 모든 p태그 추출
# divdom=dom.div  #divdom=dom.find("div")
# psdom=divdom.find_all("p")
# print(psdom)
# for p in psdom:
#     print(p)
# 클래스 추출-------------
# dom.find(class_='내용')
# dom.find("",{'class':'내용'})
# classdom=dom.find(class_='ex_class')
# # classdom=dom.find("",{'class':'ex_class'})
# print(classdom)
# classesdom=dom.find_all("",{'class':'ex_class'})
# print(classesdom)
# class가 sister인 모든 태그를 추출
#id 추출-------------
# dom.find(id='내용')
# dom.find("",{'id':'내용'})
# idsdom=dom.find(id='ex_id')
# for id in idsdom:
#     print(id)
# -특정태그의 특정 클래스(id) 가져오기----
# dom.find("태그",{'id':'내용'})
# dom.find("태그",{'class':'내용'})
# divdom=dom.find('div',{'id':"sample_id"})
# print(divdom)
# --데이터 추출
# dom.string
# dom.text
# dom.get_text()
# titledom=dom.title
# print(titledom)
# print(titledom.text)
# # 모든 a태그의 데이터을 추출
# asdom=dom.find_all("a")
# print(asdom)
# for a in asdom:
#     print(a.string)
# 속성내용추출
# dom['속성']
# dom.get('속성')
# dom.attrs['속성']
# id가 link1인 요소의 클래스 속성값 출력----
# iddom=dom.find("",{'id':'link1'})
# print(iddom['class'])
# 모든 a태그의 href 속성 출력---
# for a in dom.find_all('a'):
#     print(a['href'])
# 상위요소
# dom.parent
# dom.parents
# 클래스가 title인 p태그의 첫번째 상위요소
# pdom=dom.find("p",{'class':'title'})
# print(pdom.parent)
#  클래스가 title인 p태그의 모든 상위요소
# print(pdom.parents)
# for parent in pdom.parents:
#     print(parent)
#     print('-'*50)
# 하위요소-------------------------
# dom.children
# dom.descendants
# 아이디가 세컨드인 div 태그의 첫단계 하위요소
# divdom=dom.find("div",{'id':'second'})
# for c in divdom.children:
#     print(c)
#     print('-------------------------')
# 아이디가 세컨드인 div 태그의 모든 하위요소
# for d in divdom.descendants:
#     print(d)
#     print('-------------------------')
# 형제dom 추출
# dom.next_siblings      다음형제
# dom.previous_siblings  이전형제
# adom=dom.find('a',{'id':'link2'})
# print(adom.previous_siblings)
# for p in adom.previous_siblings:
#     print(p)
#     print('-------------------------')
#

#https://finance.naver.com/marketindex/ 에 접근하여
# 오늘의 환율을 추출하세요
import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/marketindex/"
result=requests.get(url)
# print(result)
dom=BeautifulSoup(result.text,'lxml')
divsdom=dom.find_all('div',{'class':'head_info point_dn'})
spandom=divsdom[0].find('span')
print(spandom.text)
# =========================
# dom객체.find("태그")
# dom객체.태그
# dom객체.find_all("태그")
# 클래스 추출-------------
# dom.find(class_='내용')
# dom.find("",{'class':'내용'})
#id 추출-------------
# dom.find(id='내용')
# dom.find("",{'id':'내용'})
# -특정태그의 특정 클래스(id) 가져오기----
# dom.find("태그",{'id':'내용'})
# dom.find("태그",{'class':'내용'})
# --데이터 추출
# dom.string
# dom.text
# dom.get_text()
# 속성내용추출
# dom['속성']
# dom.get('속성')
# dom.attrs['속성']
# 상위요소
# dom.parent
# dom.parents
# 하위요소-------------------------
# dom.children
# dom.descendants
# 형제dom 추출
# dom.next_siblings      다음형제
# dom.previous_siblings  이전형제







