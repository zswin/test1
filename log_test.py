# coding=utf-8
__author__ = 'zs'
import logging
import logging.handlers
import time

def test1():
    logging.basicConfig(level=logging.INFO,
                        filename='wtf.log',
                        filemode='a',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('testLogger')
    con = logging.StreamHandler()#default to standard output
    con.setLevel(logging.ERROR)
    logger.addHandler(con)
    for a in range(10):
        logger.info("this is info - {}".format(a))
    for b in range(10):
        logger.error("this is error - {}".format(b))

def test2():
    logging.basicConfig(level=logging.DEBUG,
                        filemode='a',
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    fh = logging.handlers.RotatingFileHandler('wtf2.log', 'S', 2, 10)
    fh.suffix = "%Y%m%d-%H%M%S.log"
    logger.addHandler(fh)
    i = 0
    while i < 1000:
        logger.info(time.strftime("%Y-%m-%d %H%M%S", time.localtime()))
        time.sleep(1)
if __name__ == '__main__':
    test2()