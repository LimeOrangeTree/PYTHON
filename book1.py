# def gugudan(n):
#     result=[]
#     for i in range(1,10):
#         result.append(n*i)
#     return result
# result=gugudan(3)   # --->[3,6,..27]
# print(result)
# result=gugudan(9)   # --->[3,6,..27]
# print(result)
# 1~100 중에 3의 배수만 반환하는 함수를 구현
# def num():
#     result=[]
#     for i in range(1,101):
#         if i%3==0:
#             result.append(i)
#     return result
# print(num())
# 1~100 중에 3의 배수합을 반환
# def num():
#     result=0
#     for i in range(1,101):
#         if i%3==0:
#             result=result+i
#     return result
# print(num())
# 1000미만 자연수중에 3의 배수 또는 5의배수합을 반환
# def num():
#     result=0
#     for i in range(1,1001):
#         if i%3==0 or i%5==0 :
#             result=result+i
#     return result
# print(num())
#--------------
# 데이터-312껀
# 한페이지당 10건의 자료를 표시
# 몇페이지가 나오는가?
#
# def calPage(m,n):   #데이터건수,한페이지당표시건수
#     if m%n==0:
#         return m//n
#     else:
#         return m//n+1
# print(calPage(312,10))
# print(calPage(312,7))

# python book1.py a "

# import sys
# if sys.argv[1]=='a':
#     f=open('data\\memo.txt','a',encoding='utf-8')
#     f.write(sys.argv[2]+"\n")
# elif sys.argv[1]=='v':
#     f=open('data\\memo.txt',encoding='utf-8')
#     text=f.read()
#     print(text)
# f.close()

# python book1.py data\test1.txt data\test2.txt
import sys
f=open(sys.argv[1])
text=f.read()
f.close()
text=text.replace('\t',' '*4)
f=open(sys.argv[2],'w')
f.write(text)
f.close()













