# import friday.one
# friday.one.f1()
# friday.one.f2(1000)

# from friday.one import f1,f2
# f1()
# f2(30)

# from friday.one import *
# f1()
# f2(30)
# def f3():
#     # pass
#     print('f3-->')
#     return 17
#     print('f3함수종료')
# def f4():
#     print('f4--->')
# # f3()
# # f4()
# # print(f3())
# # print(f4())
# a=f3()
# b=f4()
# print(a)
# print(b)
# def max2(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#     print('the end')

# def max2(a,b):
#     if a>b:
#         return a
#     return b
# print(max2(3,5))
# print(max2(7,5))
# print(max2(30,5))
#
# def max4(a,b,c,d):
#     return max2(max2(a,b), max2(c,d))
#
# # 4개의 정수중에 큰숫자를 찾는 함수
# print(max4(1,2,3,4))
# print(max4(100,20,30,4))


# def f5():    #0~99 한줄에 10개씩 출력
#     i=0
#     while i<100:
#         print(i,end=' ')
#         i+=1   #i=i+1
#         if i%10==0:
#             print()
# f5()
a,b=3,4
print(a)
print(b)
# 100보다 작은 짝수와 홀수의 합
def f6():
    s1,s2=0,0
    for i in range(100):
        if i%2==0:
            s1=s1+i
        else:
            s2=s2+i
    return s1,s2
# a,b=f6()
# print('짝수의 합',a)
# print('홀수의 합',b)
# 난수발생
import random
# print(random.randrange(10))
#
# for i in range(10):
#     # print(random.randrange(10),end=' ')
#     print(random.randrange(0,101,2),end=' ') #1~100 짝수

# a에 10~50의 홀수 난수 10개를 리스트로 넣으세요

# for i in range(10):
#     print(random.randrange(11,51,2))
# print()
# a=[random.randrange(11,51,2) for i in range(10)]
# print(a)
# a=[random.randrange(11,51,2) for _ in range(10)]
# print(a)
print('='*50)
# 10개의 100이하 난수중에 가장 큰숫자를 찾는 함수
def maxNumber():
    max=0
    for _ in range(10):
        n=random.randrange(101)
        print(n, end=" ")
        if max<n:
            max=n
    print()
    return max

a=maxNumber()
print('가장큰값=',a)

def f7(n):
    return n%10*10+n//10


print(f7(59))    #95 2자리숫자를 받아 뒤집는 함수수
print(f7(82))












