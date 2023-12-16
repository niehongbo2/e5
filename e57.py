from tkinter import *
from time import strftime

root = Tk()
root.geometry("300x300")#设置客户端大小
root.resizable(0,0)#设置客户端大小不可变
root.title("Python 时钟")#设置客户端标题

Label(root,text="更多精彩内容\n请关注公众号「python玩转」",font="arial 20 bold",foreground = '#FF6EC7').pack(side=BOTTOM)

def time():
    string = strftime("%H:%M:%S %p")
    mark.config(text=string)
    mark.after(1000,time)#1000ms后再次调用time()函数，即1s后刷新显示

mark = Label(root,font = ('calibri', 40, 'bold'),pady=150,foreground = '#FF7F00')
mark.pack(anchor = 'center')
time()

mainloop()
