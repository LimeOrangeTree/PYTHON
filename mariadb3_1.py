import mariadb2_1

def main():
    work= input('1)조회 2)일괄입력 3)입력 4)삭제 5)일괄삭제 9)종료 => ')
    if work=='9':
        return
    else:
        con,cur=mariadb2.initDB()
        if work=='1':
            mariadb2.selectAll(cur)
        elif work=='2':
            mariadb2.insertAllFromCsv(con, cur)
        elif work == '4':
            city = input('city==> ')
            mariadb2.deleteCity(con, cur, city)
        elif work == '5':
            mariadb2.deleteAll(con, cur)
        mariadb2.freeDB(con, cur)

if __name__=="__main__":
    main()
