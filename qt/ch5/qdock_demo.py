# _*_ coding: utf-8 _*_
# @Time : 2022/5/29 21:40
# @Author : Michael
# @File : qdock_demo.py
# @desc :
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QDockWidget, QListWidget, QApplication, QTextEdit


class qock_demo(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('New')
        file.addAction('Open')
        file.addAction('Save')
        self.setCentralWidget(QTextEdit())

        self.items = QDockWidget('Dockable', self)
        self.listWidget = QListWidget()
        self.listWidget.addItems(['Item 1', 'Item 2', 'Item 3'])
        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        self.setLayout(layout)
        self.setWindowTitle('Dock例子')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = qock_demo()
    main.show()
    sys.exit(app.exec_())