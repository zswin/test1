#coding=utf-8
__author__ = 'zs'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    assert u"百度" in driver.title
    elem = driver.find_element_by_name("wd")
    elem.clear()
    elem.send_keys(u"wtf")
    elem.send_keys(Keys.ENTER)
    time.sleep(3)
    assert u"wtf" not in driver.page_source
    driver.close()

if __name__ == "__main__":
    test()
