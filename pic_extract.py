#coding=utf-8
__author__ = 'zs'
import urllib
from lxml import etree
import requests

def schedule(blocknum, blocksize, totalsize):
    per = 100.00 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print("download percentage:%d" % per)

if __name__ == '__main__':
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    headers = {"User-Agent":user_agent}
    r = requests.get("http://www.ivsky.com/tupian/ziranfengguang", headers=headers)
    html = etree.HTML(r.text)
    img_urls = html.xpath(".//img/@src")
    i = 0
    for img in img_urls:
#        print(img)
        urllib.request.urlretrieve(img, r'c:/temp/img' + str(i) + '.jpg', schedule)
        i += 1