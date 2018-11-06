#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     setting
   Description :
   Author :       24637
-------------------------------------------------
"""
REDIS_HOST = '127.0.0.1'

REDIS_PORT = 6379

REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200,302]

POOL_MAX_THRESHOLD = 50000

TEST_CYCLE = 20

GET_CYCLE = 300

TEST_URL = 'http://www.baidu.com'

API_HOST = '0.0.0.0'

API_PORT = 8888

TEST_ENABLED = True
GET_ENABLED = True
API_ENABLED = True

MAX_TEST_SIZE = 10

