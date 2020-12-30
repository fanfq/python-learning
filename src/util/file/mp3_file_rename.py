# -*- coding: utf-8 -*-
"""
@Projcet :  python-learning
@File : file_rename
@Descriptioin : 
@DateTime : 2020/11/5 09:33
@Author : fangqing.fan#hotmail.com

#依赖安装
pip3 install mutagen
pip3 install qiniu

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

import sys
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

'''
eg: 2020-12-30
:return:
'''
def get_date_today():
    today = datetime.date.today()
    return today

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

    #根据目录遍历该目录的文件,其中包含子目录
    '''
    os.walk的函数声明为:
    walk(top, topdown=True, onerror=None, followlinks=False)
    参数：
        top 是你所要便利的目录的地址
        topdown 为真，则优先遍历top目录，否则优先遍历top的子目录(默认为开启)
        onerror 需要一个 callable 对象，当walk需要异常时，会调用
        followlinks 如果为真，则会遍历目录下的快捷方式(linux 下是 symbolic link)实际所指的目录(默认关闭)
        os.walk 的返回值是一个生成器(generator),也就是说我们需要不断的遍历它，来获得所有的内容。
        每次遍历的对象都是返回的是一个三元组(root,dirs,files)
        root 所指的是当前正在遍历的这个文件夹的本身的地址
        dirs 是一个 list ，内容是该文件夹中所有的目录的名字(包括子目录)
        files 同样是 list , 内容是该文件夹中所有的文件(包括子目录的文件)
    '''
    g = os.walk(path)
    files = []

    #该目录下的，所有文件，其中包含子目录
    #for root,dir_list,file_list in g:
    #    for file_name in file_list:
    #        file_ = os.path.join(root, file_name)
    #        if(file_.upper().endswith(files_ext_filter.upper())):
    #            files.append(file_)

    #该目录下的，所有文件，其中不包含子目录
    for root,dir_list,file_list in g:
        if root == path: #只包含当前目录，排除子目录
            for file_name in file_list:
                file_ = os.path.join(root, file_name)
                #根据文件扩展名过滤
                if(file_.upper().endswith(files_ext_filter.upper())):
                    files.append(file_)

    #sys.exit()

    for f in files:
        #******************************************************
        name = get_file_name(f)
        #根据文件名前缀过滤
        if(name.startswith(prefix)):
            continue
        #duration = get_mp3_duration(f)
        #length = int(get_file_size(f) * 1024 * 1024)
        md5hash = get_file_md5hash(f)
        #print(duration)
        #print(length)
        #print(md5hash)
        #print(name)
        #print("src:",f)

        #******************************************************
        #newName = prefix + name + "_" + str(length) + "_" + str(duration) + "." + get_file_ext(f)
        #dstFilePath = get_file_root_path(f) + newName
        #print('newName:',newName)
        #print('dstFilePath:',dstFilePath)
        #os.rename(f, dstFilePath)

        #******************************************************
        #新文件名以hacode命名，目录名则是当天日期 yyyy-mm-dd
        #mov 至新目录，并删除原文件。当在mov发现重名文件则替换从而排重
        newName = md5hash+"."+get_file_ext(f)
        dstPath = get_file_root_path(f) + str(get_date_today())
        #目录不存在则创建
        if not os.path.exists(dstPath):
            os.makedirs(dstPath)
        dstFilePath = os.path.join(dstPath, newName)
        print('newName:',newName)
        print('dstFilePath:',dstFilePath)
        os.rename(f, dstFilePath)
        
        #******************************************************
        #上传至cdn
        #upload_to_qiniu(dstFilePath,newName)



