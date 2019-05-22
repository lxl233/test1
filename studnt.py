from tkinter import *
import tkinter.messagebox as mb
with open('.\shige.txt', 'r') as file:
    a = file.read()
    a = a.split('\n')
    for i, j in enumerate(a):
        if j == '':
            a.pop(i)
        else:
            continue
tk=Tk()
tk.geometry('500x500')
tk.title('古诗词默写')
tk.resizable(width=False, height=False)
i=0
def start():
    n.forget
    v.forget
    global i
    i=0
    title.config(text=a[i])
    l1.config(text='')
    l2.config(text='')
    l3.config(text='')
    l4.config(text='')
    disply.config(text='')
def next():
    global i
    i+=5
    title.config(text=a[i])
    l1.config(text='')
    l2.config(text='')
    l3.config(text='')
    l4.config(text='')
    disply.config(text='')

title=Label(tk,text='')
title.place(x=180,y=35)

def verify():
    f1=t1.get()
    f2=t2.get()
    f3=t3.get()
    f4=t4.get()
    if f1==a[i+1] and f2==a[i+2] and f3==a[i+3] and f4==a[i+4]:
        disply.config(text='默写正确')
    else:
        l1.config(text=a[i+1])
        l2.config(text=a[i+2])
        l3.config(text=a[i+3])
        l4.config(text=a[i+4])
l1=Label(tk,text='',width=20)
l1.place(x=280,y=60)
l2=Label(tk,text='',width=20)
l2.place(x=280,y=120)
l3=Label(tk,text='',width=20)
l3.place(x=280,y=180)
l4=Label(tk,text='',width=20)
l4.place(x=280,y=240)
Button(tk,text='开始',command=start).place(x=80,y=450)
n=Button(tk,text='下一题',command=next)
n.place(x=160,y=450)
v=Button(tk,text='验证',command=verify)
v.place(x=250,y=450)
disply=Label(tk,text='')
disply.place(x=10,y=10)
t1=Entry(tk,width=20)
t1.place(x=130,y=60)
t2=Entry(tk,width=20)
t2.place(x=130,y=120)
t3=Entry(tk,width=20)
t3.place(x=130,y=180)
t4=Entry(tk,width=20)
t4.place(x=130,y=240)
tk.mainloop()