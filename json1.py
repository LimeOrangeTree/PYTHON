import json
j1='{"ip": "8.8.8.8"}'
print(type(j1))
j2=json.loads(j1)   #문자열-->딕션어리
print(type(j2))
print(j2["ip"])
j3='''{
   "Accept-Language": "en-US,en;q=0.8",
   "Host": "headers.jsontest.com",
   "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}'''
print(j3)
j4=json.loads(j3)
print(type(j4))
# j4에서 값만 출력해보세요
for k in j4:   #키값만 반환
    print(j4[k])
for k,v in j4.items():
    print(k,v)
# ------
j5='''{
   "Accept-Language": true,
   "Host": null,
   "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}'''
print(j5)
j6=json.loads(j5)
print(j6)
# 딕션어리-->문자열
j7=json.dumps(j6)
print(type(j7))






