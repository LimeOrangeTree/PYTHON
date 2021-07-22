#application programming interface
import os
import sys
import urllib.request
import json
client_id = "CErOrUqKUfGLkcbs54lj"
client_secret = "yJa2Jjbvu0"
encText = urllib.parse.quote("봄")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# 경로지정시
# http://경로?변수명1=값1&변수명2=값2&변수명3=값3
url = "https://openapi.naver.com/v1/search/blog?display=50&start=100&query=" + encText # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
print(result)
result1=json.loads(result)
print(result1["lastBuildDate"])
# print(result1["items"])  #[{0},{1},{},{},....{9}]  리스트
# print(result1["items"][1])  #{1}   딕션어리
print(result1["items"][1]["title"])
# 제목과 상세설명,경로들 가져오기
print('-'*30)
for i in result1["items"]:   #i=result1["items"][0],i=result1["items"][1]
    print(i["title"])
    print(i["description"])
    print(i["bloggerlink"])