# _*_ coding: utf-8 _*_
# @Time : 2022/5/29 23:42
# @Author : Michael
# @File : qtimer_demo.py
# @desc :

from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import QWidget, QListWidget, QLabel, QPushButton, QGridLayout, QApplication


class QtimerDemo(QWidget):
    def __init__(self):
        super(QtimerDemo, self).__init__()
        self.setWindowTitle("QTimer Demo")
        self.listFile = QListWidget()
        self.label = QLabel('显示当前时间')
        self.startBtn = QPushButton('开始')
        self.stopBtn = QPushButton('停止')
        layout = QGridLayout()

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)

        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0, 1, 2)
        layout.addWidget(self.stopBtn, 2, 0, 1, 2)

        self.startBtn.clicked.connect(self.startTimer)
        self.stopBtn.clicked.connect(self.stopTimer)

        self.setLayout(layout)

    def startTimer(self):
        self.timer.start(1000) # 每隔1秒触发一次
        self.startBtn.setEnabled(False)
        self.stopBtn.setEnabled(True)

    def stopTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.stopBtn.setEnabled(False)

    def showTime(self):
        time = QDateTime().currentDateTime()
        timedisplay = time.toString('yyyy-MM-dd hh:mm:ss')
        self.label.setText(timedisplay)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = QtimerDemo()
    win.show()
    sys.exit(app.exec_())