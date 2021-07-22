# class Calc:
#     a=100
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def add(self):
#         print(self.x+self.y+self.a)
#     def sub(self):
#         print(self.a-self.x-self.y)
#     def __del__(self):   #소멸자
#         print("계산기 삭제")
# c1=Calc(3,4)
# c2=Calc(30,40)
# c1.add()   #3+4+100
# c1.a=77
# c1.sub()   #77-3-4
# del c1
# c2.add()   #100+30+40
# ------------------
# class Calc:
#     a=100
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def add(self):
#         print(self.x+self.y+Calc.a)
#     def sub(self):
#         print(Calc.a-self.x-self.y)
#     def __del__(self):   #소멸자
#         print("계산기 삭제")
#
# c1=Calc(3,4)
# c2=Calc(30,40)
# c1.add()   #3+4+100
# c1.a=77
# c1.sub()   #100-3-4
# # del c1
# c2.add()   #100+30+40
#----------------------------------------------------
# class Number:
#     x=0
#     y=0
#     def numberPrint(self):
#         self.x=self.x+1       #x인스턴스변수
#         Number.y=Number.y+1   #y클래스변수
#         print("x,y={},{}".format(self.x,Number.y))
#
# a=Number()
# b=Number()
# a.numberPrint()
# b.numberPrint()
# b.numberPrint()
# ---상속
# class Car(object):   #모든 클래스는 object클래스를 상속
#     speed=0
#     def speedUp(self,speed):
#         self.speed=self.speed+speed
#         print("현재 속도(Car)는 %s"% self.speed)
# class Sedan(Car):
#     pass
# class Truck(Car):
#     pass
#
# s1=Sedan()
# s1.speedUp(50)
# t1=Truck()
# t1.speedUp(100)
# --------------------
# class Car:   #모든 클래스는 object클래스를 상속
#     speed=0
#     def speedUp(self,speed):
#         self.speed=self.speed+speed
#         print("현재 속도(Car)는 %s"% self.speed)
# class Sedan(Car):
#     people=0
#
# class Truck(Car):
#     ton=0
#     def speedUp(self,speed):    #메서드 오버라이딩
#         self.speed=self.speed+speed
#         if self.speed>100:
#             self.speed=100
#         print("현재 속도(Truck)는 %s"% self.speed)
# s1=Sedan()
# s1.speedUp(200)
# s1.people=4
# print(s1.people,s1.speed)
# t1=Truck()
# t1.speedUp(200)
#--------------------------------
class MyClass(object):
    a=2
    def __init__(self,x):
        self.x=x
        print("MyClass의 생성자 호출")
    def mul(self):
        print("MyClass의 mul호출")
        return self.a*self.x

# class MyChild(MyClass):
#     pass

# c1=MyClass(5)
# print(c1.mul())
# c2=MyChild(10)
# print(c2.mul())

# class MyChild(MyClass):
#     a=3
#     def __init__(self,x,y):   #생성자 재정의
#         super().__init__(x)   #부모의 생성자 호출
#         self.y=y
#         print("MyChild의 생성자호출")
#     def mul2(self):
#         print("MyChild의 mul2호출")
#         return self.a*self.x*self.y
#
# c1=MyClass(30)
# print(c1.mul())
# c2=MyChild(50,60)
# print(c2.a, c2.x, c2.y)
# print(c2.mul())
# print(c2.mul2())
# ---
class Line:
    length=0
    def __init__(self,length):
        self.length=length
        print(self.length,"길이의 선이 생성")
    def __del__(self):
        print(self.length,"길이의 선이 제거")
    def __add__(self, other):
        print("__add__호출")
        return self.length+other.length
    def __lt__(self, other):   #less then <
        print("__lt__호출")
        return self.length<other.length
    def __eq__(self, other):  #==
        print("__eq__호출")
        return self.length==other.length
    def __repr__(self):
        print("__repr__호출")
        return "선의길이"+str(self.length)
l1=Line(100)
l2=Line(200)
if l1<l2:
    print("l2가 길어요")
elif l1==l2:
    print("l1,l2가 같아요")
else:
    print("l1이 길어요")
print("선의 합",l1+l2)
print(l1)



























