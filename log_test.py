# coding=utf-8
__author__ = 'zs'
import logging

logging.basicConfig(level=logging.INFO,
                    filename='wtf.log',
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('testLogger')

if __name__ == '__main__':
    for a in range(10):
        logger.info("this is info - {}".format(a))
    for b in range(10):
        logger.error("this is error - {}".format(b))