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

files_ext_filter = '.py' #只筛选出.py文件
files_json_file = 'imgs.json'
albums_json_file = 'albums.json'

print('***获取当前目录***')
path = os.getcwd()
#print(os.getcwd())


#根据目录遍历该目录的文件
g = os.walk(path)
files = []
for path,dir_list,file_list in g:
    for file_name in file_list:
        file_ = os.path.join(path, file_name)
        if(file_.upper().endswith(files_ext_filter.upper())):
            files.append(file_)

for f in files:
    print(f)

count = len(files)
print(count)
#写入imgs.json

with open(files_json_file, "w") as f:
    dist = {}
    dist['imgs'] = files
    json.dump(dist, f)

with open(albums_json_file, "w") as f:
    dist = {}
    dist['count'] = count
    dist['current'] = 1
    dist['desc'] = 0
    json.dump(dist, f)
    print("加载入文件完成...")
