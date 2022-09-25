#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import pathlib

try:
    from . import script_tool
except Exception:
    import script_tool

import pyside2uic


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def uic2py(name):
    """
    :param name:
    :return:
    """
    py_file = str(name).replace('.ui', '.py')
    with open(py_file, 'w') as f:
        pyside2uic.compileUi(name, f)

    change2qt(py_file)


def change2qt(py_file):
    print(py_file)
    os.system('python -m Qt --convert "{}"'.format(py_file))


if __name__ == '__main__':
    ui = script_tool.get_script_path().parent.joinpath("UI")  # type: pathlib.Path
    [uic2py(str(x)) for x in ui.glob("**/*.ui")]
