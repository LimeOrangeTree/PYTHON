# import re
# import requests
# # url='http://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K'
# url="http://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page={}&view_size=20"
# no=0
# for page in range(1,21):
#     pageUrl=url.format(page)
#     result=requests.get(pageUrl)
#     names=re.findall\
#         (r'<div class="mode-cell title">.+?<a href="/mycar/.+?" title="(.+?)"',result.text,re.DOTALL)
#     items=re.findall\
#     (r'<div class="mode-cell year">.+?<span>(.+?)</span>.+?<dd class="a-hide">(.+?)</dd>',result.text,re.DOTALL)
#     prices=re.findall\
#         (r'<div class="mode-cell price">.+?<em class="cr">(.+?)</b>',result.text,re.DOTALL)
#     # print(names)
#     # print(items)
#     # print(prices)
#     # print(len(names))
#     # print(len(items))
#     # print(len(prices))
#     for i in zip(names,items,prices):
#         no=no+1
#         # print(i)
#         s1=i[1][0].replace("<br>","")
#         s2=i[2].replace("</em>","")
#         # str="%s-%s-%s-%s"%(i[0],s1,i[1][1],s2)
#         # print(str)
#         str="%s-%s-%s-%s-%s"%(no,i[0],s1,i[1][1],s2)
#         print(str)
#---------------------------------
import re
import requests
url="http://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page={}&view_size=20"
def makeUrl(page):
    pageUrl=url.format(page)
    return pageUrl
def getWebPage(pageUrl):
    result=requests.get(pageUrl)
    return result.text
def findItems(html):
    names=re.findall\
        (r'<div class="mode-cell title">.+?<a href="/mycar/.+?" title="(.+?)"',html,re.DOTALL)
    items=re.findall\
    (r'<div class="mode-cell year">.+?<span>(.+?)</span>.+?<dd class="a-hide">(.+?)</dd>',html,re.DOTALL)
    prices=re.findall\
        (r'<div class="mode-cell price">.+?<em class="cr">(.+?)</b>',html,re.DOTALL)
    for i in zip(names,items,prices):
        s1=i[1][0].replace("<br>","")
        s2=i[2].replace("</em>","")
        str="%s-%s-%s-%s"%(i[0],s1,i[1][1],s2)
        print(str)
def main():
    for page in range(1,21):
        pageUrl=makeUrl(page)
        html=getWebPage(pageUrl)
        findItems(html)
if __name__=="__main__":
    main()
