# coding=utf-8
__author__ = 'zs'
import os
from datetime import datetime
import shutil

def copy_photos(src_dir, dst_dir):
    files = os.listdir(src_dir)
    for f in files:
        fp = os.path.join(src_dir, f)
        if os.path.isfile(fp):
            create_time = datetime.fromtimestamp(os.path.getmtime(fp))
            print("%s is created @%s"%(fp, create_time))

            ym = datetime.strftime(create_time, "%Y%m")
            year = datetime.strftime(create_time, "%Y")

            dst_path = os.path.join(dst_dir, year, ym)
            if not os.path.exists(dst_path):
                os.makedirs(dst_path)

            dst_fp = os.path.join(dst_path, f)

            print('ready to copy:%s -> %s'%(fp, dst_fp))
            shutil.copyfile(fp, dst_fp)
            print('ok')
        else:
            print("%s is not a file"%fp)


if __name__ == '__main__':
    copy_photos("c:/temp/3", "c:/temp/1")