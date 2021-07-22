import re
import requests
url='http://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K'
result=requests.get(url)
names=re.findall\
    (r'<div class="mode-cell title">.+?<a href="/mycar/.+?" title="(.+?)"',result.text,re.DOTALL)
items=re.findall\
(r'<div class="mode-cell year">.+?<span>(.+?)</span>.+?<dd class="a-hide">(.+?)</dd>',result.text,re.DOTALL)
prices=re.findall\
    (r'<div class="mode-cell price">.+?<em class="cr">(.+?)</b>',result.text,re.DOTALL)
print(names)
print(items)
print(prices)
print(len(names))
print(len(items))
print(len(prices))

for i in zip(names,items,prices):
    # print(i)
    s1=i[1][0].replace("<br>","")
    s2=i[2].replace("</em>","")
    str="%s-%s-%s-%s"%(i[0],s1,i[1][1],s2)
    print(str)
