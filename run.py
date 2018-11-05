#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     run
   Description :
   Author :       24637
-------------------------------------------------
"""
from proxypool.scheduler import Schedular
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


def main():
    try:
        s = Schedular()
        s.run()

    except:
        main()

if __name__ == '__main__':
    main()