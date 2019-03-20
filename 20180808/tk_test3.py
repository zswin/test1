#coding=utf-8
__author__ = 'zs'

from tkinter import *

# 初始化Tk()
myWindow = Tk()
# 设置标题
myWindow.title('Python GUI Learning')
# 设置窗口大小
width = 380
height = 300
# 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = myWindow.winfo_screenwidth()
screenheight = myWindow.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
myWindow.geometry(alignstr)
# 设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=False, height=True)

# 框架布局
frame_root = Frame(myWindow)
frame_l = Frame(frame_root)
frame_r = Frame(frame_root)
# 创建一个标签，并在窗口上显示
Label(frame_l, text="中国", bg="green", font=("Arial", 12), width=10, height=2).pack(side=TOP)
Label(frame_l, text="日本", bg="green", font=("Arial", 12), width=10, height=2).pack(side=TOP)
Label(frame_r, text="美国", bg="green", font=("Arial", 12), width=10, height=2).pack(side=TOP)
Label(frame_r, text="韩国", bg="green", font=("Arial", 12), width=10, height=2).pack(side=TOP)
Label(frame_root, text = '这是一个测试', bg='blue',fg='white', font=('Arial', 12), width=10, height = 2).pack(side=RIGHT)
Button(frame_root, command=quit, text = 'OK', bg='black', fg='white', highlightbackground='green', activebackground='white', activeforeground='black').pack(side=BOTTOM)
# 框架的位置布局
frame_l.pack(side=LEFT)
frame_r.pack(side=RIGHT)
frame_root.pack()

# 进入消息循环
myWindow.mainloop()
