# _*_ coding: utf-8 _*_
# @Time : 2022/5/9 21:08
# @Author : Michael
# @File : list_view1.py
# @desc :
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QMessageBox, QApplication


class listViewDemo(QWidget):
    def __init__(self):
        super(listViewDemo, self).__init__()
        self.setWindowTitle("ListView例子")
        self.resize(300, 300)

        layout = QVBoxLayout()

        listview = QListView()

        str_list_model = QStringListModel()
        self.qList = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        str_list_model.setStringList(self.qList)

        listview.setModel(str_list_model)
        listview.clicked.connect(self.clicked)

        layout.addWidget(listview)
        self.setLayout(layout)
    def clicked(self, qModelIndex):
        QMessageBox.information(self, "title", "text:你选择了 " + self.qList[qModelIndex.row()])

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = listViewDemo()
    main.show()
    sys.exit(app.exec_())