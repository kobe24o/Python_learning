# _*_ coding: utf-8 _*_
# @Time : 2022/5/3 9:45
# @Author : Michael
# @File : screen_geometry1.py
# @desc :
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QPushButton, QToolTip
import sys

app = QApplication(sys.argv)
widget = QWidget()
QToolTip.setFont(QFont('SansSerif', 10))
widget.setToolTip('这是一个<b>气泡提示</b>')
btn = QPushButton('点击我', parent=widget)
btn.move(100, 50)
btn.resize(180, 30)
widget.resize(300, 300)
widget.move(150, 300)
widget.setWindowTitle('我的窗口')
# widget.setFixedWidth(300)  # 固定宽度
widget.setWindowIcon(QIcon('logo.png'))
widget.show()
print('w.x() = ', widget.x())
print('w.y() = ', widget.y())
print('w.width() = ', widget.width())
print('w.height() = ', widget.height())
print('w.geometry() = ', widget.geometry())
print('w.geometry().x() = ', widget.geometry().x())
print('w.geometry().y() = ', widget.geometry().y())
print('w.geometry().width() = ', widget.geometry().width())
print('w.geometry().height() = ', widget.geometry().height())
print('w.frameGeometry() = ', widget.frameGeometry())
print('w.frameGeometry().x() = ', widget.frameGeometry().x())
print('w.frameGeometry().y() = ', widget.frameGeometry().y())
print('w.frameGeometry().width() = ', widget.frameGeometry().width())
print('w.frameGeometry().height() = ', widget.frameGeometry().height())
print('w.pos() = ', widget.pos())
sys.exit(app.exec_())
