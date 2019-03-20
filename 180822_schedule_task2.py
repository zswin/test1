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
    def __init__(self, job_name, device_id, device_name, time_points, command):
        self.job_name = job_name
        self.time_points = time_points
        self.command = command
        self.device_id = device_id
        self.device_name = device_name
        self.start_point = -1
        self.cmd = None
    def f_run_task(self):
        fname = ''.join((self.device_id, self.device_name, '-', time.strftime('%Y%m%d%H%M%S', time.localtime())))
        print(''.join(('>>>start task ', self.job_name, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) )))
        #self.cmd = subprocess.Popen(self.command.format(fname), shell = True, stdin = subprocess.PIPE)
        print(''.join((' @@@@@@@@@@@@@@ exec ', self.command.format(fname))))

    def f_stop_task(self):
        print(''.join(('###stop task', self.job_name, '-', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) )))
        if self.cmd.poll() is None:
            self.cmd.comnunicate(input = b'q')
            self.start_point += 1
            print(''.join((self.job_name, ' start point changed to %d'%self.start_point)))

    def f_timer(self):
        flag = 0
        fin = True
        while fin:
            time_start = self.time_points[self.start_point][0]
            time_end = self.time_points[self.start_point][1]
            if time_start >= time_end:
                flag = 0
                ok = False
                print(''.join((self.job_name, ' time period is invalid')))
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
                        print(''.join(('****', self.job_name, " Today's work is finished.")))
                        fin = False
                        exit
    def f_start(self):
        for idx, tup in enumerate(self.time_points):
            now = time.strftime("%H:%M:%S", time.localtime())
            print(tup)
            l =  tup[0]
            m = tup[1]
            if tup[0] < now < tup[1]:
                self.start_point = idx
                print(''.join((self.job_name, ' start from %d'% idx)))
                self.f_timer()
            if self.start_point == -1:
                print(''.join((self.job_name, ' No entry found, task schedule stopped.')))
if __name__ == '__main__':
    i = 0
    cam_list = glob.glob(CWD + '//*.ini')
    for cam in cam_list:
        i += 1
        with open(cam, 'r') as cam_ini:
            cfg = configparser.ConfigParser()
            cfg.read(cam_ini.name)
            _job_name = cam_ini.name
            _device_id = cfg.get('db', 'device_id')
            _device_name = cfg.get('db', 'device_name')
            _time_points = eval(cfg.get('db', 'time_points'))
            _command = cfg.get('db', 'command')
            qgdownloader = QingGuoDownloader(_job_name, _device_id, _device_name, _time_points, _command)
            print('start %d'% i)
            qgdownloader.f_start()
