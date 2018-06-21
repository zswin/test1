# coding=utf-8

from wordcloud import WordCloud
import numpy
from PIL import Image
import matplotlib.pyplot as plt
import itchat

users = ''
SEARCH = 'LAG'
itchat.login()
room = itchat.search_chatrooms(SEARCH)
room_full = itchat.update_chatroom(room[0]['UserName'], detailedMember=True)
for usr in room_full['MemberList']:
    print usr['NickName']
    users += ' ' + usr['NickName']
print users

sig = users
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
wc.generate(sig)
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.savefig('c:/temp/wc.jpg', dpi=200)

itchat.send_image('c:/temp/wc.jpg', 'filehelper')
print 'ok!'