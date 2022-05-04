# _*_ coding: utf-8 _*_
# @Time : 2022/5/4 21:34
# @Author : Michael
# @File : radio_button1.py
# @desc :
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QRadioButton, QApplication


class radio_button(QWidget):
    def __init__(self):
        super(radio_button, self).__init__()
        layout = QHBoxLayout()

        self.button1 = QRadioButton("Button1")
        self.button1.setChecked(True) # 默认选中
        self.button1.toggled.connect(lambda: self.btnstate(self.button1))
        layout.addWidget(self.button1)

        self.button2 = QRadioButton("Button2")
        self.button2.toggled.connect(lambda: self.btnstate(self.button2))
        layout.addWidget(self.button2)

        self.setLayout(layout)
        self.setWindowTitle("RadioButton例子")

    def btnstate(self, btn):
        if btn.text() == "Button1":
            if btn.isChecked():
                print("Button1 is selected")
            else:
                print("Button1 is deselected")
        elif btn.text() == "Button2":
            if btn.isChecked():
                print("Button2 is selected")
            else:
                print("Button2 is deselected")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    example = radio_button()
    example.show()
    sys.exit(app.exec_())