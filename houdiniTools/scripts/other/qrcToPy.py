#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time  : 2020/2/19 0019 23:47
# @File  : qrcToPy.py
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import glob
import subprocess


# proc function -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
rccPath = r'D:\Program Files\Side Effects Software\Houdini 17.0.352\bin\Qt\rcc.exe'


# function main -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def qrc_to_py(in_path):
    qrc_path, file_flag = os.path.splitext(in_path)
    print qrc_path.replace('\\', '/')
    pipe = subprocess.Popen('{0} -o {1}_rc.py {1}.qrc'.format(rccPath, qrc_path.replace('\\', '/')),
                            stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=0x08)
    del pipe


if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                             'UI/').replace('\\', '/')
    func = lambda x: qrc_to_py(x)
    map(func, glob.glob(file_path + '*.qrc'))