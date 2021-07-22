import pymysql as my
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
    sql="insert into member (userid,name,pw,hp,city) values (%s,%s,%s,%s,%s)"
    cur.execute(sql, (temp))
    con.commit()
def update(con,cur,temp):
    sql="update member set name=%s,pw=%s,hp=%s,city=%s where userid=%s"
    cur.execute(sql, (temp))
    con.commit()
def delete(con,cur,userid):
    sql="delete from member where userid=%s"
    cur.execute(sql, (userid))
    con.commit()
def select(cur,userid):
    sql="select * from member where userid=%s"
    cur.execute(sql,(userid))
    row=cur.fetchone()
    return row
def selectAll(cur,gubun):
    if gubun==1:
        sql="select * from member order by userid"
    elif gubun==2:
        sql="select * from member order by name"
    else:
        sql="select * from member order by city"
    cur.execute(sql)
    rows=cur.fetchall()
    return rows
def freeDB(con,cur):
    cur.close()
    con.close()
    print("연결해제")