# _*_ coding: utf-8 _*_
# @Time : 2022/6/1 0:06
# @Author : Michael
# @File : webjs2.py
# @desc :
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWebChannel import QWebChannel
import sys


from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import QWidget, QMessageBox


class MySharedObject(QWidget):

    def __init__(self):
        super(MySharedObject, self).__init__()

    def _getStrValue(self):
        #
        return '100'

    def _setStrValue(self, str):
        #
        print('获得页面参数 ：%s' % str)
        QMessageBox.information(self, "Information", '获得页面参数 ：%s' % str)

    # 需要定义对外暴露的方法
    strValue = pyqtProperty(str, fget=_getStrValue, fset=_setStrValue)

# 创建一个 application实例
app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('Web页面中的JavaScript与 QWebEngineView交互例子')

# 创建一个垂直布局器
layout = QVBoxLayout()
win.setLayout(layout)

# 创建一个 QWebEngineView 对象
view = QWebEngineView()
htmlUrl = 'http://localhost:63342/Python_learning/qt/ch5/web/index.html'
view.load(QUrl(htmlUrl))

# 创建一个 QWebChannel对象，用来传递pyqt参数到JavaScript
channel = QWebChannel()
myObj = MySharedObject()
channel.registerObject("bridge", myObj)
view.page().setWebChannel(channel)

# 把QWebView和button加载到layout布局中
layout.addWidget(view)

# 显示窗口和运行app
win.show()
sys.exit(app.exec_())