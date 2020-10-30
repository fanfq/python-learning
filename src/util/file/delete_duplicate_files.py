# -*- coding: utf-8 -*-
"""
@Projcet :  python-learning
@File : delete_duplicate_files
@Descriptioin : 
@DateTime : 2020/10/30 11:25
@Author : fangqing.fan#hotmail.com
"""
import os

from util.file.db_mgr import *
from util.file.file_entity import FileEntity

def delete_duplicate_files(path):
    print(path)
    list_dir(path)

def list_dir(file_dir):
    '''
        通过 listdir 得到的是仅当前路径下的文件名，不包括子目录中的文件，如果需要得到所有文件需要递归
    '''
    print('\n<><><><><><> listdir <><><><><><>')
    print("current dir : {0}".format(file_dir))
    dir_list = os.listdir(file_dir)

    files = []
    for cur_file in dir_list:
        # 获取文件的绝对路径
        path = os.path.join(file_dir, cur_file)
        if os.path.isfile(path): # 判断是否是文件还是目录需要用绝对路径
            print("{0} : is file!".format(cur_file))
            print(path)
            files.append(FileEntity(path))
        if os.path.isdir(path):
            print("{0} : is dir!".format(cur_file))
            list_dir(path) # 递归子目录


    for f in files:
        count = get_file_by_md5hash(f.md5hash)
        print(count)
        if(count==0):
            #添加记录,以便后来者比较
            add_file(f)
        else:
            #已存在直接删除
            os.remove(f.path)

    #清空数据库,如果不清的可能会误删数据
    truncat_file_table()


