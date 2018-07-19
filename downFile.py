#coding=utf-8
__author__ = 'zs'
import sys
import requests

def downFile(url):
    cnt = 0
    print (u'downloading %s'%url)
    fileName = url.split('/')[-1]
    r = requests.get(url, stream = True)
    with open(fileName, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024*1024):
            if chunk:
                cnt += 1
                f.write(chunk)
                f.flush()
                print('%d M downloaded'%cnt)

    print ('%s downloaded'%url)

from urllib.request import urlretrieve
import os
def schedule(a,b,c):
    per = 100.00 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%'%per)
def downFile2(url):
    fileName = url.split('/')[-1]
    urlretrieve(url, fileName, schedule)
if __name__ == '__main__':
    #downFile('http://huajun1.onlinedown.net/down/IPCameraViewer.zip')
    downFile2('http://huajun1.onlinedown.net/down/IPCameraViewer.zip')

