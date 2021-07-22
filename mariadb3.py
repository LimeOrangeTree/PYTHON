import mariadb2

def main():
    con, cur = mariadb2.initDB()  # db연결
    while True:
        work=input('1)조회 2)일괄입력 3)검색입력 4)삭제 5)일괄삭제 6)수정 9)종료')
        if work=='9':
            break
        elif work=='1':
            mariadb2.selectAll(cur)
        elif work=='2':
            mariadb2.insertAllFromCsv(con, cur)
        elif work=='3':
            mariadb2.insertAllSearch(con, cur)
        elif work=='4':
            city=input('city==>')
            mariadb2.deleteCity(con,cur,city)
        elif work=='5':
            mariadb2.deleteAll(con,cur)
            # delete from kma
        elif work=="6": #도시를 입력받아 wf,tmn,tmx 수정
            city=input('city==>')
            wf=input('wf==>')
            tmn=input('tmn==>')
            tmx=input('tmx==>')
            dataList=[]
            dataList.append(city)
            dataList.append(wf)
            dataList.append(tmn)
            dataList.append(tmx)
            mariadb2.updateCity(con,cur,dataList)
    #       update kma set wf='맑음',tmn=5,tmx=15 where city='서울'
    mariadb2.freeDB(con,cur)
if __name__=="__main__":
    main()