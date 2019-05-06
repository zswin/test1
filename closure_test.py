# coding=utf-8
__author__ = 'zs'


def outer(a):
    b = 10

    def inner():
        print(a+b)
    return inner


if __name__ == '__main__':
    demo = outer(5)
    demo()

    demo2 = outer(8)
    demo2()

