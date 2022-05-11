# _*_ coding: utf-8 _*_
# @Time : 2022/5/9 21:39
# @Author : Michael
# @File : tablewidgetDemo.py
# @desc :
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem, QApplication, QHeaderView, QComboBox, \
    QPushButton


class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("TableWidget例子")
        self.resize(500, 300)

        layout = QHBoxLayout()

        tablewidget = QTableWidget(4, 3)  # 行，列
        # tablewidget.setRowCount(4)
        # tablewidget.setColumnCount(3)

        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(["姓名", "性别", "体重(kg)"])
        tablewidget.setVerticalHeaderLabels(["1行", "2行", "3行", "4行哦"])
        # 表根据界面宽度自动伸缩
        tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 禁止编辑
        # tablewidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # 默认选中整行
        tablewidget.setSelectionBehavior(QTableWidget.SelectRows)
        # 设置宽高度匹配内容
        tablewidget.resizeColumnsToContents()
        # tablewidget.resizeRowsToContents()
        # 表格头的显示
        tablewidget.horizontalHeader().setVisible(False)
        tablewidget.verticalHeader().setVisible(False)

        tablewidget.setItem(0, 0, QTableWidgetItem("张三"))
        tablewidget.setItem(0, 1, QTableWidgetItem("男"))
        tablewidget.setItem(0, 2, QTableWidgetItem("150"))

        # 添加控件
        combox = QComboBox()
        combox.addItem("男")
        combox.addItem("女")
        combox.setStyleSheet("QComboBox{margin:3px width:80px;}")
        tablewidget.setCellWidget(1, 1, combox)

        btn = QPushButton("保存")
        btn.setDown(True)
        btn.setStyleSheet("QPushButton{margin:20px width:20px;}")
        tablewidget.setCellWidget(1, 2, btn)

        self.setLayout(layout)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main = TableWidgetDemo()
    main.show()
    sys.exit(app.exec_())
