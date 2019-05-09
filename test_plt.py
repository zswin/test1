# coding=utf-8
__author__ = 'zs'
import numpy as np
import matplotlib.pyplot as plt
def sincos():
    x = np.arange(0, 10, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, label='sin')
    plt.plot(x, y2, linestyle='--', label='cos')
    plt.xlabel('x轴', fontproperties='SimHei')
    plt.ylabel('y轴', fontproperties='SimHei')
    plt.title("sin和cos图形", fontproperties='YouYuan')
    plt.legend()
    plt.show()


def _and(x1, x2):
    x = np.array((x1,x2))
    w = np.array((0.5, 0.5))
    b = -0.7
    tmp = sum(x*w) + b
    if tmp >= 0:
        return 1
    else:
        return 0


def _nand(x1, x2):
    x = np.array([x1,x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = sum(x*w) + b
    if tmp >= 0:
        return 1
    else:
        return 0

def _or(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = sum(x*w) + b
    if tmp >= 0:
        return 1
    else:
        return 0


def step_func(x):
    return np.array(x>0, dtype=np.int)

def sigmoid(x):
    return 1/(1+np.exp(-x))


def fun1():
    x = np.arange(-5, 5, 0.1)
    y = sigmoid(x)
    y2 = step_func(x)
    plt.plot(x,y)
    plt.plot(x, y2, linestyle='--')
    plt.ylim(-0.1,1.1)
    plt.show()
def fun2():
    x1 = np.arange(-10,10, 0.1)
    x2 = np.arange(-10, 10, 0.1)
    y = x1**2 + x2**2
    plt.plot(x1,x2,y)
    plt.show()

if __name__ == '__main__':
    '''print('and (1,1)=', _and(1,1))
    print('nand(1,0)=', _nand(1,0))
    print('or(1,0)=', _or(1,0))
    '''
    fun2()