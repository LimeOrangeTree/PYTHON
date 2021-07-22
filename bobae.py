# http://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K
# 차이름, 연식, 주행거리, 가격을 수집하여 bobae.csv로 저장

http://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K"

result=requests.get(url)
# print(result.text)
name=re.findall(r'<p class="tit ellipsis">.+?target="_blank">(.+?)</a>',result.text,re.DOTALL)
print(name)
print(len(name))

model=re.findall(r'<div class="mode-cell year">.+?<span>(.+?)</span>',result.text,re.DOTALL)
# model=<br> replace
print(model)
print(len(model))

mileage=re.findall(r'<div class="mode-cell km">.+?<dd class="a-hide">(.+?)</dd>',result.text,re.DOTALL)
print(mileage)
print(len(mileage))

price=re.findall(r'<div class="mode-cell price">.+?<em class="cr">(.+?)</b>',result.text,re.DOTALL)
for item in items:
    print (item)
    str="{},{},{},{}".format\
        (item[0],item[1],item[2].replace("<br>","")),item[3].replace("</em>",""))
    print(str)
print(price)
print(len(price))
