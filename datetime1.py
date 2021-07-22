# import time
#
# print(time.time())
# print(round(time.time()))
# time.sleep(3)
# print(time.time()+5)
# print(time.ctime())
# print(time.localtime())
# print(time.gmtime())
# print(time.asctime())

# import datetime
# date:년월일
# time:시분초마이크로초
# datetime:날짜와시간
# timedelta:날짜와 시간간격
# from datetime import date
# white=date(2019,3,14)
# print(white)
# print(white.year)
# print(white.month)
# print(white.day)
# print(white.isoformat())

# from datetime import time
# bedtime=time(23,30,1)
# print(bedtime)
# print(bedtime.hour)
# print(bedtime.minute)
# print(bedtime.second)

import datetime
# someday=datetime.datetime(2030,2,14,9,30,1)
# print(someday)
# print(someday.isoformat())
# now=datetime.datetime.now()
# print(now)
# dday=datetime.timedelta(days=3)
# print(now+dday)
# print(now+datetime.timedelta(weeks=1,days=1,hours=1,minutes=1,seconds=1))
someday=datetime.datetime(2019,3,14,9,40,0)
print(someday)
print(someday.strftime("%Y/%m/%d %H:%M:%S"))
print(someday.strftime("%y/%m/%d %H:%M:%S"))
print(someday.strftime("%I:%M %p"))
print(someday.strftime("%B of %y"))