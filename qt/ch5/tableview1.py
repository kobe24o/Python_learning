# _*_ coding: utf-8 _*_
# @Time : 2022/5/9 9:44
# @Author : Michael
# @File : tableview1.py
# @desc :
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout, QApplication, QHeaderView


class table_view(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("table_view")
        self.resize(500, 300)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["姓名", "年龄", "性别", "地址"])

        for r in range(4):
            for c in range(4):
                item = QStandardItem("row %s, col %s" % (r, c))
                self.model.setItem(r, c, item)
        # 添加数据
        self.model.appendRow([
            QStandardItem("张三"), QStandardItem("20"),
        ])
        self.model.appendRow([
            QStandardItem('李四'), QStandardItem("21"),
        ])

        self.tableview1 = QTableView()
        self.tableview1.setModel(self.model)
        self.tableview1.horizontalHeader().setStretchLastSection(True)
        self.tableview1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 表格填满窗口

        # 删除数据
        indexs = self.tableview1.selectionModel().selection().indexes()
        print(indexs)
        if len(indexs) > 0:
            index = indexs[0]
            self.model.removeRows(index.row(), 2)  # 删除两行
        index = self.tableview1.currentIndex()
        print(index, index.row(), index.column())
        self.model.removeRows(index.row()+1, 3)

        layout = QVBoxLayout()
        layout.addWidget(self.tableview1)
        self.setLayout(layout)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = table_view()
    win.show()
    sys.exit(app.exec_())
