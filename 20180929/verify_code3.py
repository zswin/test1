from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random

def get_random_color():
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return (c1, c2, c3)

def get_random_char():
    rand_num = str(random.randint(0, 9))
    rand_low = chr(random.randint(97, 122))
    rand_up = chr(random.randint(65, 90))
    return random.choice([rand_num, rand_low, rand_up])

img1 = Image.new('RGB', (150, 30), (255,255,255))
draw1 = ImageDraw.Draw(img1, 'RGB')
font1 = ImageFont.truetype("c:/windows/fonts/Arial.ttf", size=26)
for i in range(5):
    random_char = get_random_char()
    draw1.text((10+i*30, 0), random_char, get_random_color(), font1)

width = 150
height = 30

#random lines
for i in range(5):
    x1 = random.randint(0, width)
    x2 = random.randint(0, width)
    y1 = random.randint(0, height)
    y2 = random.randint(0, height)
    draw1.line((x1, y1, x2, y2), fill = get_random_color())

#random dots
for i in range(30):
    draw1.point((random.randint(0, width), random.randint(0, height)), fill = get_random_color())
    x = random.randint(0, width)
    y = random.randint(0, height)
    draw1.arc((x, y, x+4, y+4), 0, 90, fill = get_random_color())
with open('verify3.png', 'wb') as f:
    img1.save(f, format = 'PNG')

img1.show()
