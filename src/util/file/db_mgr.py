
# -*- coding: utf-8 -*-
"""
@Projcet :  python-learning
@File : db_mgr
@Descriptioin : https://www.jianshu.com/p/2b778c32a2f4
@DateTime : 2020/10/30 13:00
@Author : fangqing.fan#hotmail.com
"""
from util.file.db_config import *
from util.file.file_entity import FileEntity

dbname = 'mydb.db3'

db_config(dbname)

executescript('drop table if exists test;'
             'drop table if exists school;')

executefile('util.file','test.sql')

with trans():
    execute('insert into test values(?,?,?)',[1,'Tom',23])
    executemany('insert into test values(?,?,?)',[
        [2,'Alice',22],
        [3,'John',21]])

def truncat_file_table():
    with trans():
        execute('DELETE FROM files')
        executescript("DELETE FROM sqlite_sequence WHERE name = 'files'")

def get_file_by_md5hash(md5hash:str):
    #sql = "select count(*) from files where md5hash= ?"+md5hash
    count = findvalue('select count(*) from files where md5hash= ?',[md5hash])
    return count


def add_file(f:FileEntity):
    #print(f.name, f.ext, f.path, f.size, f.md5hash, f.sha1hash)
    #print({f.name}, {f.ext}, "${f.path}", '${f.size}', '${f.md5hash}', '${f.sha1hash}')
    with trans():
        #name,ext,path,size,md5hash,sha1hash
        #"insert into files values(${f.name}, ${f.ext}, ${f.path}, ${f.size}, ${f.md5hash}, ${f.sha1hash})
        sql = "insert into files(name,ext,path,size,md5hash,sha1hash) values('"+f.name+"','"+ f.ext+"','"+f.path+"','"+ str(f.size)+"','"+ f.md5hash+"','"+ f.sha1hash+"')"
        #print(sql)
        execute(sql)


'''
注意： execute 和 executemany 需要在 trans 环境下执行，
同一个trans下全部执行成功则提交服务器，执行中存在异常则全部回滚。
如果不在 trans环境下执行，则连接关闭后修改的数据完全丢失。
executescript 和 executefile不需要在 trans环境下执行，会自动提交。
故只应使用 DDL 语句，而不应该插入或修改数据 。

'''