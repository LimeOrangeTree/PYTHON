import time

class MyTime(object):
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
    @staticmethod
    def now():
        t=time.localtime()
        # print(t.tm_hour,t.tm_min,t.tm_sec)
        return "{}시 {}분 {}초".format(t.tm_hour,t.tm_min,t.tm_sec)
    @staticmethod
    def hours_later(h):
        t=time.localtime(time.time()+h*60*60)
        return "{}시 {}분 {}초".format(t.tm_hour,t.tm_min,t.tm_sec)

# a=MyTime(9,10,1)
# print(a.h)
print(MyTime.now())
print(MyTime.hours_later(2))
print(MyTime.hours_later(3))
