# _*_ coding: utf-8 _*_
# @Time : 2022/5/29 23:56
# @Author : Michael
# @File : qtimer_demo2.py
# @desc :
import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel('<font color=red size=40>Hello World, 3秒后会消失</font>')
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint) # 无边框窗口
    label.show()

    QTimer.singleShot(3000, app.quit) # 一次性定时器，可模仿程序启动画面
    sys.exit(app.exec_())