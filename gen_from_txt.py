#coding=utf-8
__author__ = 'zs'
# coding=utf-8

from wordcloud import WordCloud
import numpy
from PIL import Image
import matplotlib.pyplot as plt
import itchat
import sys
from random import randint

reload(sys)
sys.setdefaultencoding('utf8')


def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = randint(120, 250)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(randint(60, 120)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)

with open('./nicks.txt', 'r') as fr:
    sig=fr.readline()
#    print sig

msk = numpy.array(Image.open('c:/temp/logo.jpg'))
wc = WordCloud(font_path='STHUPO.TTF',
               background_color='white',
               max_font_size=75,
               min_font_size=15,
               #color_func= random_color_func(),
               #               mask=msk,
               font_step=1,
               mode='RGB',
               random_state=45,
               width=1024,
               height=768,
               margin=15)
#wc.generate(sig)
#wc.generate(u'明_ 铁_ Jason Mraz 流浪的米狼 Sky tap billy 裸奔的手机 暴雨 wxl [LAG]ZS 小米爸爸 SiS6326 Justin 温州 鼓手孙斌 dancer 迷途羔羊 Daniel')
wc.generate(u'指兔为马 冰城 风云 TT bibby [LAG]ZS sunmoon DaiPi 小花Rave FENG 没心没肺 zero5 johnson Sky _锤 如天 THOR 铲屎大官人 zumain 钱新 JIAWEI Numb 暴雨 夏华 韩嘉伦 陈小象 裸奔的手机 鼓手孙斌 Gary Lam Yu 陈捷 Maxgon Keel Grin chris huh 曲波 夜星 Ray 骆东生 陆地 至尊宝 刘航 庄_ Leant 老白 昱 马大哈尼 nothing 大海 Johnson 龘飝 烂砖头 张雪峰 Evence 赵辉 梅梦潇 Gina 黄福龙 A翔 犀利哥 TODD 人才 A诚昱 NL CopyCat Marcato LC 奋斗的小白猪 英雄 大軍 阿萌 Phelix 土豆 过河卒 溜溜球 小八宝贝多之茶禅一味 AAA意利达胶带厂 terrant 言 凯利 Norther deadhead 姚家桢 勇哥 JY 古道西北风 Dexter Edward 张三的哥 VOKA gentleman 就叫我红领巾吧 袁旭 汪宇 弩哥 开 Terry 褚达 赖树鹏 明明 来世愿做风 大衣服 憨哥老赵 MAX L 朱成标-Bill Rain AA汤义 omphalos 狼 ‮‮‮‮‮‮‭Aellen 半點鐘 李万亮 我是猫萌萌 AXXXXL Chao.z 弘二 王勇Ping999 [DraGon]Four quakerw dancer k x5dragon RukiapR0ss zlllp YXH咸鱼 亚龙 奔放的主席 小神仙他爹老神经 树洞君 老程 无处安放 Cobradane Iny')

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.savefig('c:/temp/wc.jpg', dpi=200)

#itchat.send_image('c:/temp/wc.jpg', 'filehelper')
print 'ok!'