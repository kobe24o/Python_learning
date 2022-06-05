# _*_ coding: utf-8 _*_
# @Time : 2022/5/30 0:53
# @Author : Michael
# @File : web_load.py
# @desc :
import os

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("load url")
        self.setGeometry(300, 300, 1000, 600)
        self.browser = QWebEngineView()
        # url = QUrl("D:/gitcode/Python_learning/qt/ch5/index.html")
        # self.browser.load(url)
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title></title>
        </head>
        <body>
            <h1>Hello michael</h1>
            <h1>Hello PyQt5 from setHtml</h1>
        </body>
        </html>
        """
        self.browser.setHtml(html)
        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())