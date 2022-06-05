# _*_ coding: utf-8 _*_
# @Time : 2022/6/5 17:11
# @Author : Michael
# @File : nest_layout1.py
# @desc :
import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QPushButton, QLineEdit, \
    QApplication


class mywin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('nest_layout1')
        self.resize(500, 300)

        # 全局部件, 注意 self 参数
        globalwidget = QWidget(self)

        # 全局布局
        globallayout = QHBoxLayout(globalwidget)

        # 局部布局
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        g_layout = QGridLayout()
        form_layout = QFormLayout()

        # 局部布局 添加控件
        h_layout.addWidget(QPushButton(str(1)))
        h_layout.addWidget(QPushButton(str(2)))
        v_layout.addWidget(QPushButton(str(3)))
        v_layout.addWidget(QPushButton(str(4)))
        g_layout.addWidget(QPushButton(str(5)), 0, 0)
        g_layout.addWidget(QPushButton(str(6)), 0, 1)
        g_layout.addWidget(QPushButton(str(7)), 1, 0)
        g_layout.addWidget(QPushButton(str(8)), 1, 1)
        g_layout.addWidget(QPushButton(str(9)), 2, 0)
        g_layout.addWidget(QPushButton(str(10)), 2, 1)
        form_layout.addRow('name', QLineEdit())
        form_layout.addRow('age', QLineEdit())

        # 局部布局 添加到 全局布局
        globallayout.addLayout(h_layout)
        globallayout.addLayout(v_layout)
        globallayout.addLayout(g_layout)
        globallayout.addLayout(form_layout)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mywin()
    win.show()
    sys.exit(app.exec_())