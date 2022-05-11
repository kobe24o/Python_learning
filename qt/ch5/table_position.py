# _*_ coding: utf-8 _*_
# @Time : 2022/5/10 9:48
# @Author : Michael
# @File : table_position.py
# @desc :
from PyQt5.QtGui import QBrush, QColor, QFont, QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem, QApplication, QMenu
from PyQt5.QtCore import Qt, QSize


class table_position(QWidget):
    def __init__(self):
        super(table_position, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Table Position")
        self.resize(300, 200)

        layout = QHBoxLayout()

        tablewidget = QTableWidget()
        tablewidget.setRowCount(30)
        tablewidget.setColumnCount(4)

        layout.addWidget(tablewidget)

        for i in range(30):
            for j in range(4):
                itemContent = f'{i},{j}'
                tablewidget.setItem(i, j, QTableWidgetItem(itemContent))
        self.setLayout(layout)

        # 遍历表格查找指定内容
        text = '10,1'
        items = tablewidget.findItems(text, Qt.MatchExactly)
        item = items[0]
        # 选中单元格
        item.setSelected(True)
        # 设置背景颜色
        item.setForeground(QBrush(QColor(255, 0, 0)))

        row = item.row()
        # 鼠标滚轮定位到第11行
        tablewidget.verticalScrollBar().setSliderPosition(row)

        # 设置颜色
        newitem = QTableWidgetItem('new')
        newitem.setForeground(QBrush(QColor(0, 255, 0)))
        tablewidget.setItem(10, 1, newitem)

        # 加粗字体
        newitem = QTableWidgetItem("new")
        newitem.setFont(QFont("Times", 20, QFont.Bold))
        tablewidget.setItem(10, 2, newitem)

        # 排序
        tablewidget.sortItems(2, Qt.DescendingOrder)  # 2 列，降序

        # 文本对齐方式
        newitem = QTableWidgetItem("michael")
        newitem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        tablewidget.setItem(10, 3, newitem)

        # 合并单元格
        tablewidget.setSpan(0, 0, 3, 1)  # 0,0 位置 占据 3行 1列
        tablewidget.setItem(0, 0, QTableWidgetItem("michael"))
        tablewidget.setItem(1, 0, QTableWidgetItem("hello"))  # 被占了，无效

        # 设置单元格大小
        tablewidget.setColumnWidth(0, 300)  # 0列 300宽
        tablewidget.setRowHeight(0, 150)  # 0行 150高

        # 不显示分割线
        tablewidget.setShowGrid(False)

        ## 放置图片，调整大小
        newitem = QTableWidgetItem(QIcon('../store.png'), "微软商店")
        tablewidget.setItem(10, 3, newitem)
        tablewidget.setIconSize(QSize(100, 100))

        # 获取单元格内容
        tablewidget.itemClicked.connect(self.handleItemClicked)

        def generateMenu(pos):
            row_num = -1
            for i in tablewidget.selectionModel().selection().indexes():
                row_num = i.row()

                menu = QMenu()
                item1 = menu.addAction("删除")
                item2 = menu.addAction("修改")
                item3 = menu.addAction("添加")
                action = menu.exec_(tablewidget.mapToGlobal(pos))
                if action == item1:
                    print(f"选中了删除，行号：{row_num}")
                elif action == item2:
                    print(f"选中了修改，行号：{row_num}")
                elif action == item3:
                    print(f"选中了添加，行号：{row_num}")

        # 允许右键菜单
        tablewidget.setContextMenuPolicy(Qt.CustomContextMenu)
        tablewidget.customContextMenuRequested.connect(generateMenu)



    def handleItemClicked(self, item):
        print('你点击了' + item.text())

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = table_position()
    window.show()
    sys.exit(app.exec_())
