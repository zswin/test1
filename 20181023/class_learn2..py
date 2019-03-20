#coding=utf-8
__author__ = 'zs'
def bulk(self):
    print('%s is talking'%(self.name))

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self):
        print('%s is eating'%(self.name))

d = Dog("TOM")
choice = input("please input method name:")
if hasattr(d, choice):
    func = getattr(d, choice)
    func()
else:
    setattr(d, choice, bulk)
    func = getattr(d, choice)
    func(d)
   # print('no this method')