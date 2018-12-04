#coding=utf-8
__author__ = 'zs'
import time
import os
from selenium.common.exceptions import NoSuchElementException
from urllib import request
from selenium import webdriver

PIC_BASE_DIR = 'd:\smoke_pic'
def get_file_ext(full_file):
    return os.path.splitext(full_file)[1]

def get_page_info():
    br = webdriver.Chrome()
    k = 0
    err = 0
    base_url = "http://www.etmoc.com/Firms/Product?Id="
    lst_all = list()
    lst_ok = list()
    lst_err = list()
    csv_line = ''
    csv_file = open('smokes.csv', 'w')
    for i in range(999, 3097):
        k = k + 1
        goods_id = str(i)
        url = base_url + goods_id
        page = br.get(url)
        time.sleep(2)
        try:
          '''  goods_name = br.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div[1]").text
            prop_tmp = br.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div[2]").text
            goods_prop_list = prop_tmp.split('\n')
            goods_type = goods_prop_list[1].split("：")[1]
            goods_tar = goods_prop_list[2].split("：")[1]
            goods_nicotine = goods_prop_list[3].split("：")[1]
            goods_co = goods_prop_list[4].split("：")[1]
            goods_package = goods_prop_list[5].split("：")[1]
            goods_spec = goods_prop_list[6].split("：")[1]
            goods_pack_barcode = goods_prop_list[7].split("：")[1]
            goods_bar_barcode = goods_prop_list[8].split("：")[1]
            goods_pack_price = goods_prop_list[9].split("：")[1]
            goods_bar_price = goods_prop_list[10].split("：")[1]
            goods_whole_sale_price = goods_prop_list[11].split("：")[1]
            goods_pic_url = br.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/a/img").\
                get_attribute('src')
            csv_line = ','.join([goods_name, goods_type, goods_tar, goods_nicotine, goods_co, goods_package, goods_spec,
                                 goods_pack_barcode, goods_bar_barcode, goods_pack_price, goods_bar_price,
                                 goods_whole_sale_price, goods_pic_url])
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
            dic['goods_pic_url'] = goods_pic_url
            pic_ext = get_file_ext((goods_pic_url))
            pic_local = PIC_BASE_DIR + "\\" + goods_pack_barcode + pic_ext
            request.urlretrieve(goods_pic_url, pic_local)
            print(url)
            print(dic)
            lst_all.append(str(dic))
            dic.clear()
            time.sleep(1)
            print('finished ', str(k))
            lst_ok.append(i)
        except NoSuchElementException as e:
            err = err + 1
            lst_err.append(i)
            print(e)
            '''
    br.close()
    csv_file.close()
    print(lst_all)
    f = open('smokes.txt', 'w')
    f.write(str(lst_all))
    f.close()

    f_ok = open('smoke_ok_id.txt', 'w')
    f_ok.write(str(lst_ok))
    f_ok.close()

    f_err = open('smoke_err_id.txt', 'w')
    f_err.write(str(lst_err))
    f_err.close()


if __name__ == '__main__':
    get_page_info()
