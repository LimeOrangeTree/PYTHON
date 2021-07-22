# from tkinter import *
# from tkinter.simpledialog import *
# window=Tk()
# window.geometry("300x200")
# l1=Label(window,text="값=",bg="yellow", width=200)
# l1.pack()
# n=askinteger("주사위","던지세요",minvalue=1,maxvalue=6)
# l1.configure(text="값은 "+str(n))
# window.mainloop()
#------------------
# from tkinter import *
# from tkinter.filedialog import *
# window=Tk()
# window.geometry("600x500")
# l1=Label(window,text="값=",bg="yellow", width=200)
# l1.pack()
# photo=PhotoImage(file="1.gif")
# l2=Label(window,image=photo)
# l2.pack(expand=1,anchor=CENTER)
# filename=askopenfilename(parent=window,
#         filetypes=(("gif파일","*.gif"),("모든파일","*.*")))
# l1.configure(text="값은 "+filename)
# photo=PhotoImage(file=filename)
# l2.configure(image=photo)
# window.mainloop()
# 실습
# 1.윈도우 크기를 400x400 으로 하고 창 제목은 Python Study
# 2.파일메뉴를 만들고 하위메뉴로 파일열기,종료 작성
    # 파일열기 선택되면  fileOpen 함수 수행
    # 종료 선택되면 pgEnd 함수 수행
    # fileOpen 함수-askopenfilename()창 생성
    # pgEnd 함수- 프로그램 종료
# 3.화면구성
#   취미선택      <--라벨
#      독서     <--라디오
#      수영     <--라디오
#      등산     <--라디오
#   확인        <--버튼
from tkinter import *
from tkinter.filedialog import *
def fileOpen(window,photo,l1):
        filename=askopenfilename\
                (parent=window,filetypes=(("gif파일","*.gif"),("모든파일","*.*")))
        # print(filename)
        photo.configure(file=str(filename))
        l1.configure(image=photo)
def pgEnd(window):
        window.quit()
        window.destroy()
def makeMenu(window,photo,l1):
        mainMenu=Menu(window)
        window.config(menu=mainMenu)
        fileMenu=Menu(mainMenu)
        mainMenu.add_cascade(label="파일",menu=fileMenu)
        fileMenu.add_command(label="열기",command=lambda:fileOpen(window,photo,l1))
        fileMenu.add_separator()
        fileMenu.add_command(label="종료",command=lambda:pgEnd(window))
def showPhoto(hobby,l1,photo):
        if hobby==1:
                photo.configure(file="a1.png")
        elif hobby==2:
                photo.configure(file="a1.png")
        else:
                photo.configure(file="1.gif")
        l1.configure(image=photo)
def makeScreen(window):
        Label(window,text="취미를 선택하세요",fg="blue",font=("고딕체",20)).pack(pady=10)
        hobby=IntVar()
        rb1=Radiobutton(window,text="독서",variable=hobby,value=1)
        rb2=Radiobutton(window,text="수영",variable=hobby,value=2)
        rb3=Radiobutton(window,text="등산",variable=hobby,value=3)
        rb1.pack(padx=5,pady=5)
        rb2.pack(padx=5,pady=5)
        rb3.pack(padx=5,pady=5)
        photo= PhotoImage(file="1.gif")
        l1=Label(window,width=300,height=200,bg="pink",image=None)
        Button(window,text="확인",command=lambda:showPhoto(hobby.get(),l1,photo)).pack(padx=5,pady=5)
        l1.pack(padx=5,pady=5)
        return photo,l1
def main():
        window=Tk()
        window.geometry("500x500")
        window.title("Python Study")
        photo,l1=makeScreen(window)
        makeMenu(window,photo,l1)
        window.mainloop()
if __name__=="__main__":
        main()

