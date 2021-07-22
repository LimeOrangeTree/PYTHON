# import calendar
#
# # print(calendar.calendar(2019))
# print(calendar.prmonth(2019,5))
# print(calendar.weekday(2019,5,5))
# print(calendar.monthrange(2019,2))
# import random
# temp=[]
# random.seed(17)
# for i in range(10):
#     # temp.append(random.random())   #0~1 실수
#     # temp.append(random.randint(1,10))
#     temp.append(random.randint(100,200))
# print(temp)

# data=[1,2,3,4,5]
# random.shuffle(data)
# print(data)

# python book.py 3 10 55 88 7 10
# 3+10+55+88+7+10 출력
# import sys
# # print(sys.argv[0])
# # print(sys.argv[1])
# # print(sys.argv[2])
# # print(len(sys.argv))
# sum=0
# for i in range(1,len(sys.argv)):
#     sum=sum+int(sys.argv[i])
# print(sum)
# glob모듈을 이용하여 E:\big\pythonStudy 에서 확장자가 html인것만 출력하세요
# import glob
# print(glob.glob("E:\\big\pythonStudy\\*.html"))
#random모듈을 이용하여 로또번호 (1-45사이의 숫자 6개 생성, 단 중복숫자안됨)
# import random
# lotto=[]
# while(len(lotto)<6):
#     n=random.randint(1,45)
#     if n not in lotto:
#         lotto.append(n)
# print(lotto)
# print(abs(-777))
# print(abs(77))

# print(any([1,4,6,4,0]))
# print(any([0,0,0]))
#
# print(chr(65))
# print(chr(97))
#
# print(dir())
# print(dir([1,2,3]))

print(divmod(778,3))
a=['red','blue','green']
# for i in a:
#     print(i)
# for i in range(len(a)):
#     print(i,a[i])
# for i in enumerate(a):
#     print(i)
# for i,j in enumerate(a):
#     print(i,j)
# print(eval('1+5'))
# print(eval('divmod(4,3)'))

# def positive(x):
#     return x>0
#
# print(list(filter(positive,[8,-7,99,-8,0,5])))
# print(hex(16))
# print(oct(15))
#
# a=5
# print(id(a))
# print(id(5))
#
# def double(x):
#     return x*2
# print(list(map(double,[4,3,-7,99])))
# print(list(map(lambda x:x*2,[4,3,-7,99])))
# print(max([4,3,-7,99]))
# print(min([4,3,-7,99]))
#
# print(ord('B'))
# print(ord('b'))
#
# print(pow(2,10))

a=[4,3,-7,99]
print(a)
print(sorted(a))
print(sorted('zero'))
print(tuple(a))
# filter, lamda를 이용하여 [8,-7,99,-8,0,5]에서 음수 모두 제거
print(list(filter(lambda x:x>0,[8,-7,99,-8,0,5] )))



