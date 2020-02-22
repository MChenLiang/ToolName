#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time      :  14:40
# Email     : spirit_az@foxmail.com
# File      : openUI.py
__author__ = 'ChenLiang.Miao'
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import existsUI as exUI
import baseFunction as bFc
from imp import reload

reload(exUI)

# function +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

houdini_win = exUI.getMainWindow()
__abs_path__ = bFc.getScriptPath().replace('\\', '/')
main_win_name = 'tool name'
scriptVersion = 'version by author'


def icon_path(in_name):
    # return in_name
    return os.path.join(os.path.dirname(__abs_path__), 'icons', in_name).replace('\\', '/')


def getUIPath():
    return os.path.join(__abs_path__, 'UI/UIName.ui').replace('\\', '/')


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
form_class, base_class = exUI.loadUi(getUIPath())


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

class mainFunc(form_class, base_class):
    def __init__(self, parent=houdini_win):
        super(mainFunc, self).__init__(parent)
        self._init_ui()
        self._bt_clicked()

    def _init_ui(self):
        # print exUI.getStyleSheet()
        # self.setStyleSheet(exUI.getStyleSheet())
        pass

    def _bt_clicked(self):
        pass


def show():
    exUI.deleteUI(exUI.QMainWindow, main_win_name)
    anim_path = icon_path('waiting.gif')
    splash = exUI.mSplashScreen(anim_path, exUI.Qt.WindowStaysOnTopHint)
    splash.setParent(houdini_win)
    splash.show()
    ui = mainFunc()  # type: exUI.QMainWindow
    # 设置名称 一定不可以在初始化的时候设置，否则会出问题
    ui.setObjectName(main_win_name)
    ui.setWindowTitle('%s %s' % (main_win_name, scriptVersion))
    ui.setWindowIcon(exUI.QIcon(icon_path('MCL.png')))
    splash.showMessage('author : %s' % __author__, exUI.Qt.AlignLeft | exUI.Qt.AlignBottom,
                       exUI.Qt.yellow)
    t = exUI.QElapsedTimer()
    t.start()
    while t.elapsed() < 600:
        exUI.QCoreApplication.processEvents()
    splash.finish(ui)
    ui.setStyleSheet(exUI.getStyleSheet())
