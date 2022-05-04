# _*_ coding: utf-8 _*_
# @Time : 2022/5/4 14:26
# @Author : Michael
# @File : line_edit1.py
# @desc :

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QFormLayout
import sys

class lineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("lineEditDemo")

        layout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        layout.addRow("Normal LineEdit", normalLineEdit)
        layout.addRow("No Echo LineEdit", noEchoLineEdit)
        layout.addRow("Password LineEdit", passwordLineEdit)
        layout.addRow("Password Echo On Edit LineEdit", passwordEchoOnEditLineEdit)

        normalLineEdit.setPlaceholderText("Normal LineEdit")
        noEchoLineEdit.setPlaceholderText("No Echo LineEdit")
        passwordLineEdit.setPlaceholderText("Password LineEdit")
        passwordEchoOnEditLineEdit.setPlaceholderText("Password Echo On Edit LineEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(layout)
if __name__=='__main__':
    app = QApplication(sys.argv)
    main = lineEditDemo()
    main.show()
    sys.exit(app.exec_())