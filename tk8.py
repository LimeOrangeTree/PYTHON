# 1.테이블생성
# CREATE TABLE `member` (
# 	`no` INT NOT NULL AUTO_INCREMENT,
# 	`userid` VARCHAR(50) NOT NULL,
# 	`name` VARCHAR(50) NULL,
# 	`pw` VARCHAR(50) NULL,
# 	`hp` VARCHAR(50) NULL,
# 	`city` VARCHAR(50) NULL,
# 	PRIMARY KEY (`no`),
# 	UNIQUE INDEX `userid` (`userid`)
# )
# COLLATE='utf8_general_ci'
# ;
import mariadb5
from tkinter import *
class GUI(Tk):
    def __init__(self,con,cur):
        super().__init__()
        self.con=con
        self.cur=cur
        frame1=Frame(self)
        frame1.pack(fill="both",expand=True)
        Label(frame1,text="회원관리",fg="blue",font=("고딕체",20),bg="yellow").\
            grid(column=0,row=0,pady=20,columnspan=3,sticky="e")
        Label(frame1,text="아이디 :",width=10).grid(column=0,row=1,pady=5)
        Label(frame1,text="이름 :",width=10).grid(column=0,row=2,pady=5)
        Label(frame1,text="비밀번호 :",width=10).grid(column=0,row=3,pady=5)
        Label(frame1,text="연락처 :",width=10).grid(column=0,row=4,pady=5)
        Label(frame1,text="도시 :",width=10).grid(column=0,row=5,pady=5)
        self.userid=StringVar()
        self.name=StringVar()
        self.pw=StringVar()
        self.hp=StringVar()
        self.city=StringVar()
        self.msg=StringVar()
        Entry(frame1,width=20,textvariable=self.userid).grid(column=1,row=1,pady=5)
        Entry(frame1,width=20,textvariable=self.name).grid(column=1,row=2,pady=5)
        Entry(frame1,width=20,textvariable=self.pw).grid(column=1,row=3,pady=5)
        Entry(frame1,width=20,textvariable=self.hp).grid(column=1,row=4,pady=5)
        Entry(frame1,width=20,textvariable=self.city).grid(column=1,row=5,pady=5)
        Label(frame1,width=20,textvariable=self.msg,bg="yellow").grid(column=3,row=6,pady=5)
        Button(frame1,text="입력",command=self.dbInsert).grid(column=1,row=7,pady=5)
        Button(frame1,text="수정",command=self.dbUpdate).grid(column=2,row=7,pady=5)
        Button(frame1,text="삭제",command=self.dbDelete).grid(column=3,row=7,pady=5)
        Button(frame1,text="조회",command=self.dbSelect).grid(column=0,row=7,pady=5)
        # Button(frame1,text="전체조회",command=self.dbSelectAll).grid(column=4,row=7,pady=5)

        # frame2=Frame(self)
        # frame2.pack(fill="both",expand=True)
        self.rb=IntVar()
        # self.rb.set(2)
        rb1=Radiobutton(frame1,text="아이디",variable=self.rb, value=1)
        rb2=Radiobutton(frame1,text="이름",variable=self.rb, value=2)
        rb3=Radiobutton(frame1,text="주소",variable=self.rb, value=3)
        rb1.select()
        rb1.grid(column=1,row=10,pady=5)
        rb2.grid(column=2,row=10,pady=5)
        rb3.grid(column=3,row=10,pady=5)
    def dbSelectAll(self):
        pass
    def dbSelect(self):
        try:
            row=mariadb5.select(self.cur,self.userid.get())
            self.userid.set(row['userid'])
            self.name.set(row['name'])
            self.pw.set(row['pw'])
            self.hp.set(row['hp'])
            self.city.set(row['city'])
            self.msg.set("조회성공")
        except:
            self.msg.set("해당아이디가 없습니다.")
    def dbDelete(self):
        print("**"+self.userid.get()+"**")
        try:
            mariadb5.delete(self.con,self.cur,self.userid.get())
            self.userid.set("")
            self.name.set("")
            self.pw.set("")
            self.hp.set("")
            self.city.set("")
            self.msg.set("삭제완료")
        except:
            self.msg.set("삭제실패")
    def dbUpdate(self):
        temp=[]
        temp.append(self.name.get())
        temp.append(self.pw.get())
        temp.append(self.hp.get())
        temp.append(self.city.get())
        temp.append(self.userid.get())
        try:
            mariadb5.update(self.con,self.cur,temp)
            self.userid.set("")
            self.name.set("")
            self.pw.set("")
            self.hp.set("")
            self.city.set("")
            self.msg.set("수정완료")
        except:
            self.msg.set("수정실패")
    def dbInsert(self):
        temp=[]
        temp.append(self.userid.get())
        temp.append(self.name.get())
        temp.append(self.pw.get())
        temp.append(self.hp.get())
        temp.append(self.city.get())
        try:
            mariadb5.insert(self.con,self.cur,temp)
            self.userid.set("")
            self.name.set("")
            self.pw.set("")
            self.hp.set("")
            self.city.set("")
            self.msg.set("입력완료")
        except:
            self.msg.set("입력실패")
def main():
    con,cur=mariadb5.initDB()   #db연결
    window=GUI(con,cur)
    window.geometry("400x400")

    window.mainloop()
if __name__=="__main__":
    main()

