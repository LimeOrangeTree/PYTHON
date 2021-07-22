# def f1():
#     print("f1()",a,b)
#     # print("f1()",a,b,c)
# def f2():
#     c=30
#     a=1
#     print("f2()",a,b,c)
# a=10
# b=20
# f1()
# f2()
# print(a)
def f3(v):
    print("함수f3",v)
    s=0
    for i in v:
        s=s+i
    return s

import random
# a=[random.randrange(101) for _ in range(10)]
# print(a)
# hap=f3(a)
# print(hap)

# 리스트를 받아 그 값을 2배로 반환하는 함수 f7
# def f7(v):
#     n=[]
#     for i in v:  #i=v[0],v[1],..
#         n.append(i*2)
#     return n
#
# print(f7([1,2,3,4,5]))   #출력=>[2,4,6,8,10]
# a=[random.randrange(101) for i in range(10)]
# print(a)
# print(f7(a))
# print(f7(3))
# def double(x):
#     return x*2
#
# print(double(3))
# print(double(10))
# print(double([1,2,3,4,5]))
# # map 함수 : 입력받은 자료형의 각요소가 함수를 수행후 결과를 묶어서 반환
# # map(함수,반복가능한 자료형)
# print(map(double,[1,2,3,4,5]))
# print(list(map(double,[1,2,3,4,5])))

# 람다함수
# def f11(a,b):
#     return a+b
#
# print(f11(1,2))
# f12=lambda a,b:a+b
# print(f12(1,2))
# f13=lambda a=1,b=2,c=3:a*b*c
# print(f13(10,20))
# print(f13())
# # double함수를 람다함수 f14로 ...
# f14=lambda x:x*2
# print(f14(10))
# print(list(map(f14,[10,20,30,40])))

# def f20(a,b):
#     print('f20')
#     return
#     return a+b
#
# print(f20(1,2))
def getNumber():
    r=[]
    for i in range(6):
        r.append(random.randrange(1,46))
    return r

num=getNumber()  #로또 번호추첨, 랜덤 1~45 사이의 숫자 6개
print(num)

# 내부함수
def outF(a,b):
    def inF(c,d):
        return c+d
    return inF(a,b)

print(outF(10,20))
# print(inF(10,20))




