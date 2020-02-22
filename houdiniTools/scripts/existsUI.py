# !/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2019/6/27 11:55
# @Email    : spirit_az@foxmail.com
# @Name     : existsUI.py
__author__ = 'miaochenliang'

# import--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import xml
import cStringIO
import hou

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import pyside2uic as uic
try:
    from PySide2 import shiboken2 as sip
except:
    import shiboken2 as sip


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def getMainWindow():
    """Get an instance of the main window."""
    return hou.ui.mainQtWindow()


def getStyleSheet():
    """Get the Houdini stylesheet, possibly for use outside the program.
    For inside Houdini, use setProperty('houdiniStyle', True).
    """
    return hou.qt.styleSheet()


def UIExists(qtType, Name, AsBool=True):
    """
    exists ui by name
    :param Name:  object name
    :param AsBool: is return bool
    :return:
    """

    mainUI = getMainWindow()  # type: QMainWindow
    allC = mainUI.findChild(qtType, Name)
    if allC:
        return True if AsBool else allC
    else:
        return False if AsBool else ''


def deleteUI(qtType, Name):
    """
    delete ui when we find it.
    :param Name:
    :return:
    """

    panetab = UIExists(qtType, Name, AsBool=False)  # type: QMainWindow
    if not panetab:
        return False
    sip.delete(panetab)


def loadUi(uiPath):
    """
    read an ui file, get two classes to return..
    """
    parsed = xml.etree.ElementTree.parse(uiPath)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text

    with open(uiPath, 'r') as f:
        o = cStringIO.StringIO()
        frame = dict()

        uic.compileUi(f, o, indent=0)

        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec pyc in frame

        form_class = frame['Ui_%s' % form_class]
        base_class = eval(widget_class)

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
