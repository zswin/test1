#coding=utf-8
__author__ = 'zs'
import os, sys

kilobytes = 1024
chun_100k = 100 * kilobytes
megabytes = kilobytes * 1000


def split(fromfile, todir, chunksize = chun_100k):
    if not os.path.exists(todir):
        os.mkdir(todir)
    else:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir, fname))
    partnum = 0
    input = open(fromfile, 'rb')
    while True:
        chunk = input.read(chunksize)
        if not chunk:
            break
        partnum += 1
        filename = os.path.join(todir, 'part%04d' % partnum)
        fileobj = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()
    input.close()
    assert partnum <= 9999
    return partnum

def join(fromdir, tofile):
    output = open(tofile, 'wb')
    parts = os.listdir(fromdir)
    parts.sort()
    for fname in parts:
        filepath = os.path.join(fromdir, fname)
        fileobj = open(filepath, 'rb')
        while True:
            filebytes = fileobj.read(chun_100k)
            if not filebytes:
                break
            output.write(filebytes)
        fileobj.close()
    output.close()



if __name__ == '__main__':
   #split('d:/zs/test1/1.jpg', 'd:/zs/test1/jpg_split')
    join('d:/zs/test1/jpg_split', 'd:/zs/test1/2.jpg')