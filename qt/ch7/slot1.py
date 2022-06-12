# _*_ coding: utf-8 _*_
# @Time : 2022/6/11 15:13
# @Author : Michael
# @File : slot1.py
# @desc :

from PyQt5.QtWidgets import QPushButton, QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox
import sys

app = QApplication(sys.argv)
widget = QWidget()


def showMsg():
    QMessageBox.information(widget, '信息提示框', 'ok, 弹出消息框')


btn = QPushButton('测试点击按钮', widget)
btn.clicked.connect(showMsg)
widget.show()
sys.exit(app.exec_())
