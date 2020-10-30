# -*- coding: utf-8 -*-
"""
@Projcet :  python-learning
@File : file_entity
@Descriptioin : 
@DateTime : 2020/10/30 12:07
@Author : fangqing.fan#hotmail.com
"""
from util.file.file_info import *


class FileEntity:
    def __init__(self,path):
        self.name = get_file_name(path)
        self.ext = get_file_ext(path)
        self.path = path
        self.size = get_file_size(path)
        self.md5hash = get_file_md5hash(path)
        self.sha1hash = 'get_file_sha1hash(path)'