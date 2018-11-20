#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     database
   Description :
   Author :       24637
-------------------------------------------------
"""

import redis
from proxypool.error import PoolEmptyError
from proxypool.setting import REDIS_HOST,REDIS_PORT,REDIS_PASSWORD,REDIS_KEY
from proxypool.setting import MAX_SCORE,MIN_SCORE,INITIAL_SCORE
from random import choice
import re

class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        """
        初始化
        :param host: Redis地址
        :param port: Redis端口号
        :param password: Redis密码
        """
        self.db = redis.StrictRedis(host=host,port=port,password=password,db=0,decode_responses=True)

    def add(self,proxy,score=INITIAL_SCORE):
        """
        添加代理
        :param proxy: 代理
        :param score: 代理分数
        :return: 添加结果
        """
        if not re.match('\d+\.\d+\.\d+\.\d+\:\d+',proxy):
            print('代理不符合规范',proxy)
            return
        if not self.db.zscore(REDIS_KEY,proxy):
            return self.db.zadd(REDIS_KEY,score,proxy)

    def random(self):
        """
        随机获取有效的代理：首先尝试获取最高分数的代理，如果不存在，则按照排名获取，如果取不到，抛出异常
        :return: 获取到的随机代理
        """
        result = self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY,0,100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError

    def reduce(self,proxy):
        """
        减少代理分数，如果代理分数小于最小值则删除
        :param proxy: 代理
        :return: 减少后的代理分数
        """
        score = self.db.zscore(REDIS_KEY,proxy)
        if score and score > MIN_SCORE:
            print('代理',proxy,'当前分数',score,'减1')
            return self.db.zincrby(REDIS_KEY,proxy,-1)
        else:
            print('代理',proxy,'当前分数',score,'移除')
            return self.db.zrem(REDIS_KEY,proxy)

    def exists(self,proxy):
        """
        判断代理是否存在
        :param proxy:代理
        :return:是否存在
        """
        print('111')
        return not self.db.zscore(REDIS_KEY,proxy) == None

    def max(self,proxy):
        """
        将代理设置为MAX_SCORE
        :param proxy:代理
        :return:设置结果
        """
        print('代理',proxy,'可以使用，分数设置为',MAX_SCORE)
        return self.db.zadd(REDIS_KEY,MAX_SCORE,proxy)

    def count(self):
        """
        获取总代理数量
        :return: 总代理数量
        """
        return self.db.zcard(REDIS_KEY)

    def all(self):
        """
        获取全部代理
        :return: 全部代理列表
        """
        return self.db.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)

    def batch(self,start,end):
        """
        批量获取代理
        :param start:开始索引
        :param end:结束索引
        :return:代理列表
        """
        return self.db.zrevrange(REDIS_KEY,start,end,-1)

if __name__ == '__main__':
    connection = RedisClient()
    result = connection.batch(5,12)
    print(result)
