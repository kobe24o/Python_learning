# _*_ coding: utf-8 _*_
# @Time : 2022/6/11 17:40
# @Author : Michael
# @File : signal2.py
# @desc :
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class win(QWidget):
    button_clicked_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle('内置信号与槽')
        self.resize(200, 300)
        btn = QPushButton('X', self)
        btn.clicked.connect(self.btn_click)
        self.button_clicked_signal.connect(self.close)
    def btn_click(self):
        self.button_clicked_signal.emit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = win()
    w.show()
    sys.exit(app.exec_())