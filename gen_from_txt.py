#coding=utf-8
__author__ = 'zs'
# coding=utf-8

from wordcloud import WordCloud
import numpy
from PIL import Image
import matplotlib.pyplot as plt
import itchat
import sys
reload(sys)
sys.setdefaultencoding('utf8')

with open('./nicks.txt', 'r') as fr:
    sig=fr.readline()
#    print sig

msk = numpy.array(Image.open('c:/temp/logo.jpg'))
wc = WordCloud(font_path='STHUPO.TTF',
               background_color='white',
               max_font_size=75,
               min_font_size=15,
               #               mask=msk,
               font_step=1,
               mode='RGB',
               random_state=45,
               width=1024,
               height=768,
               margin=15)
#wc.generate(sig)
wc.generate(u'明_ 铁_ Jason Mraz 流浪的米狼 Sky tap billy 裸奔的手机 暴雨 wxl [LAG]ZS 小米爸爸 SiS6326 Justin 温州 鼓手孙斌 dancer 迷途羔羊 Daniel')
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.savefig('c:/temp/wc.jpg', dpi=200)

#itchat.send_image('c:/temp/wc.jpg', 'filehelper')
print 'ok!'