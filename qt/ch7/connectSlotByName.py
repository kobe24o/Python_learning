# _*_ coding: utf-8 _*_
# @Time : 2022/6/12 16:24
# @Author : Michael
# @File : connectSlotByName.py
# @desc :
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import sys


class CustWidget(QWidget):
    def __init__(self):
        super(CustWidget, self).__init__()

        self.okButton = QPushButton("OK", self)
        # 使用setObjectName设置对象名称
        self.okButton.setObjectName("okButton_1")
        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        self.setLayout(layout)
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    def on_okButton_1_clicked(self): # 跟 setObjectName("okButton_1") 中的参数字符串保持一致
        print("点击了OK按钮")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CustWidget()
    win.show()
    sys.exit(app.exec_())
