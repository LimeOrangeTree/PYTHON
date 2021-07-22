import re
import requests
# url='http://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K'
url='http://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page={}&view_size=20'

for page in range(1,21):
    pageUrl=url.format(page)
    result=requests.get(pageUrl)

def makeUrl(page):
    pafeUrl=url.format(page)
    return  pageUrl

def getWebPage(pageUrl):
    result = requests.get(pageUrl)
    return result.text
def findItems(html):
    names = re.findall \
        (r'<div class="mode-cell title">.+?<a href="/mycar/.+?" title="(.+?)"', html, re.DOTALL)
    items = re.findall \
        (r'<div class="mode-cell year">.+?<span>(.+?)</span>.+?<dd class="a-hide">(.+?)</dd>', html, re.DOTALL)
    prices = re.findall \
        (r'<div class="mode-cell price">.+?<em class="cr">(.+?)</b>', html, re.DOTALL)

    for i in zip(names, items, prices):
        # print(i)
        s1 = i[1][0].replace("<br>", "")
        s2 = i[2].replace("</em>", "")
        str = "%s-%s-%s-%s" % (i[0], s1, i[1][1], s2)
        print(str)

def main():
    for page in range(1,21):
        pageUrl=makeUrl(page)
        html=getWebPage(pageUrl)
        findItems(html)

if __name__=="__main__":
    main()
