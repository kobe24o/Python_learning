# _*_ coding: utf-8 _*_
# @Time : 2022/6/4 18:49
# @Author : Michael
# @File : hbox.py
# @desc :

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication


class Winform(QWidget):
    def __init__(self):
        super(Winform, self).__init__()
        self.setWindowTitle('HBox')

        layout = QHBoxLayout()
        layout.addWidget(QPushButton('1'), 2, Qt.AlignTop)
        layout.addWidget(QPushButton('2'), 0, Qt.AlignBottom | Qt.AlignRight)
        layout.addWidget(QPushButton('3'))
        layout.addWidget(QPushButton('4'), 3, Qt.AlignTop | Qt.AlignJustify) # 伸缩量3, 居中，两边对齐
        layout.addWidget(QPushButton('5'))
        layout.setSpacing(5)

        self.setLayout(layout)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())