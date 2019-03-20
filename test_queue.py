# coding=utf-8
__author__ = 'zs'
from multiprocessing import Queue, Process
import time

def reader_que(queue):
    while True:
        msg = queue.get()
        print(msg)
        if msg == 'DONE':
            break

def writer_que(count, queue):
    for ii in range(count):
        queue.put(ii)
    queue.put('DONE')


if __name__ == '__main__':
    print('test for queue')
    for count in [10**3, 10**4, 10**5]:
        queue=Queue()
        reader_q = Process(target=reader_que, args=(queue,))
        reader_q.daemon = True
        reader_q.start()

        _start = time.time()
        writer_que(count, queue)
        reader_q.join()
        print("sending %s numbers to Queue took %s seconds"%(count, time.time() - _start))
