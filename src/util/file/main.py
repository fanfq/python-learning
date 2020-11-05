# -*- coding: utf-8 -*-
"""
@Projcet :  python-learning
@File : main
@Descriptioin : 
@DateTime : 2020/10/30 16:06
@Author : fangqing.fan#hotmail.com
"""
#from util.file.delete_duplicate_files import delete_duplicate_files
from util.file.file_info import *
from util.file.mp3_file_info import get_mp3_duration
import os

if __name__ == '__main__':
    #删除重复文件
    #delete_duplicate_files("/Users/fred/Desktop/test")

    path = '/Users/fred/Desktop/mp3/004.mp3'
    duration = get_mp3_duration(path)
    length = int(get_file_size(path)*1024*1024)
    md5hash = get_file_md5hash(path)
    print(duration)
    print(length)
    print(md5hash)
    name = get_file_name(path)
    print(name)
    dstDir = get_file_root_path(path)+name+"_"+str(length)+"_"+str(duration)+"."+get_file_ext(path)
    print(dstDir)
    os.rename(path,dstDir)
