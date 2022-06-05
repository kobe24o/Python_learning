# _*_ coding: utf-8 _*_
# @Time : 2022/6/4 22:45
# @Author : Michael
# @File : grid2.py
# @desc :
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication


class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.initUI()

    def initUI(self):
        titleLabel = QLabel('标题')
        authorLabel = QLabel('提交人')
        contentLabel = QLabel('申告内容')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(titleLabel, 1, 0) # row 1， column 0
        grid.addWidget(titleEdit, 1, 1) # row 1， column 1

        grid.addWidget(authorLabel, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(contentLabel, 3, 0)
        grid.addWidget(contentEdit, 3, 1, 5, 1) # 行，列，行高，列宽

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('故障申告')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())