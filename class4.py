class HundaiCar:
    count=0
    def __init__(self,m):
        self.model=m    #self.model 인스턴스변수
        self.speed=0
        HundaiCar.count=HundaiCar.count+1   #클래스변수
        print(self.model+"생산되었습니다.")
    def speedUp(self,value):
        self.speed=self.speed+value
    def speedDown(self,value):
        self.speed=self.speed-value

c1=HundaiCar("싼타페")
c2=HundaiCar("코나")
c1.speedUp(30)
print("******",HundaiCar.count)
print("******",c1.count)
print(c1.model,c1.speed)
c3=HundaiCar("소나타")
print("******",c3.count)