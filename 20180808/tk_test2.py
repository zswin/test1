#coding=utf-8
__author__ = 'zs'
from tkinter import *

root = Tk()
strVar = StringVar()
strVar.set("test1")
def handler():
    strVar.set("WTF")
btn1 = Button(root, textvariable = strVar)
btn1.pack()
btn2 = Button(root, text = 'Change btn1', command = handler)
btn2.pack()
root.mainloop()
