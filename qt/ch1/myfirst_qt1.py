# _*_ coding: utf-8 _*_
# @Time : 2022/4/4 23:11
# @Author : Michael
# @File : myfirst_qt1.py
# @desc :

# 安装 pip install pyqt5, pyqt5-tools
import sys
from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle('hello Michael, First Qt 应用')
widget.show()
sys.exit(app.exec_())