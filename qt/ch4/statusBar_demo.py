# _*_ coding: utf-8 _*_
# @Time : 2022/5/8 20:53
# @Author : Michael
# @File : statusBar_demo.py
# @desc :
from PyQt5.QtWidgets import QMainWindow, QAction, QTextEdit, QStatusBar, QApplication


class StatusBarDemo(QMainWindow):
    def __init__(self):
        super(StatusBarDemo, self).__init__()

        bar = self.menuBar()
        file = bar.addMenu('&File')
        file.addAction('&New')
        file.triggered[QAction].connect(self.processTrigger)

        self.setCentralWidget(QTextEdit())
        self.status_bar = QStatusBar()

        self.setWindowTitle("状态栏例子")
        self.setStatusBar(self.status_bar)

    def processTrigger(self, q):
        if q.text() == '&New':
            self.status_bar.showMessage(q.text() + ' was triggered', 3000)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = StatusBarDemo()
    main.show()
    sys.exit(app.exec_())