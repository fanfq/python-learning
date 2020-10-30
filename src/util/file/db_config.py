# -*- coding: utf-8 -*-
"""
@Projcet :  python-learning
@File : db_config
@Descriptioin : https://www.jianshu.com/p/2b778c32a2f4
@DateTime : 2020/10/30 13:51
@Author : fangqing.fan#hotmail.com
"""

import atexit
import sqlite3
from contextlib import contextmanager, closing
from pathlib import Path

_conn = None
_config = {}

def db_config(database: str, **kw):
    global _config
    kw['database'] = str(database)
    _config = kw

def connect():
    global _conn
    if not _conn:
        _conn = sqlite3.connect(**_config)
        atexit.register(_conn.close)
    return _conn

@contextmanager
def trans():
    try:
        conn = connect()
        yield
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e

def execute(sql: str):
    return connect().execute(sql)

def execute(sql: str, params: list = []):
    return connect().execute(sql, params)

def executemany(sql: str, params: list = []):
    return connect().executemany(sql, params)

def executescript(sql: str):
    return connect().executescript(sql)

def executefile(pkg: str, filename: str):
    '''
    执行程序中附带的资源文件
    pkg         : 所在包的名称
    filename    : 相关于包的文件名，包括路径
    '''
    from pkgutil import get_data
    data = get_data(pkg, filename)
    print(data)
    sql = data.decode('utf8')
    return executescript(sql)

def find(sql: str, params: list = [], multi=True):
    '''执行sql 语句，并返行多行或一行记录'''
    cur = execute(sql, params)
    with closing(cur):
        return cur.fetchall()if multi else cur.fetchone()

def findone(sql: str, params: list = []):
    '''执行 sql 语句，并返回一行记录'''
    return find(sql, params, multi=False)

def findvalue(sql: str, params: list = []):
    '''执行 sql 语句，并返回一个值 '''
    row = findone(sql, params)
    return row and row[0]