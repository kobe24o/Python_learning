# _*_ coding: utf-8 _*_
# @Time : 2022/5/6 9:56
# @Author : Michael
# @File : draw_point.py
# @desc :
import math

from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt


class drawPoint(QWidget):
    def __init__(self):
        super(drawPoint, self).__init__()
        self.setWindowTitle("绘制点")
        self.resize(500, 300)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)  # 必须加 self 参数
        self.drawpoint(painter)
        painter.end()

    def drawpoint(self, painter):
        painter.setPen(Qt.red)
        size = self.size()
        print('size,', size)
        for i in range(1000):
            # 绘制正弦函数曲线
            x = int(100*(-1+2.0*i/1000)+size.width()/2)
            y = int(-50*math.sin((x-size.width()/2)*math.pi/50)+size.height()/2)
            painter.drawPoint(x, y)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = drawPoint()
    main.show()
    sys.exit(app.exec_())
