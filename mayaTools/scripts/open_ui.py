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
import weakref

import maya.cmds as cmds

from . import exists_ui as ex_ui
from . import script_tool
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from .UI import UIName as UIName

try:
    from maya.app.general import mayaMixin as mayaMixin
except ImportError:
    from . import mayaMixin as mayaMixin

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
maya_win = ex_ui.get_maya_main_window()
__abs_path__ = script_tool.get_script_path()
main_win_name = __abs_path__.parts[-2]
script_version = '1.0 by MCL'

names = globals()  # type: dict
names[main_win_name] = None


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def icon_path(in_name):
    # return in_name
    return str(__abs_path__.parent.joinpath("icons", in_name)).replace("\\", "/")


class MyDockingWindow(
    mayaMixin.MayaQWidgetDockableMixin,
    ex_ui.QtWidgets.QMainWindow):
    MAYA2017 = 20170000
    MAYA2022 = 20220000
    instances = list()

    def __init__(self, parent=None):

        # remove any instance of this window before starting
        MyDockingWindow.delete_instances()
        self.__class__.instances.append(weakref.proxy(self))

        super(MyDockingWindow, self).__init__(parent)

        self.setWindowFlags(ex_ui.QtCore.Qt.Tool)
        self.setAttribute(ex_ui.QtCore.Qt.WA_DeleteOnClose)

        self.setWindowTitle(main_win_name + script_version)

    def dockCloseEventTriggered(self):
        MyDockingWindow.delete_instances()

    # Delete any instances of this class
    @staticmethod
    def delete_instances():
        for ins in MyDockingWindow.instances:
            try:
                ins.setParent(None)
                # ins.deleteLater()  # 这是一个bug，不知道为什么内存会自动稀释
            except Exception:
                pass
            finally:
                MyDockingWindow.instances.remove(ins)
                del ins

    def delete_control(self, control):

        if cmds.workspaceControl(control, q=True, exists=True):
            cmds.workspaceControl(control, e=True, close=True)
            cmds.deleteUI(control, control=True)

    # Show window with docking ability
    def run(self):
        """
        2017 docking is a little different...
        """
        initScript = u''
        initScript += u'import sys\r\n'
        initScript += u'in_path = "{}"\r\n'.format(__abs_path__.parent.parent).replace("\\", "//")
        initScript += u'in_path in sys.path and sys.path.remove(in_path)\r\n'
        initScript += u'sys.path.insert(0, in_path)\r\n'
        initScript += u'from {}.scripts import open_ui\r\n'.format(
            main_win_name)

        if ex_ui.maya_api_version() < 20220000:
            initScript += u'reload(open_ui)\r\n'
        else:
            initScript += u'import importlib\r\n'
            initScript += u'importlib.reload(open_ui)\r\n'

        initScript += u'open_ui.encryption(1)'

        def run2017():

            workspace_control_name = self.objectName() + 'WorkspaceControl'
            self.delete_control(workspace_control_name)

            self.show(
                dockable=True,
                area='right',
                floating=False,
                uiScript=initScript)
            cmds.workspaceControl(
                workspace_control_name, e=True, ttc=[
                    "AttributeEditor", -1], wp="preferred")
            self.raise_()

            # size can be adjusted, of course
            self.setDockableParameters(width=420)

        def run2016():
            self.show(
                dockable=True,
                floating=False,
                area='right',
                restore=True)  #
            self.raise_()
            # size can be adjusted, of course
            self.setDockableParameters(width=420)
            self.setSizePolicy(
                ex_ui.QtWidgets.QSizePolicy.Minimum,
                ex_ui.QtWidgets.QSizePolicy.Preferred)
            self.setMinimumWidth(420)
            self.setMaximumWidth(600)

        if ex_ui.maya_api_version() < MyDockingWindow.MAYA2017:
            run2016()
        else:
            run2017()


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

window_class, base_class = UIName.Ui_MainWindow, MyDockingWindow


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class MainFunc(window_class, base_class):
    def __init__(self, parent=None):
        super(MainFunc, self).__init__(parent)
        self.setupUi(self)

        self._bt_clicked()

    def _init_ui(self):
        pass

    def _bt_clicked(self):
        self.actionhelp.triggered.connect(self.tool_help)

    def tool_help(self):
        os.system("start EXCEL.EXE \"{}\"".format(
            str(__abs_path__.parent.joinpath("doc", u"工具说明.xlsx"))))


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def encryption(restore=False):
    if names[main_win_name] is None:
        names[main_win_name] = MainFunc(parent=maya_win)
        names[main_win_name].setObjectName(main_win_name)
        names[main_win_name].setWindowTitle(main_win_name + script_version)

    if restore:
        restored_control = ex_ui.mui.MQtUtil.getCurrentParent()
        mixin_ptr = ex_ui.mui.MQtUtil.findControl(names[main_win_name].objectName())
        ex_ui.mui.MQtUtil.addWidgetToMayaLayout(
            ex_ui.ptr_to_long(mixin_ptr), ex_ui.ptr_to_long(restored_control))
    else:
        splash = ex_ui.MSplashScreen(
            icon_path('waiting.gif'), ex_ui.QtCore.Qt.WindowStaysOnTopHint)
        splash.showMessage(
            'author : %s' %
            __author__,
            ex_ui.QtCore.Qt.AlignLeft | ex_ui.QtCore.Qt.AlignBottom,
            ex_ui.QtCore.Qt.yellow)
        splash.show()
        t = ex_ui.QtCore.QElapsedTimer()
        t.start()
        while t.elapsed() < 600:
            ex_ui.QtCore.QCoreApplication.processEvents()
        splash.finish(names[main_win_name])
        names[main_win_name].run()

    return names[main_win_name]
