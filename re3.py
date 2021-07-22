import re
import requests
url="https://comic.naver.com/webtoon/list.nhn?titleId=682637&weekday=tue"
result=requests.get(url)
print(result)
items=re.findall(r'<td class="title">.+?<a href=".+?">(.+?)</a>.+?<strong>(.+?)</strong>.+?<td class="num">(.+?)</td>',result.text,re.DOTALL)
# print(len(items))
# print(items)   #[(),(),()...()]
for i in items:    #i=items[0],items[1],
    # print(i)
    s="{},{},{}".format(i[0],i[1],i[2])
    print(s)
#     # for j in i:
#     #     print(j,end=' ')
#     # print()










