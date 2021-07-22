# from tkinter import *
# def func1(e):
#     print(1)
#     print(province.get())
# window=Tk()
# window.geometry("400x400")
# # 프레임:위젯들 포함
# leftFrame=Frame(window,bd=2,relief="solid")
# leftFrame.pack(side="top",fill="both",expand=True)
# Label(leftFrame,text="지역 ").pack()
# # entry:텍스트를 입력 또는 출력
# province=Entry(leftFrame)
# province.bind("<Return>",func1)
# province.pack()
#
# rightFrame=Frame(window,bd=2,relief="solid")
# rightFrame.pack(side="top",fill="both",expand=True)
# Button(rightFrame,text="확인").pack()
# # 여러줄 문자열 출력
# text=Text(rightFrame)
# text.pack()
# text.insert(INSERT,"hi\n")
# text.insert(INSERT,"haha")
# text.insert(INSERT,"haha")
# window.mainloop()

from tkinter import *

class test:
    def __init__(self):
        wind = Tk()

        frame1 = Frame(wind)
        frame1.pack()
        self.v1 = IntVar()
        self.v2 = StringVar()

        int1 = Radiobutton(frame1, text = 'int1', variable = self.v1, value = 1, command = self.ipress)
        int2 = Radiobutton(frame1, text = 'int2', variable = self.v1, value = 2, command = self.ipress)

        str1 = Radiobutton(frame1, text = 'str1', variable = self.v2, value = '1', command = self.spress)
        str2 = Radiobutton(frame1, text = 'str2', variable = self.v2, value = '2', command = self.spress)

        int1.grid(row = 1, column = 1)
        int2.grid(row = 1, column = 2)

        str1.grid(row = 2, column = 1)
        str2.grid(row = 2, column = 2)

        str1.deselect() #this didn't fix it
        str2.deselect()

    def ipress(self):
        print('int'+str(self.v1.get()))
    def spress(self):
        print('str'+self.v2.get())

test()