# -*- coding: utf-8 -*-
import shutil
import os
from time import clock

def autoClassify(src_root_path, target_dir):
    root_src_dir = src_root_path
    root_target_dir = target_dir
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_target_dir)
        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)
        for file_ in files:
            external = os.path.splitext(file_)[1]
            src_file = os.path.join(src_dir, file_)
            dst_dir_with_type = os.path.join(dst_dir, external[1:])
            if not os.path.exists(dst_dir_with_type):
                os.mkdir(dst_dir_with_type)
            dst_file = os.path.join(dst_dir_with_type, file_)
            if os.path.exists(dst_file):
                continue
            print "coping " + dst_file + "..."
            #userOK = raw_input('are you sure to copy')
            shutil.copy(src_file, dst_file)


root = "/media/jason/Seagate Backup Plus Drive/penetration/Dic/data"
target_dir ="/media/jason/Seagate Backup Plus Drive/penetration/Dic"
autoClassify(root, target_dir)
