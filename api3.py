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
url = "https://openapi.naver.com/v1/search/book.json?display=50&start=101&query=" + encText # json 결과
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
