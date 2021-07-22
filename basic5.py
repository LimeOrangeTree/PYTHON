# print(1+2)
# eval(표현식)
# print(eval('1+2'))
# if 조건:
#     참인경우 수행문장1
#     참인경우 수행문장2
# job=int(input('1:수식계산, 2:두수의 합계-->'))
# if job==1:
#     ex=input('수식을 입력하세요-->')
#     # print(eval(ex))
#     print("%s 의 결과는 %s"%(ex,eval(ex)))
# else:
#     n1=int(input('숫자1-->'))
#     n2=int(input('숫자2-->'))
#     # print(n1+n2)
#     print("{}+{}={}".format(n1,n2,n1+n2))

# if 조건1:
#     조건1이 참인경우 수행문장
# elif 조건2:
#     조건2이 참인경우 수행문장
# elif 조건3:
#     조건3이 참인경우 수행문장
# ...
# else:
#     모든조건이 거짓인경우 수행문장
# score=int(input('점수입력-->'))
# if (score>=90):
#     print("A",end='')
# elif (score>=80):
#     print("B",end='')
# elif (score>=70):
#     print("C",end='')
# else:
#     print("F",end='')
# print("학점입니다.")
# 반복문
# print("파이썬 학습중")
# print("파이썬 학습중")
# print("파이썬 학습중")

# for 변수 in range(시작값,종료값,증감값):
#     반복수행내용

# for i in range(1,4,1):     # 1<=i<4  1,2,3
#     print(i,"파이썬 학습중")
#
# for i in range(10,13,1):
#     print(i,"파이썬 학습중")
#
# for i in range(6,1,-2):
#     print(i,"파이썬 학습중")

# for i in range(5):   #0에서 시작,증감이 1인경우 생략가능
#     print(i,"파이썬 학습중")
# # 1+2+3+....+9999=
# # 1+2+3
# hap=0
# for j in range(1,4,1):  #j=1   hap=0+1
#     hap=hap+j           #j=2   hap=0+1+2
#     print(j,hap)        #j=3   hap=0+1+2+3

# hap=0
# for j in range(1,11,1):
#     hap=hap+j
#     print(j,hap)

# 3!=1*2*3
# 10!
# mul=1
# for j in range(1,11,1):   # j=1  mul=1
#     mul=mul*j             #j=2  mul=1*2
# print(mul)                #j=3  mul=1*2*3
# 1-100숫자중 짝수의 합과 홀수의 합을 출력
# hap1,hap2=0,0
# for i in range(1,101,1):
#     if i%2==0:
#         hap1=hap1+i
#     else:   #홀수
#         hap2=hap2+i
# print("홀수의 합 {}이고 짝수의 합{}".format(hap2,hap1))
# 2*1=2
# ....
#2*9=18
# dan=2
# for i in range(1,10):
#     print("{} X {} = {}".format(dan,i,dan*i))

# 키보드로 부터 단을 입력받아 해당 구구단을 출력하세요
# dan=int(input('출력할 단을 입력하세요-->'))
# #1~9   3*1=3 ....3*9=27
# for i in range(1,10):  #1~9
#     print("{} X {} = {}".format(dan,i,dan*i))
# 실습)
# 1단 2단 3단
# 4단 5단 6단
# 7단 8단 9단
# for dan in range(1,10,3):
#     for i in range(1,10):
#         print("{}X{}={} {}X{}={} {}X{}={}".format
#          (dan, i, dan * i,(dan + 1), i, (dan + 1) * i,(dan + 2), i, (dan + 2) * i))

# 이중for문
# for i in range(1,4):          #i=1         i=2
#     for j in range(21,26):   # j=21~25     21-25
#         print("i={},j={}".format(i,j))
#2단~5단
# 2 : 1~9
# 3 : 1~9
# 4 : 1~9
# 5 : 1~9
# for dan in range(2,6):    #2~5
#     for j in range(1,10):
#         print("{}X{}={}".format(dan,j,dan*j))
# 실습)
# 2단
# 4단
# 6단
# 8단
# for i in range(시작값,종료값,증감값)   시작값<=   <종료값
# for i in range(2,9,2):
#     # print(i)
#     for j in range(1,10,1):
#         print("{}X{}={}".format(i,j,i*j))

# 1,4,7단 출력
# for i in range(1,8,3):
#     # print(i)
#     for j in range(1,10,1):
#         print("{}X{}={}".format(i,j,i*j))
# 응용실습
# 2단          3단  ~           9단
# 한줄 띄우고(print)
# 2*1=2      3*1=3           9*1=9
# ...
# 2 * 9 = 18 3 * 9 = 27      9 * 9 = 81
for dan in range(2,10):
    print(dan,'단  ',end=' ')
print()
for j in range(1,10):
    for dan in range(2,10):
        print("{}X{}={}".format(dan,j,dan*j),end=" ")
    print()
