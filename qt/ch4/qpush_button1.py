# _*_ coding: utf-8 _*_
# @Time : 2022/5/4 21:01
# @Author : Michael
# @File : qpush_button1.py
# @desc :

import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QApplication


class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QPushButton例子")
        layout = QVBoxLayout()

        self.button1 = QPushButton("Button1")
        self.button1.setCheckable(True)  # 设置按钮已经被选中，表示按钮保持已点击和释放状态
        self.button1.toggle()  # 切换按钮的状态
        self.button1.clicked.connect(lambda: self.whichButton(self.button1))
        self.button1.clicked.connect(self.btnstate)
        layout.addWidget(self.button1)

        self.button2 = QPushButton("image")
        self.button2.setIcon(QIcon(QPixmap("logo.png")))
        self.button2.clicked.connect(lambda: self.whichButton(self.button2))
        layout.addWidget(self.button2)

        self.button3 = QPushButton("disabled button")
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton("&Cancel")
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda: self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)

    def btnstate(self):
        if self.button1.isChecked():
            print("button1 is pressed")
        else:
            print("button1 is released")

    def whichButton(self, btn):
        print("clicked button is " + btn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Form()
    ui.show()
    sys.exit(app.exec_())