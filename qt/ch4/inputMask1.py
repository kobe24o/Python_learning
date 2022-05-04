# _*_ coding: utf-8 _*_
# @Time : 2022/5/4 15:48
# @Author : Michael
# @File : inputMask1.py
# @desc :
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit


class inputmask(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("输入掩码")

        layout = QFormLayout()
        ip_lineEdit = QLineEdit()
        mac_lineEdit = QLineEdit()
        date_lineEdit = QLineEdit()
        licence_lineEdit = QLineEdit()

        ip_lineEdit.setInputMask("000.000.000.000;_")
        mac_lineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        date_lineEdit.setInputMask("0000-00-00")
        licence_lineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        layout.addRow("IP地址", ip_lineEdit)
        layout.addRow("MAC地址", mac_lineEdit)
        layout.addRow("日期", date_lineEdit)
        layout.addRow("许可证", licence_lineEdit)

        self.setLayout(layout)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = inputmask()
    win.show()
    sys.exit(app.exec_())