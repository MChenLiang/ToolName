#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time  : 2020/2/19 0019 23:48
# @File  : UIToPY.py
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import glob
from PyQt5 import uic


# proc function -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# function main -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def uicToPY(name):
    with open(str(name).replace('.ui', '.py'), 'w') as f:
        uic.compileUi(name, f)


if __name__ == '__main__':
    dir_name = os.path.dirname(os.path.dirname(__file__))
    filepath = '{}/UI/*.ui'.format(dir_name)
    func = lambda x: uicToPY(x)
    map(func, glob.glob(filepath))
