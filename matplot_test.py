# coding=utf-8
__author__ = 'zs'
import numpy as np
import matplotlib.pyplot as plt

def test1():
    x = np.linspace(1, 10, 50)
    y1 = 2 * x + 1
    y2 = x**2

    plt.figure()
    plt.plot(x, y1)
    plt.show()

    plt.figure(num=3, figsize=(8,5))
    plt.plot(x, y1)
    plt.plot(x, y2, color='m', linewidth=3.0, linestyle='-')

    plt.show()

def test2():
    plt.figure()
    plt.subplot(2,2,1)
    plt.plot([0,1], [0,1])

    plt.subplot(2,2,2)
    plt.plot([0,1], [2,2])

    plt.subplot(2, 2, 3)
    plt.plot([1, 1], [2, 3])

    plt.subplot(2, 2, 4)
    plt.plot([1, 2], [2, 1])

    plt.show()

def test3():
    x = np.linspace(0, 10, 20)
    y1 = x

    plt.figure()
    plt.plot(x, y1)
    plt.xlim((-1, 10))
    plt.ylim((0, 8))
    plt.xlabel("I am x axis")
    plt.ylabel("I am y axis")
    new_ticks = np.linspace(-1, 10, 11)
    plt.xticks(new_ticks)
    plt.show()
def test4():
    x = np.linspace(-1, 5, 10)
    y1 = x
    y2 = x**2 - 1

    plt.figure()
    l1, = plt.plot(x, y1, label='L1')
    l2, = plt.plot(x, y2, label='L2')
    plt.legend(handles=[l1, l2], loc="best",ncol=2)
    plt.show()

def test5():
    x = np.linspace(0, 2, 10)
    y1 = x
    y2 = x ** 2

    plt.figure()
    l1, = plt.plot(x, y1, label="L1")
    l2, = plt.plot(x, y2, label="L2")
    plt.xlim(0, 2)
    plt.ylim(0, 2)

    plt.legend([l1,l2], loc='best')
    x0 = y0 = 1
    plt.scatter(x0, y0, s = 50, color='b')
    plt.plot([0,1], [1,1], 'k--')
    plt.plot([1,1], [0,1], 'm--')

    x1 = 0.25
    y1 = 1.5
    plt.text(x1, y1,  # 设置基准坐标
             r'$function : y={x_i}^2 $',  # 设置显示内容，可以使用Latex
             fontdict={'size': 18, 'color': 'r'})  # 设置字体
    plt.show()

def test6():
    n=1024
    x = np.random.normal(0, 1, n)
    y = np.random.normal(0, 1, n)
    t = np.arctan2(x, y)
    plt.scatter(x, y, s=45, c=t, alpha=0.5)
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.xticks(())
    plt.yticks(())
    plt.show()

if __name__ == '__main__':
    test6()