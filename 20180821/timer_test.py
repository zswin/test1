#coding=utf-8
__author__ = 'zs'
import threading
import time

def f_refresh():
#       print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    print('hello')
    global timer1
    timer1 = threading.Timer(2, f_refresh)
    timer1.start()

timer2 = threading.Timer(1,f_refresh)
timer2.start()