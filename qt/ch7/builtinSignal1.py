# _*_ coding: utf-8 _*_
# @Time : 2022/6/11 15:45
# @Author : Michael
# @File : builtinSignal1.py
# @desc :

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class win(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('内置信号与槽')
        self.resize(200, 300)
        btn = QPushButton('X', self)
        btn.clicked.connect(self.shutdown)
    def shutdown(self):
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = win()
    w.show()
    sys.exit(app.exec_())
