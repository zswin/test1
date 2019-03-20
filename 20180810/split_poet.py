#coding=utf-8
__author__ = 'zs'
import json

with open("d:/zs/test1/poetspider/x.json", 'rb') as f:
    tmp = json.loads(f.read())
    with open("d:/zs/test1/poetspider/x.txt", "w") as ff:
        for i, d in enumerate(tmp):
            li = ""
            title = d['title']
            author = d['author']
            dyna = d['dyna']
            p = d['poet']
            for p1 in p:
                li += str(p1)
            txt = "<" + title + ">" + author + "(" + dyna + ")" + li
            txt = txt.encode('gbk').decode('gbk')
            ff.write(txt)
            print(txt)