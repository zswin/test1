#coding=utf-8
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring
def dict_to_xml(tag, d):
    '''
    trun a simple dict to xml
    :param tag:
    :param d:
    :return:
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

if __name__ == "__main__":
    s = {'name':'goods', 'shares':100, 'price':490.1}
    e = dict_to_xml('stock', s)
    print(tostring(e))

