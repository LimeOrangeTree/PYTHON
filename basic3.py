# age=15
# b1=age>=10
# b2=age<20
# print(b1)
# print(b2)
# print(age>=10 and age<20)
# print(10<=age<20)
#
# # 문자열인덱싱:문자열중 특정데이터 추출
# # [시작인덱스:끝인덱스:증감]
# a="0123456789"
#
# print(a)
# print(a[2:4])   #2<=n<4
# print(a[5])
# print(a[5:])
# print(a[:3])
# print(a[:])
# print(a[:-1])
# print(a[3:-3])  #3<=n<-3
# print(a[3:7])   #3<=n<7
# # -----------------------
# a=5
# b=3
# a-=b
# print(a)
# a=a+b    #a+=b
# a=a*b    #a*=b
# a=a%b    #a%=b

# 키보드로 금액을 입력받아
# 1000원짜리 와 100 짜리로 교환하려고함
# won=int(input("교환할돈 얼마-->"))
# w1000=won//1000
# print("1000원짜리==>",w1000)
# # won=won%1000
# won%=1000
# print("남은금액==>",won)

# 3210==> 3210//1000 =3
#         3210%1000 = 210

# # 포맷팅(%d 정수, %f실수, %s 문자)
# a=123
# print("변수 a의 값은 %d입니다.!"%a)
# print("변수 a의 값은 %5d입니다.!"%a)
# print("변수 a의 값은 %05d입니다.!"%a)
# b=3.156
# print("%f"%b)
# print("%7.1f"%b)
# print("%7.3f"%b)   #소수점포함 7자리
# print("%7.3f"%10000.78912)
#
# print("I like [%s] ^^"%"Python")
# print("I like [%10s] ^^"%"Python")
# print("I like [%-10s] ^^"%"Python")
#
# print("%d 와 %d 의 곱은 %d이다"%(1,2,1*2))
# print("%d 와 %d 의 곱은 %d이다"%(1,2,1*2,3))
# print("%d 와 %d 의 곱은 %d이다"%("1",2,1*2))
# print("%s 와 %s 의 곱은 %s이다"%("1",2,1*2))
#
# # {}
# print("{}와 {}의 곱은 {}이다".format(1,2,1+2))
# print("{0}와 {1}의 곱은 {2}이다".format(1,2,1+2))
# print("{2}와 {1}의 곱은 {0}이다".format(1,2,1+2))
# print('-'*30)
# print("가나다{}123456".format("A"))
# print("가나다{:<10}123456".format("A"))
# print("가나다{:>10}123456".format("A"))
# print("가나다{:^10}123456".format("A"))
# print("가나다{:*^10}123456".format("A"))
# print(int(8.3),int(2.7))
# print("가나다{}abc".format(int(8.3)/int(2.7)))
# print("가나다{0:.0f}abc".format(int(8.3)/int(2.7)))
# print("가나다{:.1f}abc".format(8.3/2.7))
# print("가나다{:.2f}abc".format(8.3/2.7))
# # 이스케이프문자
# print("글자안에 '따옴표 표시")
# print("글자안에 \"따옴표 표시")
# print("글자안에 \\따옴표 표시")
# print("글자안에 \\\\\\따옴표 표시")
# print("글자안에 줄바꿈\n과 탭\t표시")
# # print(r'')사용
# print(r"글자\n안에\t따옴표\표시")
#
# a="4567980365418954364890159735014"
# print(a.count('5'))
# print(a.count('2'))
# print(a.find('5'))
# print(a.find('2'))
# a="The official home of the Python Programming Language."
# b=a.split()
# print(b)
# c='-'
# d=c.join(b)
# print(d)
# e=d.split('-')
# print(e)
# 공백지우기
# a="  the    official    home    "
# print("[",a,"]")
# print("[",a.lstrip(),"]")
# print("[",a.rstrip(),"]")
# print("[",a.strip(),"]")
# a="the official home of the Python Programming Language."
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
#
# print(a.replace(" ","!@!"))

# 실습)입력된 액수만큼 500원,100원,50원,10원동전으로 교환해주는 프로그램
# 동전의 갯수는 최소화
# 예)1111을 입력하면
# 500원 2
# 100원 1
# 50원 0
# 10원 1
# 남은금액1
won=int(input("교환할돈 얼마-->"))
c500=won//500
won=won%500
print("500원",c500)
c100=won//100
print("100원",c100)
won=won%100
c50=won//50
print("50원",c50)
won=won%50
c10=won//10
print("10원",c10)
won=won%10
print("남은금액",won)









