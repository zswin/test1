# coding=utf-8
__author__ = 'zs'

@profile
def fib(max):
    n,a,b=0,1,1
    while n<max:
        print(b)
        a,b=b,a+b
        n+=1


@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == '__main__':
    fib(10)

