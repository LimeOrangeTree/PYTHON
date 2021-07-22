# 생성자:객체생성시에 호출되는 메서드__init__,초기화 작업에 많이 사용
# class Triangle:
#     bottom=0
#     height=0
#     def __init__(self):
#         print("삼각형이 생성됨")
#     def area(self):
#         return 0.5*self.bottom*self.height
# t1=Triangle()
# t1.height=100
# t1.bottom=50
# print(t1.area())
# t2=Triangle()
# print(t2.area())
# ----
# class Triangle:
#     bottom=0
#     height=0
#     def __init__(self,b,h):
#         self.bottom=b
#         self.height=h
#         print("삼각형이 생성됨")
#     def area(self):
#         return 0.5*self.bottom*self.height
# t1=Triangle(3,4)
# t2=Triangle(10,1000)
# print(t1.area())
# print(t2.area())
# -------------------------------
# class Triangle:
#     def __init__(self,b,h):
#         self.bottom=b
#         self.height=h
#         print("삼각형이 생성됨")
#     def area(self):
#         return 0.5*self.bottom*self.height
# t1=Triangle(3,4)
# t2=Triangle(10,1000)
# print(t1.area(),t1.bottom,t1.height)
# print(t2.area(),t2.bottom,t2.height)
# ---------------------
# class Car:
#     def __init__(self,model,method,fuel,wheel):
#         self.model=model
#         self.method=method
#         self.fuel=fuel
#         self.wheel=wheel
#         self.speed=0
#     def speedUp(self,value):
#         self.speed=self.speed+value
#     def speedDown(self,value):
#         self.speed=self.speed-value
# c1=Car("아우디","자동","가솔린","4")
# c2=Car("쌍용","수동","경유","8")
# c1.speedUp(100)
# c2.speedUp(50)
# print(c1.model,c1.method,c1.speed)
# print(c2.model,c2.method,c2.speed)

# 학생
# 이름,전번,국,영,수
# 시험치다(국,영,수 할당)
# 학점을계산하다 (a,b,c,d,f)
# 학생 이름과 전번을 가지고 생성, 점수는 0으로
# 학생 2명 생성
class Student:
    def __init__(self,n,t):   #생성자
        self.name=n
        self.tel=t
        self.kor=0
        self.eng=0
        self.mat=0
    def testing(self,k,e,m):
        self.kor=k
        self.eng=e
        self.mat=m
    def getGrade(self):
        result=(self.kor+self.eng+self.mat)/3
        if result>=90:
            return "A"
        elif result>=80:
            return "B"
        elif result>=70:
            return "C"
        elif result>=60:
            return "D"
        else:
            return "F"
s1=Student("심청","010-1234-4561")
s2=Student("심슨","010-7894-4561")
s1.testing(100,80,90)
s2.testing(80,80,95)
print(s1.name,s1.getGrade())
print(s2.name,s2.getGrade())

ban=[Student("심청","010-1234-4561"),
     Student("심슨","010-7894-4561"),
     Student("심신","010-789-4563")]

for i in ban:   #i=ban[0],ban[1],...
    print(i.name,i.tel)




