import re
import requests

def saveImage(imgUrl,title):
    temp=requests.get(imgUrl)
    ext=imgUrl[-4:]
    filename="img\\"+title.replace("?","")+ext
    print(filename)
    f1=open(filename,"wb")
    f1.write(temp.content)
def saveCsv(f,s):
    f.write(s)
def main():
    url="https://comic.naver.com/webtoon/list.nhn?titleId=682637&weekday=tue"
    f=open("data\webtoon.csv","w",encoding="utf-8")   #w쓰기모드
    result=requests.get(url)
    items=re.findall\
    (r'<td>.+?<a href="/webtoon/.+?<img src="(.+?)" title="(.+?)" alt=".+?<strong>(.+?)</strong>.+?<td class="num">(.+?)</td>', result.text,re.DOTALL)
    for i in items:
        s="{} ,{},{},{}\n".format(i[0],i[1],i[2],i[3])
        saveCsv(f,s)
        saveImage(i[0],i[1])
if __name__=="__main__":
    main()







