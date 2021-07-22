from tkinter import *
# def click(event):
#     print("마우스가 클릭됨")
# window=Tk()
# window.geometry("600x500")
# p1=PhotoImage(file="1.gif")
# l1=Label(window,image=p1)
# l1.pack(expand=1,anchor="center")
# # 객체명.bind(이벤트,이벤트처리함수)
# # window.bind("<Button-1>",click)  #왼쪽버튼
# # window.bind("<Button>",click)    #모든버튼
# l1.bind("<Button>",click)
# window.mainloop()
#----------------
# def click(event):
#     msg=""
#     if event.num==1:
#         msg=msg+"왼쪽 버튼 "
#     elif event.num==3:
#         msg=msg+"오른쪽 버튼 "
#     msg=msg+str(event.x)+","+str(event.y)+"에서 클릭됨"
#     print(msg)
# window=Tk()
# window.geometry("600x500")
# # 객체명.bind(이벤트,이벤트처리함수)
# # window.bind("<Button-1>",click)  #왼쪽버튼
# window.bind("<Button>",click)    #모든버튼
# window.mainloop()
#--------------
def keyEvent(event):
    print(chr(event.keycode)+"가 눌러짐")
window=Tk()
window.geometry("600x500")
# window.bind("<Key>",keyEvent)
window.bind("<space>",keyEvent)
window.mainloop()














