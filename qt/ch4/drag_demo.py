# _*_ coding: utf-8 _*_
# @Time : 2022/5/6 23:36
# @Author : Michael
# @File : drag_demo.py
# @desc :
from PyQt5.QtWidgets import QComboBox, QWidget, QFormLayout, QLabel, QLineEdit, QApplication


class combo(QComboBox):
    def __init__(self, title, parent):
        super(combo, self).__init__(parent)
        self.setAcceptDrops(True)
    def dragEnterEvent(self, e):  # 重写dragEnterEvent方法
        print(e, e.mimeData().text())
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QFormLayout()

        label = QLabel('把左边的文本拖拽到右边的下拉框中')
        layout.addRow(label)
        edit1 = QLineEdit("我是一个文本框")
        edit1.setDragEnabled(True)
        com = combo('button', self)
        layout.addRow(edit1, com)

        self.setLayout(layout)
        self.setWindowTitle('拖拽')
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())