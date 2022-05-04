# _*_ coding: utf-8 _*_
# @Time : 2022/5/4 15:23
# @Author : Michael
# @File : validator1.py
# @desc :
from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
import sys

class lineEditDemo1(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('lineEditDemo1 验证器')
        layout = QFormLayout()
        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        layout.addRow('整数', intLineEdit)
        layout.addRow('浮点数', doubleLineEdit)
        layout.addRow('字母和数字', validatorLineEdit)

        intLineEdit.setPlaceholderText('整数')
        doubleLineEdit.setPlaceholderText('浮点数')
        validatorLineEdit.setPlaceholderText('字母和数字')

        intValidator = QIntValidator(self)
        intValidator.setRange(1,99)

        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-100, 100)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)

        regValidator = QRegExpValidator(QRegExp('[a-zA-Z0-9]+$'), self)

        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(regValidator)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = lineEditDemo1()
    main.show()
    sys.exit(app.exec_())