import pymysql as my
import requests
from bs4 import BeautifulSoup
def initDB():
    con=my.connect(host='localhost',
                   user='root',
                   password='1234',
                   db='pythondb',
                   charset='utf8')
    cur=con.cursor(my.cursors.DictCursor)
    print("연결성공")
    return con,cur
def insert(con,cur,temp):
    sql="insert into kma (province,city,mode1,tmef,wf,tmn,tmx,reliability)" \
        " values (%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql, (temp))
    con.commit()
def select(cur,no):
    sql="select * from kma where no=%s"
    cur.execute(sql,(no))
    row=cur.fetchone()
    return row
def selectAll(cur):
    if cur:
        sql="select * from kma"
        result=cur.execute(sql)
        rows=cur.fetchall()
        # print(rows)
        return rows
def insertAllFromCsv(con,cur):
    sql="insert into kma (province,city,mode1,tmef,wf,tmn,tmx,reliability)" \
        " values (%s,%s,%s,%s,%s,%s,%s,%s)"
    with open('data\\kma.csv',encoding='utf-8') as f:
        for line in f:
            # print(line)
            line=line.replace("\n","")
            line=line.split(',')    #리스트
            # cur.execute\
            #     (sql,(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]))
            cur.execute(sql,(line))
        con.commit()
def insertAllSearch(con,cur):
    sql="insert into kma (province,city,mode1,tmef,wf,tmn,tmx,reliability)" \
        " values (%s,%s,%s,%s,%s,%s,%s,%s)"
    url="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
    result=requests.get(url)
    dom=BeautifulSoup(result.text,'lxml')
    locationdom=dom.find_all('location')
    for location in locationdom:
        province=location.find('province')
        city=location.find('city')
        datadom=location.find_all('data')
        for data in datadom:
            mode=data.find('mode')
            tmEf=data.find('tmef')
            wf=data.find('wf')
            tmn=data.find('tmn')
            tmx=data.find('tmx')
            reliability=data.find('reliability')
            cur.execute\
                (sql,(province.text,city.text,mode.text,tmEf.text,wf.text,tmn.text,tmx.text,reliability.text))
        con.commit()
def deleteCity(con,cur,city):
    sql="delete from kma where city=%s"
    cur.execute(sql,(city))
    con.commit()
    print("**"+city+"삭제완료")
def delete(con,cur,no):
    sql="delete from kma where no=%s"
    cur.execute(sql,(no))
    con.commit()
    print("삭제완료")
def deleteAll(con,cur):
    sql="delete from kma"
    cur.execute(sql)
    con.commit()
    print("삭제완료")
def update(con,cur,dataList):
    sql="update kma set province=%s,city=%s,mode1=%s,tmef=%s,wf=%s,tmn=%s,tmx=%s,reliability=%s where no=%s"
    cur.execute(sql,(dataList))
    con.commit()
def updateCity(con,cur,dataList):
    # print(dataList)
    sql="update kma set wf=%s,tmn=%s,tmx=%s where city=%s"
    cur.execute(sql,(dataList[1],dataList[2],dataList[3],dataList[0]))
    con.commit()
def freeDB(con,cur):
    cur.close()
    con.close()
    print("연결해제")

