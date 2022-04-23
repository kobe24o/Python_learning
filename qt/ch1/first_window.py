# _*_ coding: utf-8 _*_
# @Time : 2022/4/4 23:26
# @Author : Michael
# @File : first_window.py
# @desc :
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class winform(QWidget):
    def __init__(self, parent=None):
        super(winform, self).__init__(parent)
        self.setGeometry(100, 100, 700, 350) # 窗口左上角的坐标，窗口宽高
        self.setWindowTitle('第一个窗口')
        quit = QPushButton('点击退出', self)
        quit.setGeometry(20, 10, 100, 35)
        quit.setStyleSheet("background-color: brown")
        quit.clicked.connect(self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = winform()
    win.show()
    sys.exit(app.exec_())