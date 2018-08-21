#coding=utf-8
__author__ = 'zs'
import time
import subprocess

def subprocess_exec(command, time_out = 60):
    '''launching the command'''
    cmd = subprocess.Popen(command)
    '''now waiting for the command to complete'''
    t = 0
    while t < time_out and cmd.poll() is None:
        time.sleep(1)
        t += 1

    '''there are to possibilities for the while to have stopped'''
    if cmd.poll() is None:
        #in the case the process did not complete in time_out, we kill it
        cmd.terminate()
        returncode = -1
    else:
        returncode = cmd.poll()


    return returncode

if __name__ == '__main__':
    subprocess_exec(['dir', '/ad'])
