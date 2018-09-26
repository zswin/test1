#coding=utf-8
__author__ = 'zs'
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def rand_char():
    return chr(random.randint(65, 90))

def rand_color():
    return random.randint(0, 245), random.randint(0, 245), random.randint(0, 245)

def gen_code(file_name= 'code'):
    width = 60 *4
    height = 60
    img1 = Image.new('RGB', (width, height), (255, 255, 255))
    font1 = ImageFont.truetype('c:/windows/fonts/Arial.ttf', size=28)
    draw1 = ImageDraw.Draw(img1, 'RGB')
    draw1.line((0, 0 + random.randint(0, height // 2), width, 0 + random.randint(0, height // 2)), fill = rand_color())
    draw1.line((0, height - random.randint(0, height // 2), width, height - random.randint(0, height // 2)), fill = rand_color())

    code_str = ''
    for i in range(5):
        tmp = rand_char()
        draw1.text((i*60+10, 10), tmp, fill = rand_color(), font = font1)
        code_str += tmp
    img1 = img1.filter(ImageFilter.BLUR)
    img1.save(file_name +'.png', format= 'png')
    return code_str, file_name

if __name__ == '__main__':
    for i in range(5):
        gen_code('code_%d'%i)
