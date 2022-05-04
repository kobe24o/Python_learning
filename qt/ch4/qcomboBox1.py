# _*_ coding: utf-8 _*_
# @Time : 2022/5/4 22:19
# @Author : Michael
# @File : qcomboBox1.py
# @desc :
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QApplication


class combo_box1(QWidget):
    def __init__(self):
        super(combo_box1, self).__init__()

        self.setWindowTitle("combo_box例子")
        self.resize(300, 200)
        layout = QVBoxLayout()

        self.label1 = QLabel("选择语言")

        self.cb = QComboBox()
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItem("Python")
        self.cb.addItems(["Java", "C#", "PHP"])
        self.cb.currentIndexChanged.connect(self.selectionchange)

        layout.addWidget(self.label1)
        layout.addWidget(self.cb)
        self.setLayout(layout)

    def selectionchange(self):
        self.label1.setText("你选择的语言是：" + self.cb.currentText())
        print('items in the list are:')
        for i in range(self.cb.count()):
            print(f'item {i} = {self.cb.itemText(i)}')
            print(f'current idx {i} selection changed to {self.cb.currentIndex()}')
        print('-'*10)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    combo_box1 = combo_box1()
    combo_box1.show()
    sys.exit(app.exec_())