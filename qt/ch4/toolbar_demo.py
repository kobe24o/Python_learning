# _*_ coding: utf-8 _*_
# @Time : 2022/5/8 20:36
# @Author : Michael
# @File : toolbar_demo.py
# @desc :
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QAction, QApplication


class ToolBarDemo(QMainWindow):
    def __init__(self):
        super(ToolBarDemo, self).__init__()
        self.setWindowTitle('ToolBar')
        self.resize(300, 200)

        layout = QVBoxLayout()
        toolbar = self.addToolBar('文件')
        new = QAction(QIcon('../store.png'), '新建', self)
        toolbar.addAction(new)
        toolbar.actionTriggered[QAction].connect(self.toolbuttonPressed)
        open = QAction(QIcon('logo.png'), '打开', self)
        toolbar.addAction(open)

        self.setLayout(layout)

    def toolbuttonPressed(self, q):
        print("按下了：", q.text())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = ToolBarDemo()
    main.show()
    sys.exit(app.exec_())