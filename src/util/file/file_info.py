# -*- coding: utf-8 -*-
"""
@Projcet :  python-learning
@File : file_info
@Descriptioin : 
@DateTime : 2020/10/30 11:56
@Author : fangqing.fan#hotmail.com
"""


import os
import hashlib

'''获取文件的大小,结果保留两位小数，单位为MB'''
def get_file_size(filePath:str):
    #filePath = unicode(filePath,'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    #print(fsize)
    return round(fsize,2)

def get_file_ext(filePath:str):
    '''
    eg:get_file_ext("/Users/fred/Desktop/test/ds.MP4")
    ret: mp4
    :param filePath:
    :return:
    '''
    return filePath[filePath.rindex('.')+1:len(filePath)].lower()

def get_file_name(filePath:str):
    '''
    eg:get_file_ext("/Users/fred/Desktop/test/ds.MP4")
    ret: ds
    :param filePath:
    :return:
    '''
    return filePath[filePath.rindex('/') + 1:filePath.rindex('.') ]

def get_file_root_path(filePath:str):
    return filePath[0:filePath.rindex('/')+1 ]

def get_file_sha1hash(filepath):
    with open(filepath,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        return hash

def get_file_md5hash(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash

if __name__ == '__main__':
    get_file_size("/Users/fred/Desktop/test/工作日常.jpg")