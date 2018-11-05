#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     utils
   Description :
   Author :       24637
-------------------------------------------------
"""

import requests
from requests.exceptions import ConnectionError

base_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

def get_page(url,options={}):
    """
    抓取代理
    :param url:
    :param options:
    :return:
    """
    headers = dict(base_headers,**options)
    print('正在抓取：',url)
    try:
        response = requests.get(url,headers=headers)
        print('抓取成功：',url,response.status_code)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('抓取失败：',url)
        return None