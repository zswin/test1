#coding=utf-8
__author__ = 'zs'
import time
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from urllib import request
from selenium import webdriver

PIC_BASE_DIR = 'd:\smoke_pic'
def get_file_ext(full_file):
    return os.path.splitext(full_file)[1]

def get_page_info():
    try:
        br = webdriver.Chrome()
        br.set_page_load_timeout(10)
        k = 0
        err = 0
        base_url = "http://www.etmoc.com/Firms/Product?Id="
        csv_line = ''
        csv_file = open('smokes.csv', 'w')
        f = open('smokes.txt', 'w')
        f_ok = open('smokes_ok_id.txt', 'w')
        f_err = open('smokes_err_id.txt','w')
        for i in range(111, 222):
            k = k + 1
            goods_id = str(i)
            url = base_url + goods_id
            #prevent from timeout
            try:
                page = br.get(url)
            except TimeoutException as e:
                page = br.get(url)
                print(e)
            time.sleep(2)
            try:
                goods_name = br.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div[1]").text
                prop_tmp = br.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div[2]").text
                print(goods_name, prop_tmp)
                goods_prop_list = prop_tmp.split('\n')
                goods_type = '-'
                goods_tar = '-'
                goods_nicotine = '-'
                goods_co = '-'
                goods_package = '-'
                goods_spec = '-'
                goods_pack_barcode = '-'
                goods_bar_barcode = '-'
                goods_pack_price = '-'
                goods_bar_price = '-'
                goods_whole_sale_price = '-'
                goods_ttm = '-'
                for idx, item in enumerate(goods_prop_list):
                    if item.startswith('产品类型'):
                        goods_type = goods_prop_list[idx].split("：")[1]
                    if item.startswith('焦油'):
                        goods_tar = goods_prop_list[idx].split("：")[1]
                    if item.startswith('烟碱'):
                        goods_nicotine = goods_prop_list[idx].split("：")[1]
                    if item.startswith('一氧化碳'):
                        goods_co = goods_prop_list[idx].split("：")[1]
                    if item.startswith('包装'):
                        goods_package = goods_prop_list[idx].split("：")[1]
                    if item.startswith('烟支规格'):
                        goods_spec = goods_prop_list[idx].split("：")[1]
                    if item.startswith('小盒条码'):
                        goods_pack_barcode = goods_prop_list[idx].split("：")[1]
                    if item.startswith('条盒条码'):
                        goods_bar_barcode = goods_prop_list[idx].split("：")[1]
                    if item.startswith('小盒零售价'):
                        goods_pack_price = goods_prop_list[idx].split("：")[1]
                    if item.startswith('条盒零售价'):
                        goods_bar_price = goods_prop_list[idx].split("：")[1]
                    if item.startswith('批发价格'):
                        goods_whole_sale_price = goods_prop_list[idx].split("：")[1]
                    if item.startswith('上市时间'):
                        goods_ttm = goods_prop_list[idx].split("：")[1]
                try:
                    goods_pic_url = br.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/a/img").\
                        get_attribute('src')
                except NoSuchElementException as e:
                    goods_pic_url = br.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/img").\
                        get_attribute('src')
                csv_line = ','.join([goods_name, goods_type, goods_tar, goods_nicotine, goods_co, goods_package, goods_spec,
                                     goods_pack_barcode, goods_bar_barcode, goods_pack_price, goods_bar_price,
                                     goods_whole_sale_price, goods_ttm, goods_pic_url])
                csv_file.writelines(csv_line + '\n')
                dic = dict()
                dic['goods_name'] = goods_name
                dic['goods_type'] = goods_type
                dic['goods_tar'] = goods_tar
                dic['goods_nicotine'] = goods_nicotine
                dic['goods_co'] = goods_co
                dic['goods_package'] = goods_package
                dic['goods_spec'] = goods_spec
                dic['goods_pack_barcode'] = goods_pack_barcode
                dic['goods_bar_barcode'] = goods_bar_barcode
                dic['goods_pack_price'] = goods_pack_price
                dic['goods_bar_price'] = goods_bar_price
                dic['goods_whole_sale_price'] = goods_whole_sale_price
                dic['goods_ttm'] = goods_ttm
                dic['goods_pic_url'] = goods_pic_url
                pic_ext = get_file_ext((goods_pic_url))
                pic_local = PIC_BASE_DIR + "\\" + goods_pack_barcode + pic_ext
                if not os.path.exists(pic_local):
                    request.urlretrieve(goods_pic_url, pic_local)
                print(url)
                print(dic)
                f.write(str(dic) + '\n')
                dic.clear()
                time.sleep(1)
                print('finished ', str(k))
                f_ok.write(str(i) + '\n')
            except NoSuchElementException as e:
                err = err + 1
                f_err.write(str(i) + '\n')
                print(e)
    except Exception as e:
        print(e)
    finally:
        br.close()
        csv_file.close()
        f.close()
        f_ok.close()
        f_err.close()

if __name__ == '__main__':
    get_page_info()
