#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import inspect
import pathlib


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def get_parent_classes(obj):
    """
    Get object's all of parent class...
    """
    if isinstance(obj, type):
        return inspect.getmro(obj)
    else:
        return inspect.getmro(obj.__class__)


def get_modules_path(module):
    """
    return dir for imported module..
    """
    module_file = pathlib.Path(inspect.getfile(module))
    module_path = module_file.parent
    return module_path


def get_script_path():
    """
    return dir path for used script..
    """
    script_path = get_modules_path(inspect.currentframe().f_back)
    return script_path


def get_script_file():
    """

    Returns:

    """
    return inspect.getfile(inspect.currentframe().f_back)
