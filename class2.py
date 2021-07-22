# 1.클래스 정의
# 2.클래스 변수 생성
# 3.사용
# class Tv:
#     color=""
#     channel=0
#     power=False
#     def powerOn(self):
#         self.power=True
#     def powerOff(self):
#         self.power=False
#     def channelUp(self):
#         if self.power:
#             self.channel=self.channel+1
#             if self.channel>99:
#                 self.channel=1
#     def channelDown(self):
#         if self.power:
#             self.channel=self.channel-1
#             if self.channel<1:
#                 self.channel=1
#     def channelChange(self,value):
#         if self.power:
#             self.channel=value
# t1=Tv()
# t2=Tv()
# t1.color='black'
# t1.powerOn()
# t1.channelUp()
# t1.channelUp()
# t1.channelUp()
# print("{},{},{}".format(t1.color,t1.power,t1.channel))
# t2.channelChange(50)
# print("{},{},{}".format(t2.color,t2.power,t2.channel))

# 시계
# 전원,시,분,초
# 시간설정하다
# 전원을 넣다
# 전원을 끄다
class Clock:
    hour=0
    minute=0
    second=0
    power=True
    def powerOn(self):
        self.power=True
    def powerOff(self):
        self.power=False
    def setHour(self,h):
        if h>=0 and h<25:
            self.hour=h
    def setMinute(self,m):
        if m>=0 and m<60:
            self.minute=m
    def setSecond(self,s):
        if s>=0 and s<60:
            self.second=s
    def printMessage(self):
        print("전원{},{}:{}:{}".format(self.power,self.hour,self.minute,self.second))

c1=Clock()
c1.setHour(11)
c1.setMinute(20)
c1.setSecond(30)
c1.printMessage()












