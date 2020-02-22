#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time      :  14:33
# Email     : spirit_az@foxmail.com
# File      : existsUI.py
__author__ = 'ChenLiang.Miao'

# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

import maya.OpenMayaUI as mui
import maya.cmds as cmds
from PyQt5 import sip as sip
from PyQt5 import uic as uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# function +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def GetMayaLayout(layoutString):
    """
    get maya layout
    :param layoutString: layout name
    :return:
    """
    ptr = mui.MQtUtil.findLayout(layoutString)
    if ptr:
        return sip.wrapinstance(long(ptr))


def GetWindow(windowName):
    """
    get maya window
    :param windowName: window name
    :return:
    """
    ptr = mui.MQtUtil.findWindow(windowName)
    if ptr:
        return sip.wrapinstance(long(ptr))


def GetFullName(qObj):
    """
    get Qt object full name
    :param qObj:
    :return:
    """
    pointer = sip.unwrapinstance(qObj)
    if type(pointer) == long:
        windowString = mui.MQtUtil.fullName(pointer)
        if windowString:
            return windowString
        else:
            return ''
    else:
        return GetQtWidget(qObj.objectName(), LongName=True)[-1]


def wrapInstance(widget):
    """
    change to Qt object
    :param widget:
    :return:
    """
    if isinstance(widget, basestring):
        widget = mui.MQtUtil.findWindow(widget)

    return sip.wrapinstance(long(widget), QObject)


def GetMayaMainWindow():
    maya_window = mui.MQtUtil.mainWindow()
    return wrapInstance(maya_window)


def GetQtWidget(QWidgetName, LongName=False):
    """
    Change to QT type, which must be the first level
    :param QWidgetName:
    :param LongName:
    :return:
    """
    RootName = str(GetMayaMainWindow().objectName())
    Name = QWidgetName.split('|')[-1]
    for w in QApplication.topLevelWidgets():
        try:
            if w.objectName() == Name:
                if LongName:
                    return w, '|' + '|'.join([RootName, QWidgetName])
                else:
                    return w
        except:
            pass

    try:
        for w in QApplication.topLevelWidgets():
            for c in w.children():
                if c.objectName() == Name:
                    if LongName:
                        return c, '|' + '|'.join([str(w.objectName()), str(c.objectName())])
                    else:
                        return c

    except:
        pass


def UIExists(Name, AsBool=True):
    QObject = GetQtWidget(Name)
    if QObject:
        if AsBool:
            return bool(QObject)
        return QObject
    elif AsBool:
        return False
    else:
        return None


def deleteUI(Name):
    cmds.deleteUI(Name)


def loadUi(uiPath):
    """
    read an ui file, get two classes to return..
    """
    form_class, base_class = uic.loadUiType(uiPath)
    return form_class, base_class


# start gif --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#

class mSplashScreen(QSplashScreen):
    def __init__(self, animation, flag):
        super(mSplashScreen, self).__init__(QPixmap(), flag)
        self.setObjectName('mSplashScreen')
        self.movie = QMovie(animation)
        self.movie.setParent(self)
        self.movie.frameChanged.connect(self.onNextFrame)

    def onNextFrame(self):
        pixmap = self.movie.currentPixmap()
        self.setPixmap(pixmap)
        self.setMask(pixmap.mask())

    def showEvent(self, *args):
        self.movie.start()

    def finish(self, weight):
        weight.show()
        self.movie.stop()
        deleteUI(QSplashScreen, 'mSplashScreen')


class mSplashScreen_new(QSplashScreen):
    """
    start movie once
    """

    def __init__(self, animation, flag, widget):
        super(mSplashScreen_new, self).__init__(QPixmap(), flag)
        self.setObjectName('mSplashScreen')
        self.movie = QMovie(animation)
        self.movie.setParent(self)
        self.movie.frameChanged.connect(self.onNextFrame)
        self.count = self.movie.frameCount()
        self.step = 0
        self.widget = widget

    def onNextFrame(self):
        if self.step < self.count:
            pixmap = self.movie.currentPixmap()
            self.setPixmap(pixmap)
            self.setMask(pixmap.mask())
            self.step += 1
        else:
            self.finish(self.widget)

    def showEvent(self, *args):
        self.movie.start()

    def finish(self, weight):
        weight.show()
        self.movie.stop()
        deleteUI(QSplashScreen, 'mSplashScreen')
