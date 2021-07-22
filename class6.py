# x=100
# class MyClass:
#     i=10
#     x+=2     #x=102
#     xx=x+2   #xx=104
#     print('xx=',xx)
#     def price(self):
#         y=self.i*x       #10*100
#         z=self.i*self.x  #10*102
#         print("price y=",y)
#         print("price z=",z)
#     def shop(self):
#         print("shop")
#         self.price()
#         # MyClass.price()
#
# if __name__=="__main__":
#     a=MyClass()
#     a.shop()
# ==추상메서드의 사용
# class Mammal:
#     def eat(self):      #하위클래스에서 재정의사용
#         pass
# class People(Mammal):
#     def eat(self):
#         print("사람은 잡식성")
# class Dog(Mammal):
#     pass
# p1=People()
# d1=Dog()
# p1.eat()
# d1.eat()
# -------------
# class Mammal:
#     def eat(self):      #추상메서드 하위클래스에서 재정의사용
#         raise NotImplementedError()
#     def sleep(self):
#         print("포유류는 잠을 잔다")
# class People(Mammal):
#     def eat(self):
#         print("사람은 잡식성")
# class Dog(Mammal):
#     def eat(self):
#         print("강아지는 사료를 먹는다.")
# p1=People()
# d1=Dog()
# p1.eat()
# p1.sleep()
# d1.eat()
# d1.sleep()
# 클래스메서드:클래스명.메서드명 ----
class MyClass(object):
    x=1
    @classmethod      #mul을 클래스메서드로 지정
    def mul(cls,y):
        return cls.x*y
class MyChild(MyClass):
    x=3
print(MyClass.mul(7))
# a=MyClass()
# print(a.mul(5))
print(MyChild.mul(5))
# 스태틱메서드:객체를 만들지 않아도 됨,a=MyCalc() X
class MyCalc:
    @staticmethod
    def my_add(x,y):
        return x+y
    @staticmethod
    def my_sub(x,y):
        return x-y
    @staticmethod
    def my_mul(x,y):
        return x*y
    @staticmethod
    def my_div(x,y):
        return x/y

print(MyCalc.my_add(1000,5))
print(MyCalc.my_sub(1000,5))
print(MyCalc.my_mul(1000,5))
print(MyCalc.my_div(1000,5))



