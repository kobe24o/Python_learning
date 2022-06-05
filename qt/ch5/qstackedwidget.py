# _*_ coding: utf-8 _*_
# @Time : 2022/5/29 21:16
# @Author : Michael
# @File : qstackedwidget.py
# @desc :
import sys

from PyQt5.QtWidgets import QWidget, QListWidget, QStackedWidget, QHBoxLayout, QApplication, QLabel, QCheckBox, \
    QLineEdit, QRadioButton, QFormLayout


class qstackedwidget_demo(QWidget):
    def __init__(self):
        super(qstackedwidget_demo, self).__init__()
        self.setWindowTitle("QStackedWidget控件")
        self.setGeometry(100, 100, 800, 600)

        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, "联系方式")
        self.leftlist.insertItem(1, "个人信息")
        self.leftlist.insertItem(2, "教育经历")

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hbox = QHBoxLayout()
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)

    def stack1UI(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.stack1.setLayout(layout)

    def stack2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        layout.addRow(QLabel("性别"), sex)
        layout.addRow("生日", QLineEdit())
        self.stack2.setLayout(layout)

    def stack3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.stack3.setLayout(layout)

    def display(self, i):
        self.stack.setCurrentIndex(i)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = qstackedwidget_demo()
    demo.show()
    sys.exit(app.exec_())
