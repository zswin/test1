#coding=utf-8
__author__ = 'zs'
from PIL import Image
import os

def f_jpeg_res(filename):
    img1 = Image.open(filename, 'r')

    print ('The res of the image is:', img1.size[0], img1.size[1])

if __name__ == '__main__':
    f_jpeg_res('d:/zs/test1/20181008/1.jpg')
    print(os.getcwd())