import re
import requests
url='http://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K'
result=requests.get(url)
items=re.findall(r'<div class="list-inner">.+?<img src="(.+?)" alt=".+?<div class="mode-cell title">.+?<a href=".+?title="(.+?)" target="',result.text,re.DOTALL)
print(len(items))
print(items)
for i in range(len(items)):
    # print(items[i])   #(그림경로,제목)
    filename="img\\"+items[i][1]+items[i][0][-4:]  #경로+제목+확장자
    print(filename)
    temp=requests.get(items[i][0])
    f1=open(filename,"wb")
    f1.write(temp.content)
