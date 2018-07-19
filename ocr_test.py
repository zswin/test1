#coding=utf-8
__author__ = 'zs'
#1.install teseract-ocr software on windows, find sim_chinese train data(chi_sim.traineddata,chi_sim_vert.traineddata)
#  put in tessdata directory(https://github.com/tesseract-ocr/tessdata)
#2.pip install pytesseract
#
import pytesseract
from PIL import Image

img = Image.open('c:/temp/chn.jpg')
code = pytesseract.image_to_string(img, lang='chi_sim')
print(code)

img2 = Image.open('c:/temp/test.jpg')
code2 = pytesseract.image_to_string(img2)
print(code2)
