# coding=utf-8
__author__ = 'zs'

class Fruit(object):
    def __init__(self):
        pass

    def print_color(self):
        print(">> not implemented")


class Apple(Fruit):
    def __init__(self):
        super(Apple, self).__init__()
        pass

    def print_color(self):
        print("apple is red")


class Orange(Fruit):
    def __init__(self):
        super(Orange,self).__init__()
        pass

    def print_color(self):
        print('orange is orange')


class FruitFactory(object):
    fruits = {"apple": Apple, "orange": Orange}

    def __new__(cls, name):
        if name in cls.fruits.keys():
            return cls.fruits[name]()
        else:
            return Fruit()


f1 = FruitFactory('apple')
f2 = FruitFactory('orange')
f3 = FruitFactory('banana')
f1.print_color()
f2.print_color()
f3.print_color()
