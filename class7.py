# class Test:
#     @staticmethod
#     def t1():
#         print("t1메서드")
#     @staticmethod
#     def t2():
#         print("t2메서드")
#     def t3(self):   #일반메서드
#         print("t3메서드")
# Test.t1()
# Test.t2()
# # Test.t3()
# a=Test()
# a.t3()
# 인스턴스확인 isinstance()
# class Student:
#     def __init__(self,name,kor,eng,mat):
#         self.name=name
#         self.kor=kor
#         self.eng=eng
#         self.mat=mat
#     def getTot(self):
#         return self.kor+self.eng+self.mat
#     def getAvg(self):
#         return self.getTot()/3
#     def toString(self):
#         return "{}는 총점:{} 이고 평균:{} 입니다.".format\
#             (self.name,self.getTot(),self.getAvg())

# s1=Student('홍길동',88,77,99)
# print(s1.toString())
# students=[Student('콩쥐',80,70,90),Student('팥쥐',70,60,77),Student('심청',55,70,90)]
# # a=[1,2,3]
# for student in students:   #student=students[0],students[1],...
#     print(student.toString())

# class Teacher:
#     def teach(self):
#         print("수업합니다.")
# class Student:
#     def study(self):
#         print("공부합니다.")
# persons=[Student(),Student(),Teacher(),Student(),Teacher()]
# # 인스턴스확인 isinstance(객체변수,클래스명)
# for person in persons:
#     if isinstance(person,Student):
#         person.study()
#     else:
#         person.teach()
# # 멀티쓰레드------------------
# import threading
# import time
# class Car:
#     def __init__(self,name):
#         self.name=name
#     def run(self):
#         for _ in range(5):
#             print(self.name+' 달립니다.~~')
#             time.sleep(0.1)   #0.1초 멈춤
# c1=Car('산타페')
# c2=Car('그랜져')
# c3=Car('퓨마')
# # c1.run()
# # c2.run()
# # c3.run()
# # --스레드생성
# t1=threading.Thread(target=c1.run)
# t2=threading.Thread(target=c2.run)
# t3=threading.Thread(target=c3.run)
# # --스레드 실행
# t1.start()
# t2.start()
# t3.start()

# 멀티프로세싱------------------
import multiprocessing
import time
class Car:
    def __init__(self,name):
        self.name=name
    def run(self):
        for _ in range(5):
            print(self.name+' 달립니다.~~')
            time.sleep(0.1)   #0.1초 멈춤
if __name__=="__main__":
    c1=Car('산타페')
    c2=Car('그랜져')
    c3=Car('퓨마')
    m1=multiprocessing.Process(target=c1.run)
    m2=multiprocessing.Process(target=c2.run)
    m3=multiprocessing.Process(target=c3.run)
    m1.start()
    m2.start()
    m3.start()









