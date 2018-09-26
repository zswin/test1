#coding=utf-8
__author__ = 'zs'
import random
from PIL import Image, ImageDraw, ImageFont

img1 = Image.new(mode='RGB', size=(120,30), color= (255,255,255))

draw1 = ImageDraw.Draw(img1, mode='RGB')
font1 = ImageFont.truetype('c:/windows/fonts/CHILLER.ttf', 28)
for i in range(5):
    char1 = random.choice([chr(random.randint(65, 90)), str(random.randint(0, 9))])
    color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw1.text([i*24, 0], char1, fill = color1, font = font1)

with open("verify1.png", "wb") as f:
    img1.save(f, format = "png")