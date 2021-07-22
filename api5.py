import os
import sys
import urllib.request
import json
client_id = "3F6Tnv2gJ52TlibXLZEx"
client_secret = "9KAM96ur6m"
encText = urllib.parse.quote('''
~~~~

''')
data = "source=en&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
result1=json.loads(result)
print(result1)
# print(result1['message'])  #{}
# print(result1['message']['result'])  #{}
print(result1['message']['result']['translatedText'])
# -->번역된 내용만 출력
