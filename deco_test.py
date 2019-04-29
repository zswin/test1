# coding=utf-8
__author__ = 'zs'
from datetime import datetime

#decorator with no parms
def log(func):
    def wrapper(*args, **kwargs):
        print("calling {}".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

#decorator with parms
def log2(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("callling with {}{}".format(text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log
def now():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@log2('(this is log2)')
def now2():
    print(datetime.now().strftime("%Y-%m-%d"))

if __name__ == '__main__':
    now()
    now2()
