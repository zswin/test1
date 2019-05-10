# coding=utf-8
__author__ = 'zs'

import re

def f_is_valid_ip(ip):
    pat = '^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5]).(\d{1,2}|1\d\d|2[0-4]\d|25[0-5]).(\d{1,2}|1\d\d|2[0-4]\d|25[0-5]).(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$'
    return re.match(pat, ip)


lst = {'1.1.1.1', '2.2.2.2', '232.242.113.21', '299.32.321.32', '305.255.202.111'}
for ip in lst:
    m = f_is_valid_ip(ip)
    if m == None:
        print('ip %s is none'%ip)
    else:
        print('ip %s is valid'%ip)

'''(\d{1,2}|1\d\d|2[0-4]\d|25[0-5]'''