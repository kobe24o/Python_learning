# _*_ coding: utf-8 _*_
# @Time : 2022/5/6 9:26
# @Author : Michael
# @File : painter1.py
# @desc :
import sys

from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt

class drawing_demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("绘图示例")
        self.resize(300, 300)
        self.text = "Hello 麦克"

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)  # 开始绘制, 需要传入 self
        self.drawText(event, painter) # 自定义绘制
        painter.end()

    def drawText(self, event, painter):
        painter.setPen(QColor(168, 150, 3)) # 设置画笔颜色
        painter.setFont(QFont("SimSun", 20))  # 设置字体
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = drawing_demo()
    demo.show()
    sys.exit(app.exec_())