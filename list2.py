# a=[1,2,3,4,5,6,7,8,9,10]생성
#1~10 출력
for i in range(1,11):
    print(i)
# ==>리스트로 하여 변수 a로 생성
a=[i for i in range(1,11)]
print(a)
# b=[10,20,30,...150]
for i in range(10,151,10):
    print(i)
b=[i for i in range(10,151,10)]
print(b)
# c=[7,7,....,7]
# for i in range(100):
#     print(7)
c=[7 for i in range(100)]
print(c)
print(len(c))
#a=[0,25,100,....]  #0*0,5*5,10*10,,...,50*50
for i in range(0,51,5):
    print(i*i)
a=[i*i for i in range(0,51,5)]
print(a)
# 0~100 숫자중 홀수만 가져오기
for i in range(100):
    if i%2==1:
        print(i)
a=[i for i in range(100) if i%2==1]
print(a)
# 10을 50개 가지는 리스트 b를 만드세요
b=[10 for i in range(50)]
b=[10 for _ in range(50)]
print(b)











