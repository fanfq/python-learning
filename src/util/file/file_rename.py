# -*- coding: utf-8 -*-
"""
@Projcet :  python-learning
@File : file_rename
@Descriptioin : 
@DateTime : 2020/11/5 09:33
@Author : fangqing.fan#hotmail.com

用于podcast音频文件整理
源文件：003.mp3
重命名后的文件：fm003_8776581_2192.mp3
文件命名规范：fm|003|_length_duration
prefix:文件前缀
003：文件原名
length：文件体积单位byte
duration：文件播放时长单位s
"""


import os

from util.file.file_info import *
from util.file.mp3_file_info import *

files_ext_filter = '.mp3' #只筛选出.py文件
files_json_file = 'imgs.json'
albums_json_file = 'albums.json'
prefix = 'fm'

print('***获取当前目录***')
path = "/Users/fred/Desktop/mp3" #os.getcwd()
print(path)

#根据目录遍历该目录的文件
g = os.walk(path)
files = []
for path,dir_list,file_list in g:
    for file_name in file_list:
        file_ = os.path.join(path, file_name)
        if(file_.upper().endswith(files_ext_filter.upper())):
            files.append(file_)

for f in files:
    #print(f)
    name = get_file_name(f)
    if(name.startswith(prefix)):
        continue
    duration = get_mp3_duration(f)
    length = int(get_file_size(f) * 1024 * 1024)
    md5hash = get_file_md5hash(f)
    #print(duration)
    #print(length)
    #print(md5hash)
    #print(name)
    dstDir = get_file_root_path(f) +prefix + name + "_" + str(length) + "_" + str(duration) + "." + get_file_ext(f)
    print(dstDir)
    os.rename(f, dstDir)