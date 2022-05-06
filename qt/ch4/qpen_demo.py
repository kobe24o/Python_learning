# _*_ coding: utf-8 _*_
# @Time : 2022/5/6 22:28
# @Author : Michael
# @File : qpen_demo.py
# @desc :
import sys

from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt


class qpenDemo(QWidget):
    def __init__(self):
        super(qpenDemo, self).__init__()
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle("钢笔样式")

    def paintEvent(self, event):  # paintEvent 名字大小写需要一致，重写父类的方法
        painter = QPainter()
        painter.begin(self)  # 需要加入self
        self.drawlines(painter)
        painter.end()

    def drawlines(self, painter):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qpenDemo()
    ex.show()
    sys.exit(app.exec_())