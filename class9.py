import datetime
import os
class Address:
    persons=[]
    def add(self,person):
        self.persons.append(person)
    def showAll(self):
        for p in self.persons:  #p=self.persons[0],self.persons[1],...
            print(p.lastname,p.firstname,p.tel,p.email,p.birthday)
    def insertAll(self):
        with open(os.path.join('data', 'person.csv'), 'r', encoding='utf-8') as f:
            cnt = 0
            for line in f:
                if cnt == 0:   #제목줄제거
                    cnt = 1
                    continue
                # print(line)
                line=line.replace("\n","")
                l=line.split(',')  #리스트로변환
                # print(l)
                p=Person(l[0],l[1],l[4])
                p.setEmail(l[2])
                p.setBirthday(l[3])
                self.add(p)
    def search(self,keyword):
        for p in self.persons:
            if p.lastname==keyword:
                print(p.lastname, p.firstname, p.tel, p.email, p.birthday)
    def searchAll(self,kind,keyword):
        if kind=='tel':
            for p in self.persons:
                if keyword in p.tel:
                    print(p.lastname, p.firstname, p.tel, p.email, p.birthday)
        elif kind=='firstname':
            for p in self.persons:
                if keyword in p.firstname:
                    print(p.lastname, p.firstname, p.tel, p.email, p.birthday)
    def deleteAll(self):
        self.persons.clear()
class Person:
    email=""
    birthday=""
    def __init__(self,lastname,firstname,tel):
        self.lastname=lastname
        self.firstname=firstname
        self.tel=tel
    def setEmail(self,email):
        self.email=email
    def setBirthday(self,birthday):
        self.birthday=birthday
#---------------------------------------
a=Address()
a.insertAll()
a.showAll()
print('-'*30)
a.search('이')
print('-'*30)
a.searchAll('tel','1284')
print('-'*30)
a.searchAll('firstname','만')
print('-'*30,'삭제')
a.deleteAll()
a.showAll()
# ----------------------------
# p1=Person('강','감찬','123-4567')
# p1.setEmail('kang@abc.com')
# p2=Person('강','가딘','456-7890')
# a=Address()  #주소록 생성
# a.add(p1)
# a.add(p2)
# a.showAll()
# p3=Person('이','몽룡','456-7890')
# a.add(p3)
# a.showAll()
# data\person.csv를 읽어서 출력(단,제목줄제외)
# with open(os.path.join('data', 'person.csv'), 'r', encoding='utf-8') as f:
#     cnt = 0
#     for line in f:
#         if cnt == 0:
#             cnt = 1
#             continue
#         print(line)
#         l=line.split(',')
#         print(l[3])



















