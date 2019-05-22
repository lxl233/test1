import random
from tkinter import *
import tkinter.messagebox as mb
#实例tk对象
master = Tk()
#确定程序界面大小
master.geometry('400x300')
master.title('数学运算')
#列表存储两个运算字符
nmber = [0, 0]
#存储运算符号
string = ['+', '-', '*', '/']
#禁止更改界面
master.resizable(width=False, height=False)


# 返回两个随机数且a>b
def get_number():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    if a < b:
        a, b = b, a
        print(a, b)
        nmber[0] = a
        nmber[1] = b
    return nmber


def rand():
    a.set(get_number()[0])
    b.set(get_number()[1])
    char.set(random.choice(string))
    put.set('')
#验证结果
def count():
    string = a.get()
    string += char.get()
    string += b.get()
    try:
        if int(put.get()) == eval(string):
            k.config(text='正确')
            result.forget()
        else:
            k.config(text='错误')
            result.pack()
            result.config(text='答案：'+str(eval(string)))
    except:
        mb.showerror('提示','结果不能为空')
#定义stringvar对象
a = StringVar()
b = StringVar()
char = StringVar()
put=StringVar()
put.set('0')
#设置变量的值
a.set(nmber[0])
b.set(nmber[1])
#随机选取一个运算符
char.set(random.choice(string))
#定义文本框，标签，及按钮
input = Entry(master, textvariable=put, width=5)
input.place(x=140, y=100)
Label(master, textvariable=a).place(x=50, y=100)
Label(master, textvariable=b).place(x=100, y=100)
Label(master, textvariable=char).place(x=80, y=100)
Label(master, text='=').place(x=120, y=100)
k=Label(master,text='')
k.place(x=180,y=180)
#定义一个标签，用来在验证错误时显示答案
result =Label(master,text='')
#开始时隐藏标签
result.forget()
Button(master, text='下一题', command=lambda: rand()).place(x=50, y=250)
Button(master, text='验证', command=count).place(x=200, y=250)
#进入循环，显示程序
master.mainloop()
