# coding=utf-8
__author__ = 'zs'
import gc

def dump_garbage():
    print("\nBARBAGE:")
    gc.collect()
    print("\nGarbage objects:")
    for x in gc.garbage:
        s=str(x)
        if len(s)>80:
            s=s[:77]
        print(type(x), ':', s)

if __name__ == '__main__':
    gc.enable()
    gc.set_debug(gc.DEBUG_LEAK)
    l=[ ]
    l.append(l)
    del l
    dump_garbage()
    print(gc.collect())