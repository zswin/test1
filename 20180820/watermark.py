#coding=utf-8
__author__ = 'zs'
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

font = ImageFont.truetype('C:/windows/fonts/tahoma.ttf', 20)

im = Image.open('c:/temp/1.jpg')
draw = ImageDraw.Draw(im)
draw.text((160, 0), "this is a WaterMark", (255,255,255), font = font)
draw = ImageDraw.Draw(im)

im.save('c:/temp/1-1.jpg')