# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:/MCCCCL/coding/mayaTools/mayaTool=/scripts/UI\UIName.ui'
#
# Created: Sun Jul  4 01:34:41 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(883, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_filepath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filepath.setObjectName("lineEdit_filepath")
        self.horizontalLayout.addWidget(self.lineEdit_filepath)
        self.pushButton_f_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_f_load.setObjectName("pushButton_f_load")
        self.horizontalLayout.addWidget(self.pushButton_f_load)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_ec_r = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_ec_r.setInputMethodHints(QtCore.Qt.ImhNone)
        self.comboBox_ec_r.setMaxVisibleItems(4)
        self.comboBox_ec_r.setObjectName("comboBox_ec_r")
        self.comboBox_ec_r.addItem("")
        self.comboBox_ec_r.addItem("")
        self.comboBox_ec_r.addItem("")
        self.comboBox_ec_r.addItem("")
        self.gridLayout.addWidget(self.comboBox_ec_r, 1, 0, 1, 1)
        self.checkBox_open_a = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_open_a.setObjectName("checkBox_open_a")
        self.gridLayout.addWidget(self.checkBox_open_a, 0, 3, 1, 1)
        self.comboBox_ec_g = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_ec_g.setInputMethodHints(QtCore.Qt.ImhNone)
        self.comboBox_ec_g.setMaxVisibleItems(4)
        self.comboBox_ec_g.setObjectName("comboBox_ec_g")
        self.comboBox_ec_g.addItem("")
        self.comboBox_ec_g.addItem("")
        self.comboBox_ec_g.addItem("")
        self.comboBox_ec_g.addItem("")
        self.gridLayout.addWidget(self.comboBox_ec_g, 1, 1, 1, 1)
        self.checkBox_open_r = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_open_r.setChecked(True)
        self.checkBox_open_r.setObjectName("checkBox_open_r")
        self.gridLayout.addWidget(self.checkBox_open_r, 0, 0, 1, 1)
        self.checkBox_open_b = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_open_b.setObjectName("checkBox_open_b")
        self.gridLayout.addWidget(self.checkBox_open_b, 0, 2, 1, 1)
        self.checkBox_open_g = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_open_g.setObjectName("checkBox_open_g")
        self.gridLayout.addWidget(self.checkBox_open_g, 0, 1, 1, 1)
        self.comboBox_ec_a = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_ec_a.setInputMethodHints(QtCore.Qt.ImhNone)
        self.comboBox_ec_a.setMaxVisibleItems(4)
        self.comboBox_ec_a.setObjectName("comboBox_ec_a")
        self.comboBox_ec_a.addItem("")
        self.comboBox_ec_a.addItem("")
        self.comboBox_ec_a.addItem("")
        self.comboBox_ec_a.addItem("")
        self.gridLayout.addWidget(self.comboBox_ec_a, 1, 3, 1, 1)
        self.comboBox_ec_b = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_ec_b.setInputMethodHints(QtCore.Qt.ImhNone)
        self.comboBox_ec_b.setMaxVisibleItems(4)
        self.comboBox_ec_b.setObjectName("comboBox_ec_b")
        self.comboBox_ec_b.addItem("")
        self.comboBox_ec_b.addItem("")
        self.comboBox_ec_b.addItem("")
        self.comboBox_ec_b.addItem("")
        self.gridLayout.addWidget(self.comboBox_ec_b, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(
            862,
            16,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_run = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_run.setObjectName("pushButton_run")
        self.verticalLayout.addWidget(self.pushButton_run)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_3 = QtWidgets.QFrame(self.widget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.line = QtWidgets.QFrame(self.widget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 883, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.menuFile.addAction(self.actionhelp)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBox_ec_g.setCurrentIndex(1)
        self.comboBox_ec_a.setCurrentIndex(3)
        self.comboBox_ec_b.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QtWidgets.QApplication.translate(
                "MainWindow", "MainWindow", None, -1))
        self.label.setText(
            QtWidgets.QApplication.translate(
                "MainWindow", "路径：", None, -1))
        self.pushButton_f_load.setText(
            QtWidgets.QApplication.translate(
                "MainWindow", "加载", None, -1))
        self.groupBox.setTitle(
            QtWidgets.QApplication.translate(
                "MainWindow", "点颜色设置", None, -1))
        self.comboBox_ec_r.setItemText(
            0, QtWidgets.QApplication.translate(
                "MainWindow", "R", None, -1))
        self.comboBox_ec_r.setItemText(
            1, QtWidgets.QApplication.translate(
                "MainWindow", "G", None, -1))
        self.comboBox_ec_r.setItemText(
            2, QtWidgets.QApplication.translate(
                "MainWindow", "B", None, -1))
        self.comboBox_ec_r.setItemText(
            3, QtWidgets.QApplication.translate(
                "MainWindow", "A", None, -1))
        self.checkBox_open_a.setText(
            QtWidgets.QApplication.translate(
                "MainWindow", "A", None, -1))
        self.comboBox_ec_g.setItemText(
            0, QtWidgets.QApplication.translate(
                "MainWindow", "R", None, -1))
        self.comboBox_ec_g.setItemText(
            1, QtWidgets.QApplication.translate(
                "MainWindow", "G", None, -1))
        self.comboBox_ec_g.setItemText(
            2, QtWidgets.QApplication.translate(
                "MainWindow", "B", None, -1))
        self.comboBox_ec_g.setItemText(
            3, QtWidgets.QApplication.translate(
                "MainWindow", "A", None, -1))
        self.checkBox_open_r.setText(
            QtWidgets.QApplication.translate(
                "MainWindow", "R", None, -1))
        self.checkBox_open_b.setText(
            QtWidgets.QApplication.translate(
                "MainWindow", "B", None, -1))
        self.checkBox_open_g.setText(
            QtWidgets.QApplication.translate(
                "MainWindow", "G", None, -1))
        self.comboBox_ec_a.setItemText(
            0, QtWidgets.QApplication.translate(
                "MainWindow", "R", None, -1))
        self.comboBox_ec_a.setItemText(
            1, QtWidgets.QApplication.translate(
                "MainWindow", "G", None, -1))
        self.comboBox_ec_a.setItemText(
            2, QtWidgets.QApplication.translate(
                "MainWindow", "B", None, -1))
        self.comboBox_ec_a.setItemText(
            3, QtWidgets.QApplication.translate(
                "MainWindow", "A", None, -1))
        self.comboBox_ec_b.setItemText(
            0, QtWidgets.QApplication.translate(
                "MainWindow", "R", None, -1))
        self.comboBox_ec_b.setItemText(
            1, QtWidgets.QApplication.translate(
                "MainWindow", "G", None, -1))
        self.comboBox_ec_b.setItemText(
            2, QtWidgets.QApplication.translate(
                "MainWindow", "B", None, -1))
        self.comboBox_ec_b.setItemText(
            3, QtWidgets.QApplication.translate(
                "MainWindow", "A", None, -1))
        self.pushButton_run.setText(
            QtWidgets.QApplication.translate(
                "MainWindow", "执行", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate(
            "MainWindow", "spirit_az@foxmail.com", None, -1))
        self.menuFile.setTitle(
            QtWidgets.QApplication.translate(
                "MainWindow", "File", None, -1))
        self.actionhelp.setText(
            QtWidgets.QApplication.translate(
                "MainWindow", "help", None, -1))
