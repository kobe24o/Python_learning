# _*_ coding: utf-8 _*_
# @Time : 2022/5/4 22:43
# @Author : Michael
# @File : spin_box1.py
# @desc :
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpinBox, QDoubleSpinBox, QApplication
from PyQt5.QtCore import Qt


class spin_box1(QWidget):
    def __init__(self):
        super(spin_box1, self).__init__()

        self.setWindowTitle("SpinBox例子")
        self.resize(300, 100)

        layout = QVBoxLayout()

        self.lb1 = QLabel("当前得分：")
        self.lb1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lb1)

        self.spbox = QSpinBox()
        self.spbox.setRange(0, 100)
        self.spbox.setValue(60)
        self.spbox.setSingleStep(2)
        self.spbox.valueChanged.connect(self.value_change)
        layout.addWidget(self.spbox)

        self.lb2 = QLabel("当前平均分：")
        self.lb2.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lb2)

        self.spbox_double = QDoubleSpinBox()
        self.spbox_double.setRange(0.0, 100.0)
        self.spbox_double.setValue(60.0)
        self.spbox_double.setDecimals(2)
        self.spbox_double.setSingleStep(0.50)
        self.spbox_double.valueChanged.connect(self.value_change1)
        layout.addWidget(self.spbox_double)

        self.setLayout(layout)

    def value_change(self):
        self.lb1.setText("当前得分：" + str(self.spbox.value()))

    def value_change1(self):
        self.lb2.setText("当前平均分：" + str(self.spbox_double.value()))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = spin_box1()
    w.show()
    sys.exit(app.exec_())