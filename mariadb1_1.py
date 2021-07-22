# sqlplus system/dhfkzmf402
# create user happy
#     identified by day;
# grant connect,resource to happy;
# conn happy/day
# select * from tab;
#
# #1)디렉토리 생성
# create directory 디렉토리명 as 경로
# conn system/dhfkzmf402
# grant dba to happy;
# conn happy/day
# create directory source as 'E:\big\pythonStudy\data';
# 2)외부테이블생성(읽기전용)
# create table webtoon_ext(
#     imgurl varchar2(100),
#     title varchar2(50),
#     score varchar2(10),
#     regdate varchar2(15)
# )
# organization external(
#     type oracle_loader
#     default directory source
#     location('webtoon.csv')
# );
#
# 3)테이블 조회
# select * from webtoon_ext;
# if)문제발생시--------------------------
# drop table webtoon_ext;
# create table webtoon_ext(
#     imgurl varchar2(150),
#     title varchar2(50),
#     score varchar2(10),
#     regdate varchar2(15)
# )
# organization external(
#     type oracle_loader
#     default directory source
#     location('webtoon.csv')
# );
# 4)일반테이블 변환
# create table webtoon
#     as
#     select * from webtoon_ext;
# 5)데이터 입력
# insert into webtoon values('abc','abc','10','3-1');
# select * from webtoon;
# select * from tab;
# drop table webtoon_ext;
# kma.csv 를 오라클의 일반 테이블로 만드세요
# --마리아 디비 설치
import pymysql as my
# 연결
# con=my.connect(host='localhost',
#            user='root',
#            password='qwer',
#             db='pythondb',
#             charset='utf8')
# print('연결완료')
# 커서획득
cur=con.cursor()
# 쿼리 실행
if cur:
    sql="select * from kma"
    result=cur.execute(sql)
    print(result)
#  처리
    rows=cur.fetchall()
    for row in rows:
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
cur.close()
con.close()
import pymysql as my
# 1.연결
con=my.connect(host='localhost',
               user='root',
               password='qwer',
               db='pythondb',
               charset='utf8')
# print('연결완료')
# 2.커서획득
cur=con.cursor(my.cursors.DicCursor)
# 3.쿼리실행
if cur:
    sql="select * from kma"
    result=cur.execute(sql)
    # print(result)
# 4.처리
    rows=cur.fetchall()
    print(rows)
    for row in rows:
        print(row['no'], row['province'], row['city'], row['mode1'], row['tmef'], row['wf'], row['tmn'], row['tmx'],row['reliability'])
# 5.연결해제
cur.close()
con.close()
# 값을 입력(input)받아 테이블에 입력하세요
import pymysql as my
import sys
province=input('province=>')
if province=="":
    sys.exit()
city=input('city=>')
mode1=input('mode1=>')
tmef=input('tmef=>')
wf=input('wf=>')
tmn=input('tmn=>')
tmx=input('tmx=>')
reliability=input('reliability=>')

# 1.연결
con=my.connect(host='localhost',
               user='root',
               password='qwer',
               db='pythondb',
               charset='utf8')
# 2.커서획득
cur=con.cursor(my.cursors.DictCursor)
# 커리실행
sql="insert into kma(province,city,mode1,tmef,wf,tmn,tmx,reliability)" "values(%s,%s,%s,%s,%s,%s,%s,%s)"
cur.execute(sql,(province,city,mode1,tmef,wf,tmn,tmx,reliability))
con.commit()
# 5.연결해제
cur.close()
con.close()










