# -*- coding: utf-8 -*-
"""
@Projcet :  python-learning
@File : mp3_file_info
@Descriptioin : 
@DateTime : 2020/11/5 09:55
@Author : fangqing.fan#hotmail.com
"""

from mutagen.mp3 import MP3

def get_mp3_duration(filePath):
    '''
    eg:get_mp3_duration("/Users/fred/Desktop/test/ds.mp3")
    ret: 获取mp3文件播放时长单位秒
    :param filePath:
    :return:
    '''
    audio = MP3(filePath)
    #print(audio.info.length)
    return int(audio.info.length)