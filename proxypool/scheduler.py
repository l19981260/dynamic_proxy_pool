#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     scheduler
   Description :
   Author :       24637
-------------------------------------------------
"""
import time
from multiprocessing import Process
from proxypool.api import app
from proxypool.getter import Getter
from proxypool.tester import Tester
from proxypool.database import RedisClient
from proxypool.setting import *

class Schedular():
    def schedule_tester(self,cycle=TEST_CYCLE):
        """
        定时测试代理
        :param cycle:
        """
        tester  = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self,cycle=GET_CYCLE):
        """
        定时获取代理
        :param cycle:
        """
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启api
        """
        app.run(API_HOST,API_PORT)

    def run(self):
        print('代理池开始运行')

        if TEST_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if GET_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()
