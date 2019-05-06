# coding=utf-8
__author__ = 'zs'

class Person(object):
    def __new__(cls, *args, **kwargs):
        print("__new__")
        instance = object.__new__(cls)
        return instance


    def __init__(self, name, age):
        print("__init__")
        self.name = name
        self.age = age

p = Person("tom", 10)