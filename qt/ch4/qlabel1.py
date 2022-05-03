# _*_ coding: utf-8 _*_
# @Time : 2022/5/3 13:45
# @Author : Michael
# @File : qlabel1.py
# @desc :
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication


class window_qlabel(QWidget):
    def __init__(self):
        super().__init__()

        label1 = QLabel()
        label2 = QLabel()
        label3 = QLabel()
        label4 = QLabel()

        label1.setText("<font color=red>这是一个红色的文本</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue) # 设置背景色
        label1.setPalette(palette) # 设置背景色
        label1.setAlignment(Qt.AlignCenter) # 设置文本对齐方式
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse) # 设置文本可选

        label2.setText("<a href='#'>michael 学习 PyQt</a>")
        label2.linkActivated.connect(self.link_clicked) # 连接鼠标点击信号

        label4.setText("<a href='http://michael.blog.csdn.net'>michael的博客</a>")
        label4.setOpenExternalLinks(True) # 设置打开外部链接
        label4.setToolTip("欢迎访问！") # 设置鼠标悬停提示
        label4.linkHovered.connect(self.link_hovered) # 连接鼠标悬停信号

        label3.setAlignment(Qt.AlignCenter) # 设置文本对齐方式
        label3.setToolTip('提示：这是一张图片哦') # 设置鼠标悬停提示
        label3.setPixmap(QPixmap('logo.png'))   # 设置图片

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel 示例")

    def link_hovered(self):
        print("鼠标悬停")

    def link_clicked(self):
        print("鼠标点击")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = window_qlabel()
    win.show()
    sys.exit(app.exec_())
