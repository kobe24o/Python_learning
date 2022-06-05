# _*_ coding: utf-8 _*_
# @Time : 2022/5/30 0:25
# @Author : Michael
# @File : thread_stuck.py
# @desc :
import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton

global sec
sec = 0


def setTime():
    global sec
    sec += 1
    # LED显示数字+1
    lcdNumber.display(sec)

def work():
    # 计时器每秒计数
    timer.start(1000)
    for i in range(2000000000):
        QApplication.processEvents()
        pass

    timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget()
    win.resize(300, 120)

    # 垂直布局类QVBoxLayout
    layout = QVBoxLayout(win)
    # 加个显示屏
    lcdNumber = QLCDNumber()
    layout.addWidget(lcdNumber)
    button = QPushButton("测试")
    layout.addWidget(button)

    timer = QTimer()
    # 每次计时结束，触发setTime
    timer.timeout.connect(setTime)
    button.clicked.connect(work)

    win.show()
    sys.exit(app.exec_())
