# # import 패키지명
import re     #정규식 사용
# .:글자1개,줄바꿈제외
# [abc]
# [^abc]
# + 1개이상
# * 0개이상
# ? 0 or 1
# [0-9]
# [^A-Za-z]
# a{3}
# a{3,5}
# a{2,}  aa,aaa,aaaaaaaaaaa,aaaaaaaaaaaaa
# a{,3}  aa,aaa
# db="""3412    Bob 123
# 3834  Jonny 333
# 1248   Kate 634
# 1423   Tony 567
# 2567  Peter 435
# 3567  Alice 535
# 1548  Kerry 534"""
# print(db)
# #len(),index()
# # 형식
# # re.findall(r'정규식',문자열[,옵션])
# print('aaa\nbbb')
# print(r'aaa\nbbb')

# # result=re.findall(r"[0-9]",db)  #리스트로반환
# result=re.findall(r"[0-9]+",db)
# print(result)
# # 이름찾기
# result=re.findall(r"[A-Z][a-z]+",db)
# print(result)
# for i in range(len(result)):
#     print(result[i])
# for i in result: #i=result[0],result[1],..
#     print(i)
# # T로 시작하는 이름 찾기
# result=re.findall(r"T[a-z]+",db)
# print(result)

# db="internationalization"  #
# # i로 시작하고 n으로 종료되는 문자
# result=re.findall(r"i.+n",db)  #greedy
# print(result)
# result=re.findall(r"i.+?n",db) #non-greedy
# print(result)
# result=re.findall(r"i(.+?)n",db)
# print(result)
html="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
안녕하세요
</body>
</html>"""
# print(html)
# result=re.findall(r"<.+>",html)
# result=re.findall(r"<.+?>",html)
# result=re.findall(r"<(.+?)>",html)
# print(result)
# print(len(result))
# Title 추출
result=re.findall(r"<title>(.+?)</title>",html)
print(result)
# 안녕하세요
result=re.findall(r"<body>(.+?)</body>",html,re.DOTALL) #줄바꿈포함
print(result)
print(type(result))
print(type(result[0]))
result[0]=result[0].replace("\n","")
print(result)
# a=[3,4]   a[0],a[1]
# a=[3]     a[0]
# print(a.replace(" ","!@!"))
# <head>와 </head> 사이의 내용 추출
result=re.findall(r"<head>(.+?)</head>",html,re.DOTALL)
print(result)
result[0]=result[0].replace("\n","")
print(result)
result[0]=result[0].lstrip()
print(result)
result[0]=result[0].replace(" ","")
print(result)








