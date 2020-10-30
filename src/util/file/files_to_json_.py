# -*- coding: utf-8 -*-
"""
@Projcet :
@File : files_to_json
@Descriptioin : 将文件夹中的文件名写入json文件，以便其他程序调用
@DateTime : 2020/10/20 11:27
@Author : fangqing.fan#hotmail.com

imgs.json 文件
{"imgs":["99.jpg","84c92d28f78740a49704e8f243d20a26.jpg","60c134feaceb41a9a91510a8e3c501d3.jpg","0399f162521d47699cdfd1c69ff287ee.jpg","b593ad98c6c8453292dd6230a8ad696b.jpg"]}


albums.json 相册
{"count": 445, "current": 7, "desc": 0}
count：总计有多少个文件，
current：当前已经读到第几个，
desc：是否降序
"""

import os
import json

from util.file.file_entity import FileEntity

files_ext_filter = '.jpg' #只筛选出.py文件
files_json_file = 'imgs.json'
albums_json_file = 'albums.json'

#print('***获取当前目录***')
#path = os.getcwd()
#print(os.getcwd())

def files_to_json(path):
    _list_dir(path)

def _list_dir(file_dir):
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
        print(path)
        if os.path.isfile(path): # 判断是否是文件还是目录需要用绝对路径
            print("{0} : is file!".format(cur_file))
            files.append(FileEntity(path))
        if os.path.isdir(path):
            print("{0} : is dir!".format(cur_file))
            _list_dir(path) # 递归子目录

    _files_json_file = file_dir+"/"+files_json_file
    with open(_files_json_file, "w") as f:
        dist = {}
        dist['imgs'] = json.dumps(files, ensure_ascii=False)
        json.dump(dist, f)

    _albums_json_file = file_dir+"/"+albums_json_file
    with open(_albums_json_file, "w") as f:
        dist = {}
        dist['count'] = files.count()
        dist['current'] = 1
        dist['desc'] = 0
        json.dump(dist, f)
        print("加载入文件完成...")


if __name__ == '__main__':
    #将当前文件信息写入json文件
    files_to_json("/Users/fred/Desktop/test2")