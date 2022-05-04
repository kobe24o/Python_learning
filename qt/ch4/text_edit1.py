# _*_ coding: utf-8 _*_
# @Time : 2022/5/4 19:24
# @Author : Michael
# @File : text_edit1.py
# @desc :
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QVBoxLayout, QApplication


class textEdit1(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('多行文本例子')
        self.resize(300, 200)
        self.textEdit = QTextEdit()
        self.btn1 = QPushButton('显示文本')
        self.btn2 = QPushButton('显示HTML')
        self.btn1.clicked.connect(self.btn1_clicked)
        self.btn2.clicked.connect(self.btn2_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        self.setLayout(layout)

    def btn1_clicked(self):
        self.textEdit.setPlainText('Hello Michael!')

    def btn2_clicked(self):
        self.textEdit.setHtml(
            "<font color='red' size='10'>Hello Michael!<br>点击按钮</font><br><br><br><br><a href='https://michael.blog.csdn.net/'>访问我的博客</a>")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = textEdit1()
    ui.show()
    sys.exit(app.exec_())