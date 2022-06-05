# _*_ coding: utf-8 _*_
# @Time : 2022/6/5 17:31
# @Author : Michael
# @File : qsplitter.py
# @desc :
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QSplitter, QTextEdit, QApplication


class qsplitter_demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('QSplitter')

        h_layout = QHBoxLayout(self)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        textedit = QTextEdit()

        spliter1 = QSplitter(Qt.Horizontal)
        spliter1.addWidget(topleft)
        spliter1.addWidget(textedit)
        spliter1.setSizes([100, 200])

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        spliter2 = QSplitter(Qt.Vertical)
        spliter2.addWidget(spliter1)
        spliter2.addWidget(bottom)

        h_layout.addWidget(spliter2)
        self.setLayout(h_layout)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    qsplitter_demo = qsplitter_demo()
    qsplitter_demo.show()
    sys.exit(app.exec_())