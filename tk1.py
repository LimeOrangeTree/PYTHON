from tkinter import *
# window=Tk()
# window.title('윈도우창')
# window.geometry("300x200")
# window.resizable(width=True,height=False)
# window.mainloop()
# ---Label
# window=Tk()
# # Label(윈도우창,옵션)
# label1=Label(window,text="spring~~")
# # label2=Label(window,text="summer",bg="yellow",width=20,anchor=SE)
# label2=Label(window,text="summer",bg="yellow",width=20)
# label3=Label(window,text="겨울이 다갔어요",fg="blue",font=("궁서체",20))
# photo=PhotoImage(file="img\\1.gif")
# label4=Label(window,image=photo)
# label1.pack()
# label2.pack()
# label3.pack()
# label4.pack()
# window.mainloop()
# ---Button
# from tkinter import messagebox
# def f1():
#     messagebox.showinfo('그림버튼','누르셨죠')
# window=Tk()
# btn1=Button(window,text="종료", fg="blue",command=quit)
# photo=PhotoImage(file="img\\1.gif")
# btn2=Button(window,image=photo,command=f1)
# btn1.pack()
# btn2.pack()
# window.mainloop()
#----
# cnt=0
# def plus():
#     global cnt
#     cnt=cnt+1
#     label1.configure(text=str(cnt))
# window=Tk()
# window.title="윈도우 프로그램"
# label1=Label(window,text="0")
# label1.pack()
# btn1=Button(window,text='누르세요',width=20,command=plus)
# btn1.pack()
# window.mainloop()
#----체크버튼
# from tkinter import messagebox
# def f1():
#     if chk.get()==0:
#         messagebox.showinfo("","체크버튼해제")
#     else:
#         messagebox.showinfo("","체크버튼선택")
#
# window=Tk()
# chk=IntVar()
# cb1=Checkbutton(window,text="파랑",command=f1,variable=chk)
# cb1.pack()
# window.mainloop()
#----라디오버튼
def f1():
    if rb.get()==1:
        label1.configure(text="파이쏜")
    elif rb.get()==2:
        label1.configure(text="자바")
    else:
        label1.configure(text="HTML")

window=Tk()
rb=IntVar()
rb1=Radiobutton(window,text="파이썬",variable=rb,command=f1,value=1)
rb2=Radiobutton(window,text="자바",variable=rb,command=f1,value=2)
rb3=Radiobutton(window,text="HTML",variable=rb,command=f1,value=3)
rb.set(2)
label1=Label(window,text="선택값",bg="black",fg='yellow')
rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()
window.mainloop()



