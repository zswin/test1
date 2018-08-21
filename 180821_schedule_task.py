#coding=utf-8
__author__ = 'zs'
import datetime
import time
import subprocess

global TIME_POINTS
TIME_POINTS = [('19:25:01', '19:26:01'),('19:27:01', '19:28:01'), ('19:40:30', '19:50:01')]
global START_POINT
START_POINT = 0
global COMMAND
COMMAND = r'D:\Camera\ffmpeg\bin\ffmpeg -i "rtmp://v128b0486.live.126.net/live/372d4ebb2d284049b2faf8902d099a33" -c copy -f mp4 {0}.mp4'
global c
def f_run_task():
    fname = time.strftime('%Y%m%d%H%M%S', time.localtime())
    print('>>>start task', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    global c
    c = subprocess.Popen(COMMAND.format(fname), shell=True, stdin = subprocess.PIPE)

def f_stop_task():
    global c
    print('###stop task', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    if c.poll() is  None:
        c.communicate(input=b'q')
    global START_POINT
    START_POINT += 1
    print('STARTPOINT CHANGED TO:%d:' % START_POINT)

def f_timer():
    flag = 0
    ok = True
    while ok:
        start_point = TIME_POINTS[START_POINT][0]
        end_point = TIME_POINTS[START_POINT][1]
        if start_point >= end_point:
            flag = 0
            ok = False
            print('time period is invalid')
            exit
        now = time.strftime('%H:%M:%S', time.localtime())
        if start_point < now < end_point:
            if flag == 0:
                flag = 1
                f_run_task()
        if now > end_point:
            if flag == 1:
                flag = 0
                f_stop_task()
                if len(TIME_POINTS) == START_POINT:
                    print("Today's work is finished!")
                    ok = False
                    exit

if __name__ == '__main__':
    for idx, tup in enumerate(TIME_POINTS):
        now = time.strftime('%H:%M:%S', time.localtime())
        if tup[0] < now < tup[1]:
            START_POINT = idx
            print('found STARTPOINT=', idx)
            f_timer()
    if START_POINT == 0:
        print('No Entry found, task schedule stopped.')
