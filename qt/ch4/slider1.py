# _*_ coding: utf-8 _*_
# @Time : 2022/5/5 8:20
# @Author : Michael
# @File : slider1.py
# @desc :
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSlider, QApplication
from PyQt5.QtCore import Qt


class slider_demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("滑块控件")
        self.resize(300, 100)

        layout = QVBoxLayout()

        self.label1 = QLabel('hello michael')
        self.label1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label1)

        self.slider1 = QSlider(Qt.Horizontal)  # 水平方向
        self.slider1.setMinimum(10)  # 最小值
        self.slider1.setMaximum(50)  # 最大值
        self.slider1.setSingleStep(3)  # 步长
        self.slider1.setValue(20)  # 当前值
        self.slider1.setTickPosition(QSlider.TicksBelow)  # 刻度位置
        self.slider1.setTickInterval(5)  # 刻度间隔
        layout.addWidget(self.slider1)

        self.slider1.valueChanged.connect(self.value_changed)

        self.setLayout(layout)

    def value_changed(self):
        print('当前滑块的值为：', self.slider1.value())
        size = self.slider1.value()
        self.label1.setFont(QFont('Arial', size))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    demo = slider_demo()
    demo.show()
    sys.exit(app.exec_())