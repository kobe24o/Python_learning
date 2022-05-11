# _*_ coding: utf-8 _*_
# @Time : 2022/5/9 21:20
# @Author : Michael
# @File : listWidgetDemo.py
# @desc :
from PyQt5.QtWidgets import QListWidget, QMessageBox, QApplication


class ListWidgetDemo(QListWidget):
    def clicked(self, item):
        QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    listwidget = ListWidgetDemo()
    listwidget.resize(300, 200)
    listwidget.addItem("item 1")
    listwidget.addItem("item 2")
    listwidget.addItem("item 3")
    listwidget.addItem("item 4")
    listwidget.setWindowTitle("ListWidget Demo")
    listwidget.itemClicked.connect(listwidget.clicked)
    listwidget.show()
    sys.exit(app.exec_())
