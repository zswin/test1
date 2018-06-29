#coding=utf-8
__author__ = 'zs'
import xlrd

def f_gen_bit(code):
    ll_total = 0
    ll_len = len(code)
    if ll_len <= 0:
        return 'err'
    else:
        for i in range(ll_len-1, -1, -2):
            ll_total += int(code[i])
        ll_total *=3
        for k in range(ll_len -2, -1, -2):
            ll_total += int(code[k])

        ls_ret = str(10 - (ll_total % 10))
        ls_ret = ls_ret[-1]
        return ls_ret

if __name__ == '__main__':
    workbook = xlrd.open_workbook('c:/temp/barcodes.xlsx')
    sheet = workbook.sheet_by_index(0)
    print (sheet.nrows)

    for i in range(1, sheet.nrows):
        bgid = str(int(sheet.cell(i, 0).value))
        bgname = sheet.cell(i, 1).value
        bgbc = str(int(sheet.cell(i, 2).value))
        print (bgbc)
        code = bgbc[:len(bgbc)-1]
        b_gen = f_gen_bit(code)
        b_org = bgbc[-1]
        print (b_gen, '+', b_org)
        print(bgid, bgname, bgbc)
        if b_gen != b_org:
            with open('c:/temp/bglog.txt', 'a+') as f:
                f.write(bgid + '\t' + bgname + '\t' +bgbc +'\r\n')

    print ('done')

