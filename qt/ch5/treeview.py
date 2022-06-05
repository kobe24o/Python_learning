# _*_ coding: utf-8 _*_
# @Time : 2022/5/29 20:49
# @Author : Michael
# @File : treeview.py
# @desc :
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Window系统提供的模式
    model = QDirModel()
    # 创建一个QtreeView部件
    tree = QTreeView()
    # 为部件添加模式
    tree.setModel(model)
    tree.setWindowTitle("QTreeView 例子")
    tree.resize(640, 480)
    tree.show()
    sys.exit(app.exec_())