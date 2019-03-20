#coding=utf-8
__author__ = 'zs'
import hashlib

def get_sha1(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as f:
        chunk = 0
        while chunk != b'':
            chunk = f.read(1024)
            h.update(chunk)
    return h.hexdigest()

def get_md5(filename):
    m = hashlib.md5()
    with open(filename, 'rb') as f:
        chunk = 0
        while chunk != b'':
            chunk = f.read(1024)
            m.update(chunk)
    return m.hexdigest()

if __name__ == '__main__':
    print(get_sha1('./1.jpg'))
    print(get_md5('./1.jpg'))