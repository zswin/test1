# coding=utf-8
__author__ = 'zs'
import threading
import time


def run():
    time.sleep(2)
    print("当前线程名:%s", threading.current_thread().name)
    time.sleep(2)


def test1():
    start_time = time.time()

    print("这是主线程:", threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.start()

    print("主线程结束!", threading.current_thread().name)
    print("一共用时", time.time() - start_time)


def test2():
    start_time = time.time()

    print("这是主线程", threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True)
        t.start()
    print("主线程结束", threading.current_thread().name)
    print("一共用时", time.time() - start_time)


def test3():
    start_time = time.time()
    print("this is the main thread", threading.current_thread().name)

    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        # t.setDaemon(True)
        t.start()

    for t in thread_list:
        t.join()

    print("main thread terminated", threading.current_thread().name)
    print("time used", time.time() - start_time)

def test4():
    start_time = time.time()
    print("this is the main thread", threading.current_thread().name)

    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True) # False同test1
        t.start()
    for x in range(5):# main wait for child thread
        time.sleep(1)
    print("main thread terminated", threading.current_thread().name)
    print("time used", time.time() - start_time)
if __name__ == "__main__":
    test4()