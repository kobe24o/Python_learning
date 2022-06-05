# _*_ coding: utf-8 _*_
# @Time : 2022/6/4 19:04
# @Author : Michael
# @File : addStretch.py
# @desc :
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import sys

class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn1.setText('button 1')
        btn2.setText('button 2')
        btn3.setText('button 3')

        layout = QHBoxLayout()
        # 设置伸缩量为2
        layout.addStretch(2)
        layout.addWidget(btn1)
        # 设置伸缩量为1
        layout.addStretch(1)
        layout.addWidget(btn2)
        # 设置伸缩量为1
        layout.addStretch(1)
        layout.addWidget(btn3)
        # 设置伸缩量为1
        layout.addStretch(1)
        # 剩余空间比例 2:1:1:1
        self.setLayout(layout)
        self.setWindowTitle("addStretch 例子")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.show()
    sys.exit(app.exec_())
