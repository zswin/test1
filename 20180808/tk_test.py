#coding=utf-8
__author__ = 'zs'
import tkinter

root = tkinter.Tk()
root.title = "this is a title"
root.resizable(1,1)
root.geometry('640x480')
lbl = tkinter.Label(master=root, text = 'This is a label')
lbl.pack()
btn1 = tkinter.Button(master=root, text = 'Button1')
btn1.pack(side = tkinter.LEFT)
root.mainloop()
