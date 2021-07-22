# 1~10까지의 합
# hap=0
# for i in range(1,11):
#     hap=hap+i
# print(hap)
# while 조건문:
#     조건이 참인경우 수행내용
# hap=0
# i=1
# while i<=3:     #1<=3  참   2<=3           3<=3            4<=3 거짓
#     hap=hap+i    #hap=0+1   hap=0+1+2   hap=0+1+2+3
#     i=i+1        #i=2        3             4
# print(hap)                                                 #실행

#시작값과 종료값을 받아서 그 사이의 합계출력
# start=int(input('시작->'))
# end=int(input('종료->'))
# hap=0
# for i in range(start,end+1):
#     hap=hap+i
# print("%s에서 %s까지의 합은 %s"%(start,end,hap))
#-->while문으로
# while 조건문:
#     조건이 참인경우 수행내용
# start=int(input('시작->'))
# end=int(input('종료->'))
# hap=0
# i=start
# while (i<=end):
#     hap=hap+i
#     # i=i+1
# print("%s에서 %s까지의 합은 %s"%(start,end,hap))

# while True:
#     a=int(input('숫자1->'))
#     if a==0:
#         break    #반복문을 빠져나감
#     b=int(input('숫자2->'))
#     hap=a+b
#     print("%s + %s = %s"%(a,b,hap))
#     # print("{} + {} = {}".format(a,b,hap))

# for i in range(10):  #0에서 10보다 작을때까지 1씩 증가
#     print(i)
#     if i>5:
#         break
# while문과 if을 이용(연산자는 +,-,*,/,//,%), 숫자1에 999들어오면 종료
# 숫자1-> 5
# 숫자2-> 3
# 연산자->%
# 5%3=2
# 숫자1->

# while True:
#     a=int(input("숫자1->"))
#     if a==999:
#         break
#     b=int(input("숫자2->"))
#     c=input("연산자->")
#     if c=="+":
#         print("%s + %s = %s"%(a,b,a+b))
#     elif c=="-":
#         print("%s - %s = %s"%(a,b,a-b))
#     elif c=="*":
#         print("%s * %s = %s"%(a,b,a*b))
#     elif c=="/":
#         print("%s / %s = %s"%(a,b,a/b))
#     elif c=="//":
#         print("%s // %s = %s"%(a,b,a//b))
#     elif c=="%":
#         print("%s % %s = %s"%(a,b,a%b))
#     else:
#         print("잘못된 연산자입니다.")

# a="hi~ "
# b="python"
# c=a+b
# d=a*3
# # e=a-b
# print(a,b)
# print(a+b)
# print(c)
# print(d)
# aa=5
# bb=7
# print(aa,bb)
# print("a="+a)
# print("b="+b)
# # print("aa="+aa)
# print("aa=",aa)

# print("bb="+bb)
# -->eval()사용
# while True:
#     a=input("숫자1->")
#     if a=="999":
#         break
#     b=input("숫자2->")
#     c=input("연산자->")
#     # print(a+c+b)
#     if c!="+" & c!="-" & c!="*" & c!="/" & c!="//" & c!="%":
#         print("잘못된 연산자입니다.")
#     else:
#         print("%s %s %s의 결과는 %s"%(a,c,b,eval(a+c+b)))

# 실습)1~100까지의 합을 구하는 중 그 합이 최초로 1000이 넘게 하는 숫자와 그 합 출력
# for, break 이용
# hap=0
# for i in range(1,101):
#     hap=hap+i
#     if hap>1000:
#         break
# print(i,hap)
# ==>while문으로 변경
# hap=0
# i=1
# while i<=100:
#     hap=hap+i
#     if hap>1000:
#         break
#     i=i+1
# print(i,hap)
# 1,2,3,4,6,7,8,9,10의 합
# continue 반복문으로 분기
# hap=0
# for i in range(1,11):
#     if i==5:
#         continue
#     hap=hap+i
# print(hap)
# 1~100까지의 합(3의배수는 제외) 출력
hap=0
for i in range(1,101):
    if i%3==0:
        continue
    hap=hap+i
print(hap)










