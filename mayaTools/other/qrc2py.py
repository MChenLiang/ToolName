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
import pathlib

try:
    from . import script_tool
except ImportError:
    import script_tool


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def run():
    command_tool = 'C:/ProgramData/Anaconda3/envs/py37/Scripts/pyrcc5.exe'
    ui = script_tool.get_script_path().parent.joinpath("scripts", "UI")  # type: pathlib.Path
    for each in ui.glob("**/*.qrc"):
        no_flag = each.with_suffix('')
        command = '"{0}" -o {1}_rc.py {2}.qrc'.format(
            command_tool, str(no_flag), str(no_flag))
        os.popen2(command)


if __name__ == "__main__":
    run()
