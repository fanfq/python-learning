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

https://developer.qiniu.com/kodo/sdk/1242/python#3
增加了cdn直接上传功能，文件从命名完成后直接上传cdn并返回最终url
"""

import os
from mutagen.mp3 import MP3
import hashlib
from qiniu import Auth, put_file, etag
import qiniu.config

files_ext_filter = '.mp3'  # 只筛选出.py文件
files_json_file = 'imgs.json'
albums_json_file = 'albums.json'
# 新文件名的前缀
prefix = 'fm'

# 七牛CDN相关参数
# 需要填写你的 Access Key 和 Secret Key
access_key = 'access_key'
secret_key = 'secret_key'
# 要上传的空间
bucket_name = 'cdn-elselook-com'
upload_prefix = 'mp3/'
cdn_url = 'https://cdn.elselook.com/' + upload_prefix


def upload_to_qiniu(filePath, name):
    print('upload file:', filePath)
    print('upload key:', name)
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 上传后保存的文件名,因为我需要单独的目录管理音频文件所以加了 upload_prefix
    key = upload_prefix + name
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    # 要上传文件的本地路径
    localfile = filePath
    ret, info = put_file(token, key, localfile)
    print(info)
    # assert ret['key'] == key
    # assert ret['hash'] == etag(localfile)
    print('')
    print(cdn_url + name)
    print('')


def get_mp3_duration(filePath):
    '''
    eg:get_mp3_duration("/Users/fred/Desktop/test/ds.mp3")
    ret: 获取mp3文件播放时长单位秒
    :param filePath:
    :return:
    '''
    audio = MP3(filePath)
    # print(audio.info.length)
    return int(audio.info.length)


'''获取文件的大小,结果保留两位小数，单位为MB'''


def get_file_size(filePath: str):
    # filePath = unicode(filePath,'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    # print(fsize)
    return round(fsize, 2)


def get_file_ext(filePath: str):
    '''
    eg:get_file_ext("/Users/fred/Desktop/test/ds.MP4")
    ret: mp4
    :param filePath:
    :return:
    '''
    return filePath[filePath.rindex('.') + 1:len(filePath)].lower()


def get_file_name(filePath: str):
    '''
    eg:get_file_ext("/Users/fred/Desktop/test/ds.MP4")
    ret: ds
    :param filePath:
    :return:
    '''
    return filePath[filePath.rindex('/') + 1:filePath.rindex('.')]


def get_file_root_path(filePath: str):
    return filePath[0:filePath.rindex('/') + 1]


def get_file_sha1hash(filepath):
    with open(filepath, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        return hash


def get_file_md5hash(filepath):
    with open(filepath, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash


if __name__ == '__main__':
    print('***获取当前目录***')
    path = os.getcwd()
    print(path)

    # 根据目录遍历该目录的文件
    g = os.walk(path)
    files = []
    for path, dir_list, file_list in g:
        for file_name in file_list:
            file_ = os.path.join(path, file_name)
            if (file_.upper().endswith(files_ext_filter.upper())):
                files.append(file_)

    for f in files:

        name = get_file_name(f)
        if (name.startswith(prefix)):
            continue
        duration = get_mp3_duration(f)
        length = int(get_file_size(f) * 1024 * 1024)
        # md5hash = get_file_md5hash(f)
        # print(duration)
        # print(length)
        # print(md5hash)
        # print(name)
        print("src:", f)
        newName = prefix + name + "_" + str(length) + "_" + str(duration) + "." + get_file_ext(f)
        dstFilePath = get_file_root_path(f) + newName
        print('newName:', newName)
        print('dstFilePath:', dstFilePath)
        os.rename(f, dstFilePath)

        # 上传至cdn
        upload_to_qiniu(dstFilePath, newName)

