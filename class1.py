# 클래스:현실세계의 사물을 컴퓨터안에서 구현하기 위한 개념, 설계도

# 자동차
#    속성(바퀴, 변속,  연료,  속도,   모델명,...)  -->필드,멤버변수(변수)
#    기능(속도를 높이다,   속도를 내리다,...)      -->메서드(함수)
# # 클래스의 정의
# class 클래스명:
#     구현내용
# 1.클래스 정의
class Car:
    wheel=0
    method=""
    fuel=""
    speed=0
    model=""
    def speedUp(self,value):
        self.speed=self.speed+value
    def speedDown(self,value):
        self.speed=self.speed-value
# # 2.클래스 변수 생성
c1=Car()          # a=5  변수명=값
c2=Car()
# 3.사용
c1.wheel=4
c1.method="auto"
c1.fuel="gasoline"
c1.model="소나타"
print(c1.model,c1.speedUp(30),c1.speed)
print(c2.model,c2.speedDown(10),c2.speed)
#
# c2=Car()
# c2.wheel=8
# c2.method="manual"
# c2.fuel="gasoline"
# speed=100
# model="티볼리"

# 1.클래스 정의
# 2.클래스 변수 생성
# 3.사용
# class Triangle:
#     bottom=0
#     height=0
#     def area(self):
#         return 0.5*self.bottom*self.height   #self :자신의 변수를 사용

# t1=Triangle()     #t1,t2,t3 인스턴스 변수
# t2=Triangle()
# t3=Triangle()
# t1.bottom=20
# t1.height=30
# t3.bottom=3
# t3.height=4
# print(t1.bottom,t1.height,t1.area())
# print(t2.bottom,t2.height,t2.area())
# print(t3.bottom,t3.height,t3.area())












# 계산기
#   변수1
#   변수2
#   더하기
#   빼기
#   곱하기
#   나누기





