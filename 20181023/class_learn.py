#coding=utf-8
__author__ = 'zs'
class Dog(object):
    '''this is a test class'''
    _score = 0
    def __init__(self,name):
        self.name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


if __name__ == '__main__':
    d = Dog('tom')
#    d.score = 100
    print(d.score)
    print(d.__doc__)
    print(d.__module__)
    print(d.__class__)