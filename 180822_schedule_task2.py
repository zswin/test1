#coding=utf-8
__author__ = 'zs'
import time
import subprocess
import glob
import configparser
import os

global CWD
CWD = r'd:\camera\ffmpeg\bin'

class QingGuoDownloader():
    def __init__(self, time_points, command, device_id, device_name):
        self.time_points = time_points
        self.command = command
        self.device_id = device_id
        self.device_name = device_name
        self.start_point = 0
        self.cmd = None
    def f_run_task(self):
        fname = ''.join((self.device_id, self.device_name, time.strftime('%Y%m%d%H%M%S', time.localtime())))
        print(''.join(('>>>start task', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) )))
        self.cmd = subprocess.Popen(self.command.format(fname), shell = True, stdin = subprocess.PIPE)

    def f_stop_task(self):
        print(''.join(('###stop task', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) )))
        if self.cmd.poll() is None:
            self.cmd.comnunicate(input = b'q')
            self.start_point += 1
            print('start point changed to %d'%self.start_point)

    def f_timer(self):
        flag = 0
        fin = True
        while fin:
            time_start = self.time_points[self.start_point][0]
            time_end = self.time_points[self.start_point][1]
            if time_start >= time_end:
                flag = 0
                ok = False
                print('time period is invalid')
                exit
            now = time.strftime('%H:%M:%S', time.localtime())
            if time_start < now < time_end:
                if flag == 0:
                    flag = 1
                    self.f_run_task()
            if now > time_end:
                if flag == 1:
                    flag = 0
                    self.f_stop_task()
                    if len(self.time_points) == self.start_point:
                        print("Today's work is finished.")
                        fin = False
                        exit

if __name__ == '__main__':
    cam_list = glob.glob(CWD + '//*.ini')
    for cam in cam_list:
        with open(cam, 'r') as cam_ini:
            cfg = configparser.ConfigParser()
            cfg.read(cam_ini.name)
            device_id = cfg.get('db', 'device_id')
            device_name = cfg.get('db', 'device_name')
            time_points = cfg.get('db', 'time_points')
            command = cfg.get('db', 'command')
            print(''.join((device_id, device_name, time_points, command)))
