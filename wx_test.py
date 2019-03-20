# coding=utf-8
__author__ = 'zs'
import itchat
from PIL import Image
import os

itchat.auto_login()
friends=itchat.get_friends(update=True)[0:]
user=friends[0]['UserName']
print user

num=0
for i in friends:
	img=itchat.get_head_img(userName=i['UserName'])
	fileImage=open('c:/temp/itchat' + os.sep + str(num) + '.jpg', 'wb')
	fileImage.write(img)
	num+=1

mw=133
ms=10
msize=mw * ms
fpre='x'
toImage=Image.new('RGB', (msize, msize))
for y in range(1,11):
	for x in range(1,11):
		fname='c:/temp/itchat/%s.jpg' % (ms*(y-1)+x)
		fromImage=Image.open(fname)
		fromImage=fromImage.resize((mw, mw), Image.ANTIALIAS)
		a=(x-1) * mw
		b=(y-1) * mw
		toImage.paste(fromImage, box=(a,b))
toImage.save('c:/temp/itchat/all.jpg')
toImage.show()
