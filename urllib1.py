from urllib.parse import urljoin
base="http://www.iedu.or.kr/html/a.html"
print(urljoin(base,'b.html'))
print(urljoin(base,'sub/c.html'))
print(urljoin(base,'../d.html'))
print(urljoin(base,'../css/e.html'))
print(urljoin(base,'http://www.naver.com'))
print(urljoin(base,'//www.daum.net'))
print(urljoin(base,'/z.html'))