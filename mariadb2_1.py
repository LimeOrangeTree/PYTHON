import pymysql as my
def initDB():
    con = my.connect(host='localhost',
                     user='root',
                     password='qwer',
                     db='pythondb',
                     charset='utf8')
    cur = con.cursor(my.cursors.DictCursor)
    print("연결성공")
    return con,cur

def insert(con,cur):
    print("입력성공")
def selectAll(cur):
    if cur:
        sql="select * from kma"
        result=cur.execute(sql)
        rows=cur.fetchall()
        # print(rows)
        cnt=0
        for row in rows:
            cnt=cnt+1
            print(cnt,row['province'],row['city'],row['mode1'],
                row['tmef'],row['wf'],row['tmn'],row['tmx'],row['reliability'])
def insertAllFromCsv(con,cur):
    sql = "insert into kma (province,city,mode1,tmef,wf,tmn,tmx,reliability)" \
          " values (%s,%s,%s,%s,%s,%s,%s,%s)"
    with open('data\\kma.csv',encoding='utf-8') as f:
        for line in f:
            # print(line)
            line.replace("\n","")
            line=line.split(',')
            # print(line)
            # sql = "insert into kma (province,city,mode1,tmef,wf,tmn,tmx,reliability)" \
            #       " values (%s,%s,%s,%s,%s,%s,%s,%s)"
            # cur.execute(sql,(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]))
            cur.execute(sql,(line))
        con.commit()
def deleteCity(con,cur,city):
    sql="delete from kma where city=%s"
    cur.execute(sql,(city))
    con.commit()
    print("**"+city+"삭제완료")
def deleteAll(con,cur):
    sql="delete from kma"
    cur.excute(sql)
    con.commit()
    print("삭제완료")
def freeDB(con,cur):
    cur.close()
    con.close()
    print("연결해제")