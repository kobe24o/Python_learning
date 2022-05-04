# _*_ coding: utf-8 _*_
# @Time : 2022/5/4 16:22
# @Author : Michael
# @File : text_example.py
# @desc :
from PyQt5.QtGui import QIntValidator, QFont, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLineEdit, QFormLayout
from PyQt5.QtCore import Qt


class lineEdit_demo(QWidget):
    def __init__(self):
        super(lineEdit_demo, self).__init__()

        e1 = QLineEdit()
        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        e1.setAlignment(Qt.AlignRight)
        e1.setFont(QFont("Arial", 20))

        e2 = QLineEdit()
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        layout = QFormLayout()
        layout.addRow("整数验证器", e1)
        layout.addRow("浮点数验证器", e2)

        e3 = QLineEdit()
        e3.setInputMask("+99_9999_999999")

        layout.addRow("输入掩码", e3)

        e4 = QLineEdit()
        e4.textChanged.connect(self.text_changed)

        layout.addRow("文本改变", e4)

        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)
        e5.editingFinished.connect(self.enterPress)

        layout.addRow("密码模式", e5)

        e6 = QLineEdit("Hello world, michael")
        e6.setReadOnly(True)

        layout.addRow("只读", e6)

        self.setLayout(layout)
        self.setWindowTitle("QLineEdit控件")

    def text_changed(self, text):
        print('输入的内容：', text)

    def enterPress(self):
        print("已输入内容")


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    main = lineEdit_demo()
    main.show()
    sys.exit(app.exec_())