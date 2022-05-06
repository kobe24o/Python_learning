# _*_ coding: utf-8 _*_
# @Time : 2022/5/6 23:20
# @Author : Michael
# @File : qpixmap.py
# @desc :
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    label1 = QLabel()
    label1.setPixmap(QPixmap('logo.png'))
    vbox = QVBoxLayout()
    vbox.addWidget(label1)
    win.setLayout(vbox)
    win.setWindowTitle('QPixmap')
    win.show()
    sys.exit(app.exec_())