#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

import os
import sys
import tempfile
import logging

"""
日志的级别:
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0

"""


class myLogger(object):
    __logger = None
    __handler = None
    __sHandler = None
    __log_file = ''

    @property
    def logfile(self):
        return self.__log_file

    @property
    def logger(self):
        return self.__logger

    @logger.setter
    def logger(self, val):
        self.__logger = logging.getLogger(val)

        # 设置级别， handler的总控级别，默认为WARNING
        self.__logger.setLevel(logging.DEBUG)

    @property
    def handler(self):
        return self.__handler

    @handler.setter
    def handler(self, val):
        handler = self.__handler
        handler and self.logger.removeHandler(handler)
        self.__sHandler and self.logger.removeHandler(self.__sHandler)
        self.__log_file = os.path.join(
            tempfile.gettempdir(),
            "%s.txt" %
            val).replace(
            '\\',
            '/')
        # 日志存储 : 存储警告以上内容
        self.__handler = logging.FileHandler(
            self.__log_file, mode='w', encoding='utf-8')
        fmt = logging.Formatter(
            '%(asctime)s -- %(name)s "%(filename)s" %(levelname)s:%(message)s')
        self.__handler.setFormatter(fmt=fmt)
        self.__handler.setLevel(logging.WARN)
        self.__logger.addHandler(self.__handler)
        # 日志报文 ： 正常操作报文
        self.__sHandler = logging.StreamHandler(sys.stdout)
        self.__sHandler.setFormatter(fmt)
        self.__sHandler.setLevel(logging.INFO)
        self.__logger.addHandler(self.__sHandler)

    def close(self):
        x = self.logger.handlers
        for i in x:
            self.logger.removeHandler(i)
            i.flush()
            i.close()
