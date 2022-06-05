# _*_ coding: utf-8 _*_
# @Time : 2022/5/29 23:20
# @Author : Michael
# @File : qmultiDocInterface.py
# @desc :

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class qmultiDocInterface(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(qmultiDocInterface, self).__init__(parent)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.triggered[QAction].connect(self.windowaction)
        self.setWindowTitle("MDI demo")

    def windowaction(self, q):
        print("triggered")

        if q.text() == "New":
            qmultiDocInterface.count = qmultiDocInterface.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("子窗口" + str(qmultiDocInterface.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        if q.text() == "cascade":
            self.mdi.cascadeSubWindows() # 层叠
        if q.text() == "Tiled":
            self.mdi.tileSubWindows() # 平铺


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = qmultiDocInterface()
    demo.show()
    sys.exit(app.exec_())