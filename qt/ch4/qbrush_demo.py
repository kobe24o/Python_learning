# _*_ coding: utf-8 _*_
# @Time : 2022/5/6 22:58
# @Author : Michael
# @File : qbrush_demo.py
# @desc :

import sys

from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QFont
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect


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
        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 15, 90, 60)
        painter.setPen(QColor(168, 150, 3))  # 设置画笔颜色
        painter.setFont(QFont("SimSun", 7))  # 设置字体
        painter.drawText(QRect(10, 65, 90, 60), Qt.AlignCenter, 'SolidPattern')

        brush.setStyle(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 15, 90, 60)
        painter.setPen(QColor(168, 150, 3))
        painter.setFont(QFont("SimSun", 7))
        painter.drawText(QRect(130, 65, 90, 60), Qt.AlignCenter, 'Dense1Pattern')

        brush.setStyle(Qt.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 15, 90, 60)
        painter.setPen(QColor(168, 150, 3))
        painter.setFont(QFont("SimSun", 7))
        painter.drawText(QRect(250, 65, 90, 60), Qt.AlignCenter, 'Dense2Pattern')

        brush.setStyle(Qt.Dense3Pattern)
        painter.setBrush(brush)
        painter.drawRect(10, 285, 90, 60)
        painter.setPen(QColor(168, 150, 3))
        painter.setFont(QFont("SimSun", 7))
        painter.drawText(QRect(10, 335, 90, 60), Qt.AlignCenter, 'Dense3Pattern')

        brush.setStyle(Qt.DiagCrossPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 105, 90, 60)
        painter.setPen(QColor(168, 150, 3))
        painter.setFont(QFont("SimSun", 7))
        painter.drawText(QRect(10, 155, 120, 60), Qt.AlignCenter, 'DiagCrossPattern')

        brush.setStyle(Qt.Dense5Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 105, 90, 60)
        painter.setPen(QColor(168, 150, 3))
        painter.setFont(QFont("SimSun", 7))
        painter.drawText(QRect(130, 155, 90, 60), Qt.AlignCenter, 'Dense5Pattern')

        brush.setStyle(Qt.Dense6Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 105, 90, 60)
        painter.setPen(QColor(168, 150, 3))
        painter.setFont(QFont("SimSun", 7))
        painter.drawText(QRect(250, 155, 90, 60), Qt.AlignCenter, 'Dense6Pattern')

        brush.setStyle(Qt.HorPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 195, 90, 60)
        painter.setPen(QColor(168, 150, 3))
        painter.setFont(QFont("SimSun", 7))
        painter.drawText(QRect(10, 245, 90, 60), Qt.AlignCenter, 'HorPattern')

        brush.setStyle(Qt.VerPattern)
        painter.setBrush(brush)
        painter.drawRect(130, 195, 90, 60)
        painter.setPen(QColor(168, 150, 3))
        painter.setFont(QFont("SimSun", 7))
        painter.drawText(QRect(130, 245, 90, 60), Qt.AlignCenter, 'VerPattern')

        brush.setStyle(Qt.BDiagPattern)
        painter.setBrush(brush)
        painter.drawRect(250, 195, 90, 60)
        painter.setPen(QColor(168, 150, 3))
        painter.setFont(QFont("SimSun", 7))
        painter.drawText(QRect(250, 245, 90, 60), Qt.AlignCenter, 'BDiagPattern')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qpenDemo()
    ex.show()
    sys.exit(app.exec_())