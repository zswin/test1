# coding=utf-8
__author__ = 'zs'
from datetime import datetime

def log(func):
    def wrapper(*args, **kwargs):
        print("calling {}".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@log
def now():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    now()