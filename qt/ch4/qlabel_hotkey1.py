# _*_ coding: utf-8 _*_
# @Time : 2022/5/4 9:10
# @Author : Michael
# @File : qlabel_hotkey1.py
# @desc :

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QDialog, QLineEdit, QPushButton, QGridLayout


class Qlabel_hotkey1(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel_hotkey1 demo")
        nameLabel1 = QLabel("&Name") # 必须加& 否则不能绑定快捷键
        nameLineEdit1 = QLineEdit()
        nameLabel1.setBuddy(nameLineEdit1) # 设置名称标签和输入框的关联

        nameLabel2 = QLabel("&Password")
        nameLineEdit2 = QLineEdit()
        nameLabel2.setBuddy(nameLineEdit2)

        submit_btn = QPushButton("&Submit")
        cancel_btn = QPushButton("&cancel")
        layout = QGridLayout(self)
        layout.addWidget(nameLabel1, 0, 0)
        layout.addWidget(nameLineEdit1, 0, 1, 1, 2)

        layout.addWidget(nameLabel2, 1, 0)
        layout.addWidget(nameLineEdit2, 1, 1, 1, 2)

        layout.addWidget(submit_btn, 2, 1)
        layout.addWidget(cancel_btn, 2, 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Qlabel_hotkey1()
    w.show()
    sys.exit(app.exec_())