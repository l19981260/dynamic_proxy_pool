#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     importer
   Description :
   Author :       24637
-------------------------------------------------
"""
from proxypool.database import RedisClient

connection = RedisClient()

def set(proxy):
    result = connection.add(proxy)
    print(proxy)
    print('录入成功' if result else '录入失败')


def scan():
    print('请输入代理，输入exit退出读入')
    while True:
        proxy = input()
        if proxy == 'exit':
            break
        set(proxy)



if __name__ == '__main__':
    scan()

