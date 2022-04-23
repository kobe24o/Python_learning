# -*- coding: utf-8 -*-
# menu_bar_tool_bar.py
"""
Module implementing MainWindow.
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from Ui_menu_bar_tool_bar import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionclose.triggered.connect(self.on_actionclose_triggered)
        self.actionopen_O.triggered.connect(self.on_actionopen_O_triggered)
    
    @pyqtSlot()
    def on_actionnew_N_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionclose_triggered(self):
        """
        Slot documentation goes here.
        """
        self.statusbar.showMessage("再见！")
    
    @pyqtSlot()
    def on_actionopen_O_triggered(self):
        """
        Slot documentation goes here.
        """
        file,  ok = QFileDialog.getOpenFileName(self,  "打开",  "D:/",  "ALL Files(*);; Text Files(*TxT)")
        self.statusbar.showMessage(file)

if __name__  == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
