# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\gitcode\Python_learning\qt\ch1\menu_bar_tool_bar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# Ui_menu_bar_tool_bar.py

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 328)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 611, 441))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridlayout1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridlayout1.setContentsMargins(0, 0, 0, 0)
        self.gridlayout1.setObjectName("gridlayout1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 401, 26))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionopen_O = QtWidgets.QAction(MainWindow)
        self.actionopen_O.setObjectName("actionopen_O")
        self.actionnew_N = QtWidgets.QAction(MainWindow)
        self.actionnew_N.setObjectName("actionnew_N")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.addWinAction = QtWidgets.QAction(MainWindow)
        self.addWinAction.setObjectName("addWinAction")
        self.menu_F.addAction(self.actionopen_O)
        self.menu_F.addAction(self.actionnew_N)
        self.menu_F.addAction(self.actionclose)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.addWinAction)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu.setTitle(_translate("MainWindow", "编辑(E)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionopen_O.setText(_translate("MainWindow", "open(O)"))
        self.actionopen_O.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionnew_N.setText(_translate("MainWindow", "new(N)"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        self.addWinAction.setText(_translate("MainWindow", "添加窗体"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())