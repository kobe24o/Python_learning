# -*- coding: utf-8 -*-

"""
Module implementing MainWindow_child.
"""
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QFileDialog

from Ui_childform2 import ui_childform
from Ui_menu_bar_tool_bar import Ui_MainWindow


class MainWindow_withchild(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(MainWindow_withchild, self).__init__(parent)
        self.setupUi(self)

        self.child = my_childform() # 创建子窗口实例
        self.actionclose.triggered.connect(self.close)
        self.actionopen_O.triggered.connect(self.openMsg)
        self.addWinAction.triggered.connect(self.childshow)

    def childshow(self):
        self.gridlayout1.addWidget(self.child)
        self.child.show()

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files (*.txt)")
        # 在状态栏显示文件地址
        self.statusbar.showMessage(file)

class my_childform(QWidget, ui_childform):
    def __init__(self):
        super(my_childform, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow_withchild()
    win.show()
    sys.exit(app.exec_())
