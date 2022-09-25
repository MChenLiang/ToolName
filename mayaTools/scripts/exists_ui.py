#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

import maya.OpenMayaUI as mui
import maya.cmds as cmds
from Qt import QtCompat as QtCompat
from Qt import QtCore as QtCore
from Qt import QtGui as QtGui
from Qt import QtWidgets as QtWidgets


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def maya_api_version():
    return int(cmds.about(api=True)[:8])


def ptr_to_long(ptr):
    return long(ptr) if maya_api_version() < 20220000 else int(ptr)


def to_qt_object(maya_name, qt_type=QtCore.QObject):
    ptr = mui.MQtUtil.findControl(maya_name)
    if ptr is None:
        ptr = mui.MQtUtil.findLayout(maya_name)
    if ptr is None:
        ptr = mui.MQtUtil.findMenuItem(maya_name)
    if ptr is not None:
        return wrap_instance(ptr_to_long(ptr), qt_type)
    return None


def get_maya_layout(layout_string):
    ptr = mui.MQtUtil.findLayout(layout_string)
    if ptr:
        return wrap_instance(ptr_to_long(ptr))


def get_window(window_name):
    ptr = mui.MQtUtil.findWindow(window_name)
    if ptr:
        return wrap_instance(ptr_to_long(ptr), QtWidgets.QMainWindow)


def get_full_name(qt_object):
    pointer = QtCompat.getCppPointer(qt_object)
    if isinstance(pointer, long):
        window_string = mui.MQtUtil.fullName(pointer)
        if window_string:
            return window_string
        else:
            return ''
    else:
        return get_qt_widget(qt_object.objectName(), long_name=True)[-1]


def wrap_instance(widget, qt_type=QtCore.QObject):
    cond = bool(maya_api_version() < 20220000)
    if cond:
        key_type = basestring
    else:
        key_type = str
    if isinstance(widget, key_type):
        widget = mui.MQtUtil.findWindow(widget)

    return QtCompat.wrapInstance(ptr_to_long(widget), qt_type)


def get_maya_main_window():
    maya_window = mui.MQtUtil.mainWindow()
    return wrap_instance(ptr_to_long(maya_window), QtWidgets.QMainWindow)


def get_qt_widget(qt_widget_name, long_name=False):
    root_name = str(get_maya_main_window().objectName())
    get_name = qt_widget_name.split('|')[-1]
    for w in QtWidgets.QApplication.topLevelWidgets():
        try:
            if w.objectName() == get_name:
                if long_name:
                    return w, '|' + '|'.join([root_name, qt_widget_name])
                else:
                    return w
        except Exception:
            pass

    try:
        for w in QtWidgets.QApplication.topLevelWidgets():
            for c in w.children():
                if c.objectName() == get_name:
                    if long_name:
                        return c, '|' + \
                               '|'.join([str(w.objectName()), str(c.objectName())])
                    else:
                        return c

    except Exception:
        pass


def ui_exists(ui_name, as_bool=True):
    q_object = get_qt_widget(ui_name)
    if q_object:
        if as_bool:
            return bool(q_object)
        return q_object
    elif as_bool:
        return False
    else:
        return None


def raise_ui(ui_name):
    q_object = get_qt_widget(ui_name)
    if q_object:
        return q_object
    else:
        return False


def delete_ui(ui_name, qt_type=QtCore.QObject):
    try:
        QtCompat.delete(to_qt_object(ui_name, qt_type))
    except Exception:
        pass


def load_ui(ui_path):
    """
    read an ui file, get two classes to return..
    """
    form_class, base_class = QtCompat.load_ui(ui_path)

    return form_class, base_class


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class MSplashScreen(QtWidgets.QSplashScreen):
    def __init__(self, animation, flag):
        super(MSplashScreen, self).__init__(QtGui.QPixmap(), flag)
        self.setObjectName('SplashScreen')
        self.movie = QtGui.QMovie(animation)
        self.movie.setParent(self)
        self.movie.frameChanged.connect(self.onNextFrame)
        self.setEnabled(False)

    @QtCore.Slot(int)
    def onNextFrame(self, *args):
        pixmap = self.movie.currentPixmap()
        self.setPixmap(pixmap)
        self.setMask(pixmap.mask())

    def showEvent(self, *args):
        self.movie.start()

    def closeEvent(self, *args):
        self.movie.stop()
        super(MSplashScreen, self).closeEvent(*args)


class MSplashScreenNew(QtWidgets.QSplashScreen):
    """
    start movie once
    """

    def __init__(self, animation, flag, widget):
        super(MSplashScreenNew, self).__init__(QtGui.QPixmap(), flag)
        self.setObjectName('SplashScreen')
        self.movie = QtGui.QMovie(animation)
        self.movie.setParent(self)
        self.movie.frameChanged.connect(self.onNextFrame)
        self.count = self.movie.frameCount()
        self.step = 0
        self.widget = widget

    @QtCore.Slot(int)
    def onNextFrame(self, *args):
        if self.step < self.count:
            pixmap = self.movie.currentPixmap()
            self.setPixmap(pixmap)
            self.setMask(pixmap.mask())
            self.step += 1
        else:
            self.finish(self.widget)

    def showEvent(self, *args):
        self.movie.start()

    def closeEvent(self, *args):
        self.movie.stop()
        super(MSplashScreenNew, self).closeEvent(*args)
