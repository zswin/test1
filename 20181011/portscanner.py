#coding=utf-8

__author__ = 'zs'
import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('cls', shell=True)

remote_server = input('please input host to scan:')
remote_server_ip = socket.gethostbyname(remote_server)

print ('-'*60)
print ('please wait, scanning remote', remote_server_ip)
print ('-'*60)

t1 = datetime.now()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remote_server_ip, port))
        if result == 0:
            print('port {}:open'.format(port))
        sock.close()
except KeyboardInterrupt:
    print('you pressed ctrl+c')
    sys.exit()
except socket.gaierror:
    print('host could not be resolved')
    sys.exit()
except socket.error:
    print('could not connect to host')
    sys.exit()

t2 = datetime.now()
total = t2 - t1

print('scanning complete in:', total)
