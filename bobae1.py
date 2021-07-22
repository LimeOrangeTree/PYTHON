import re
import requests
url='http://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K'
f=open("data\\bobae.csv","w",encoding="utf-8")   # open(파일명,모드,옵션)
# f=open("data\\bobae.csv","w")
result=requests.get(url)
print(result)
items=re.findall(r'<div class="list-inner">.+?<div class="mode-cell title">.+?<a href="/mycar/.+?" title="(.+?)".+?<div class="mode-cell year">.+?<span>(.+?)</span>.+?<div class="mode-cell km">.+?<dd class="a-hide">(.+?)</dd>.+?<div class="mode-cell price">.+?<em class="cr">(.+?)</b>',result.text,re.DOTALL)
# 차이름,연식,주행거리,가격 을 수집하여 data\bobae.csv로 저장
# print(len(items))   items=[(a,b,c,d),(),()...()]    a=[1,2,3,4,5]
# print(items)
for item in items:
    # print(item)
    str="{}-{}-{}-{}\n".format\
        (item[0],item[1].replace("<br>",""),item[2],item[3].replace("</em>",""))
    # print(str)
    f.write(str)



# a=[1,2,3,4,5]
# for i in a:   #i=a[0],a[1],a[2]..
#     print(i)
# for i in range(len(a)):  #i=0,1,2,3,4
#     print(a[i])
#
# items=[(a,b,c,d),(),()...()]
# for i in items:   i=items[0],items[1],...
#     print(i)


