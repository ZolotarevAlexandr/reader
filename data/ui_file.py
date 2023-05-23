# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data/running_line_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.running_line = QtWidgets.QTextEdit(self.centralwidget)
        self.running_line.setGeometry(QtCore.QRect(40, 10, 531, 231))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.running_line.setFont(font)
        self.running_line.setTabChangesFocus(True)
        self.running_line.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.running_line.setObjectName("running_line")
        self.cont_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cont_btn.setGeometry(QtCore.QRect(680, 220, 75, 23))
        self.cont_btn.setObjectName("cont_btn")
        self.pause_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn.setGeometry(QtCore.QRect(590, 220, 75, 23))
        self.pause_btn.setObjectName("pause_btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(640, 80, 77, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plus_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.plus_btn.setObjectName("plus_btn")
        self.verticalLayout.addWidget(self.plus_btn)
        self.current_speed = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_speed.setFont(font)
        self.current_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.current_speed.setObjectName("current_speed")
        self.verticalLayout.addWidget(self.current_speed)
        self.minus_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.minus_btn.setObjectName("minus_btn")
        self.verticalLayout.addWidget(self.minus_btn)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(40, 260, 75, 23))
        self.start_btn.setObjectName("start_btn")
        self.change_btn = QtWidgets.QPushButton(self.centralwidget)
        self.change_btn.setGeometry(QtCore.QRect(130, 260, 75, 23))
        self.change_btn.setObjectName("change_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cont_btn.setText(_translate("MainWindow", "Continue"))
        self.pause_btn.setText(_translate("MainWindow", "Pause"))
        self.plus_btn.setText(_translate("MainWindow", "+"))
        self.current_speed.setText(_translate("MainWindow", "100"))
        self.minus_btn.setText(_translate("MainWindow", "-"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.change_btn.setText(_translate("MainWindow", "Change book"))
