from tkinter import *
def f3():
    window.quit()
    window.destroy()
def f1():
    print("메뉴가 선택됨")
window=Tk()
# Menu(부모윈도우)
mainMenu=Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일",menu=fileMenu)
fileMenu.add_command(label="열기",command=f1)
fileMenu.add_command(label="환경설정",command=f1)
fileMenu.add_separator()
fileMenu.add_command(label="종료",command=f3)

editMenu=Menu(mainMenu)
mainMenu.add_cascade(label="글자색",menu=editMenu)
editMenu.add_radiobutton(label="파랑")
editMenu.add_radiobutton(label="노랑")
editMenu.add_radiobutton(label="빨강",state="disable")

viewMenu=Menu(mainMenu)
mainMenu.add_cascade(label="보기",menu=viewMenu)
viewMenu.add_checkbutton(label="상태줄")
viewMenu.add_checkbutton(label="아이콘")
viewMenu.add_checkbutton(label="기타")

window.mainloop()


