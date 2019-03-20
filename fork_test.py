#coding=utf-8
__author__ = 'zs'
import os
print('current process(%s) start ...'%(os.getpid()))
pid = os.fork()
if pid < 0:
    print('error in fork')
elif pid == 0:
    print("I'm a child process(%s), parent process is (%s)"%(os.getpid(), os.getppid()))
else:
    print("I'm a parent process(%s), created child(%s)"%(os.getpid(), pid))