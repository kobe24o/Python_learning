# _*_ coding: utf-8 _*_
# @Time : 2022/5/5 22:40
# @Author : Michael
# @File : file_dialog1.py
# @desc :
import time

from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QFileDialog, QApplication


class file_dialog1(QWidget):
    def __init__(self):
        super(file_dialog1, self).__init__()
        layout = QVBoxLayout()

        self.btn = QPushButton('加载图片')
        self.btn.clicked.connect(self.loadfile)
        layout.addWidget(self.btn)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.btn1 = QPushButton('加载文本文件')
        self.btn1.clicked.connect(self.loadfiles)
        layout.addWidget(self.btn1)

        self.content = QTextEdit() # 文本框
        layout.addWidget(self.content)

        self.setLayout(layout)
        self.setWindowTitle('文件对话框')

    def loadfile(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开文件', './', '图片文件(*.jpg *.png *gif)')
        self.label.setPixmap(QPixmap(fname))
    def loadfiles(self):
        dlog = QFileDialog()
        dlog.setFileMode(QFileDialog.AnyFile)
        dlog.setFilter(QDir.Files)

        if dlog.exec_():
            fnames = dlog.selectedFiles()
            print(fnames)
            with open(fnames[0], 'r', encoding='utf-8') as f:
                data = f.read()
                self.content.setText(data)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = file_dialog1()
    ui.show()
    sys.exit(app.exec_())