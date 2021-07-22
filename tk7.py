from tkinter import *
import mariadb4
def makeScreen(frame,frame2,con,cur):
    valList=[]
    Label(frame,text="기상정보관리",fg="blue",font=("고딕체",20),bg="yellow").\
        grid(column=0,row=0,pady=20,columnspan=3,sticky="e")
    Label(frame,text="번호 :",width=10).grid(column=0,row=1,pady=5)
    Label(frame,text="지역 :",width=10).grid(column=0,row=2,pady=5)
    Label(frame,text="도시 :",width=10).grid(column=0,row=3,pady=5)
    Label(frame,text="모드 :",width=10).grid(column=0,row=4,pady=5)
    Label(frame,text="tmef :",width=10).grid(column=0,row=5,pady=5)
    Label(frame,text="w f :",width=10).grid(column=0,row=6,pady=5)
    Label(frame,text="tmn :",width=10).grid(column=0,row=7,pady=5)
    Label(frame,text="tmx :",width=10).grid(column=0,row=8,pady=5)
    Label(frame,text="reliability :",width=10).grid(column=0,row=9,pady=5)
    # no=Entry(frame,width=10,state="readonly")
    no=Entry(frame,width=10)
    province=Entry(frame,width=10)
    city=Entry(frame,width=10)
    mode1=Entry(frame,width=10)
    tmef=Entry(frame,width=10)
    wf=Entry(frame,width=10)
    tmn=Entry(frame,width=10)
    tmx=Entry(frame,width=10)
    reliability=Entry(frame,width=10)
    no.grid(column=1,row=1)
    province.grid(column=1,row=2)
    city.grid(column=1,row=3)
    mode1.grid(column=1,row=4)
    tmef.grid(column=1,row=5)
    wf.grid(column=1,row=6)
    tmn.grid(column=1,row=7)
    tmx.grid(column=1,row=8)
    reliability.grid(column=1,row=9)
    # valList.append(no)   #자동증가값
    valList.append(province)
    valList.append(city)
    valList.append(mode1)
    valList.append(tmef)
    valList.append(wf)
    valList.append(tmn)
    valList.append(tmx)
    valList.append(reliability)
    msg=Label(frame,text="",width=30,bg="yellow")
    msg.grid(column=1,row=10,columnspan=2)
    Button(frame,text="입력",command=lambda:dbInsert(con,cur,valList,msg),width=7).grid(column=2,row=2,rowspan=2,padx=5)
    Button(frame,text="수정",command=lambda:dbUpdate(con,cur,valList,no,msg),width=7).grid(column=2,row=4,rowspan=2,padx=5)
    Button(frame,text="삭제",command=lambda:dbDelete(con,cur,no,msg),width=7).grid(column=2,row=6,rowspan=2,padx=5)
    Button(frame,text="조회",command=lambda:dbSelect(cur,no,msg,valList),width=7).grid(column=2,row=8,rowspan=2,padx=5)

    rb = IntVar()
    rb1 = Radiobutton(frame2, text="날짜", variable=rb, value=1)
    rb2 = Radiobutton(frame2, text="도시", variable=rb, value=2)
    rb3 = Radiobutton(frame2, text="신뢰도", variable=rb, value=3)
    rb1.select()
    rb1.grid(column=0,row=0)
    rb2.grid(column=1,row=0)
    rb3.grid(column=2,row=0)

    # rb.set(2)
    b1=Button(frame2,text="확인",command=lambda :dbSelectAll(cur,text))
    b1.grid(column=3,row=0)
    text=Text(frame2)
    text.place(x=3,y=30)
def dbSelectAll(cur,text):
    text.delete("1.0",END)  #행번호.열번호:행은 1부터,열은 0부터 시작
    # text.delete(0,100)
    # try:
    rows = mariadb4.selectAll(cur)
    # rows = mariadb4.selectAll(cur,rb.get())
    text.insert("1.0","no\t지역\t도시\t모드\ttmef\twf\ttmn\ttmx\t신뢰도\n")
    # text.insert(INSERT,"no\t지역\t도시\t모드\ttmef\twf\ttmn\ttmx\t신뢰도\n")
    for row in rows:
        str="{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format\
            (row['no'],row['province'],row['city'],row['mode1'],row['tmef'],row['wf'],row['tmn'],row['tmx'],row['reliability'])
        # print(text.get(1,2))
        text.insert(INSERT,str)
        print("조회완료")

def dbDelete(con,cur,no,msg):
    txt="삭제성공"
    temp=[]
    try:
        temp.append(no.get())
        mariadb4.delete(con,cur,no.get())
    except:
        txt = "삭제실패"
    finally:
        msg.configure(text=txt)
def dbUpdate(con,cur,valList,no,msg):
    txt="수정성공"
    temp=[]
    try:
        for i in valList:
            temp.append(i.get())
        temp.append(no.get())
        mariadb4.update(con,cur,temp)
        for c in valList:
            c.delete(0,5)
    except:
        txt = "수정실패"
    finally:
        msg.configure(text=txt)
def dbSelect(cur,no,msg,valList):
    txt="조회성공"
    try:
       row=mariadb4.select(cur,no.get())
       valList[0].insert(0,row['province'])
       valList[1].insert(0,row['city'])
       valList[2].insert(0,row['mode1'])
       valList[3].insert(0,row['tmef'])
       valList[4].insert(0,row['wf'])
       valList[5].insert(0,row['tmn'])
       valList[6].insert(0,row['tmx'])
       valList[7].insert(0,row['reliability'])
    except:
        txt = "조회실패"
    finally:
        msg.configure(text=txt)
def dbInsert(con,cur,valList,msg):
    txt = "입력성공"
    try:
        temp=[]
        for val in valList:
            temp.append(val.get())
        mariadb4.insert(con,cur,temp)
        for c in valList:
            c.delete(0,5)
    except:
        txt = "입력실패"
    finally:
        msg.configure(text=txt)
        valList[0].focus()
def main():
    window=Tk()
    window.geometry("800x400")
    # window.resizable(False,False)
    leftFrame=Frame(window,bd=2,relief="solid")
    leftFrame.pack(side="left",fill="both",expand=True)
    rightFrame=Frame(window,bd=2,relief="solid")
    rightFrame.pack(side="left",fill="both",expand=True)
    try:
        con,cur=mariadb4.initDB()
        makeScreen(leftFrame,rightFrame,con,cur)
        # mariadb4.freeDB(con,cur)
    except:
        print("오류")
    window.mainloop()

if __name__=="__main__":
    main()