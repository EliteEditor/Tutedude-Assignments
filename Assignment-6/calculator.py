import tkinter as tk
from tkinter import ttk
from tkinter import *

window = tk.Tk()
window.title("Calculator")
window.geometry("500x500")

e = tk.Entry(window,width=56,border=4)
e.place(x=0,y=0)
def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))
    
b = ttk.Button(text="1",width=12,command=lambda:click(1))
b.place(x = 10,y=60)
b = ttk.Button(text="2",width=12,command=lambda:click(2))
b.place(x = 100,y=60)
b = ttk.Button(text="3",width=12,command=lambda:click(3))
b.place(x = 190,y=60)
b = ttk.Button(text="4",width=12,command=lambda:click(4))
b.place(x = 10,y=100)
b = ttk.Button(text="5",width=12,command=lambda:click(5))
b.place(x = 100,y=100)
b = ttk.Button(text="6",width=12,command=lambda:click(6))
b.place(x = 190,y=100)
b = ttk.Button(text="7",width=12,command=lambda:click(7))
b.place(x = 10,y=140)
b = ttk.Button(text="8",width=12,command=lambda:click(8))
b.place(x = 100,y=140)
b = ttk.Button(text="9",width=12,command=lambda:click(9))
b.place(x = 190,y=140)
b = ttk.Button(text="0",width=12,command=lambda:click(0))
b.place(x = 10,y=180)
def add():
    n1 = e.get()
    global i
    global math
    math = "addition"
    i = int(n1)
    e.delete(0,END)
b = ttk.Button(text="+",width=12,command=add)
b.place(x = 100,y=180)
def sub():
    n1 = e.get()
    global i
    global math
    math = "subtraction"
    i = int(n1)
    e.delete(0,END)
b = ttk.Button(text="-",width=12,command=sub)
b.place(x = 190,y=180)
def mul():
    n1 = e.get()
    global i
    global math
    math = "multiplication"
    i = int(n1)
    e.delete(0,END)
b = ttk.Button(text="*",width=12,command=mul)
b.place(x = 10,y=220)
def div():
    n1 = e.get()
    global i
    global math
    math = "division"
    i = int(n1)
    e.delete(0,END)
b = ttk.Button(text="/",width=12,command=div)
b.place(x = 100,y=220)
def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,i+int(n2))
    elif math == "subtraction":
        e.insert(0,i-int(n2))
    elif math == "multiplication":
        e.insert(0,i*int(n2))
    elif math == "division":
        e.insert(0,i/int(n2))
b = ttk.Button(text="=",width=12,command=equal)
b.place(x = 190,y=220)
def clear():
    e.delete(0,END)
b = ttk.Button(text="Clear",width=12,command=clear)
b.place(x = 10,y=260)



window.mainloop()