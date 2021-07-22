from bs4 import BeautifulSoup
import requests
url="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
result=requests.get(url)
# print(result)
# print(result.text)
with open('data\\kma.csv','w',encoding='utf-8') as f:
    dom=BeautifulSoup(result.text,'lxml')
    # print(dom.find('title').text)
    # --province,city,mode,tmEf,wf,tmn,tmx,reliability
    # --수도권,,서울a,2-22,0,5 ...
    # --수도권,서울,a,2-22,12,10 ......
    locationdom=dom.find_all('location')
    print(len(locationdom))
    for location in locationdom:
        province=location.find('province')
        city=location.find('city')
        # print(province.text,city.text)
        datadom=location.find_all('data')
        # print(len(datadom))
        for data in datadom:
            mode=data.find('mode')
            tmEf=data.find('tmef')
            wf=data.find('wf')
            tmn=data.find('tmn')
            tmx=data.find('tmx')
            reliability=data.find('reliability')
            str="{},{},{},{},{},{},{},{}\n".format\
                (province.text,city.text,mode.text,tmEf.text,wf.text,tmn.text,tmx.text,reliability.text)
            # print(str)
            f.write(str)
# 파일로 저장 data\kma.csv









