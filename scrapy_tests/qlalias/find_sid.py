# coding=utf-8
__author__ = 'zs'
import re
import glob

if __name__ == '__main__':
    files = [name for name in glob.glob('d:/log/*.log')]
    dic = dict()
    pat = re.compile("\w* player_connect[(]\w*[(]\w*[:](.*)[)][,]")
    for f in files:
        print('processing ', f)
        for line in open(f, encoding='utf-8'):
            lst = pat.findall(line)
            if len(lst) > 0:
                str_lst = lst[0].split(':')
                nick = str_lst[0].replace(',','，').encode('utf-8')
                sid = str_lst[1]
                dic[sid] = nick

    with open('d:/list.txt', 'a', encoding='utf-8') as f:
        for x in dic:
            f.write(x + ',' + dic[x].decode('utf-8') + '\n')


