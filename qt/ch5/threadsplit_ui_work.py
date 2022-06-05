# _*_ coding: utf-8 _*_
# @Time : 2022/5/30 0:37
# @Author : Michael
# @File : threadsplit_ui_work.py
# @desc :
import sys

from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton

global sec
sec = 0


class WorkThread(QThread):
    trigger = pyqtSignal()

    def __int__(self):
        super(WorkThread, self).__init__()

    def run(self):
        for i in range(2000000000):
            pass

        # 循环完毕后发出信号
        self.trigger.emit()


def countTime():
    global sec
    sec += 1
    # LED显示数字+1
    lcdNumber.display(sec)


def work():
    # 计时器每秒计数
    timer.start(1000)
    # 计时开始
    workThread.start()
    # 当获得循环完毕的信号时，停止计数
    workThread.trigger.connect(timeStop)


def timeStop():
    timer.stop()
    print("运行结束用时", lcdNumber.value())
    global sec
    sec = 0


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
    workThread = WorkThread()

    button.clicked.connect(work)
    # 每次计时结束，触发 countTime
    timer.timeout.connect(countTime)

    win.show()
    sys.exit(app.exec_())