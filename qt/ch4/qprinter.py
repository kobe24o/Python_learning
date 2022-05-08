# _*_ coding: utf-8 _*_
# @Time : 2022/5/8 21:14
# @Author : Michael
# @File : qprinter.py
# @desc :
from PyQt5.QtGui import QImage, QPixmap, QIcon, QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import QMainWindow, QLabel, QSizePolicy, QAction, QApplication
from PyQt5.QtCore import Qt, QPoint


class printer_demo(QMainWindow):
    def __init__(self):
        super(printer_demo, self).__init__()
        self.setWindowTitle(self.tr("打印测试"))  # tr 函数用于以后翻译为其他语言
        self.imageLabel = QLabel()
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setCentralWidget(self.imageLabel)

        self.image = QImage()
        self.createActions()
        self.createMenus()
        self.createToolBars()

        if self.image.load('logo.png'):
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
            self.resize(self.image.width(), self.image.height())
    def createActions(self):
        self.printAct = QAction(QIcon('../store.png'), self.tr("打印哦"), self)
        self.printAct.setShortcut('Ctrl+P')
        self.printAct.setStatusTip(self.tr("打印图像"))
        self.printAct.triggered.connect(self.printImage)

    def createMenus(self):
        printmenu = self.menuBar().addMenu(self.tr("打印菜单"))
        printmenu.addAction(self.printAct) #

    def createToolBars(self):
        printToolBar = self.addToolBar(self.tr("打印！"))
        printToolBar.addAction(self.printAct)

    def printImage(self):
        printer = QPrinter()
        printDialog = QPrintDialog(printer, self)
        if printDialog.exec_():
            print('打印中...')
            painter = QPainter(printer)
            rect = painter.viewport()
            print(rect)
            size = self.image.size()
            print(size)
            size.scale(rect.size(), Qt.KeepAspectRatio)
            print('after scale: ', size)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            print(self.image.rect())
            painter.drawImage(QPoint(0, 0), self.image)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = printer_demo()
    window.show()
    sys.exit(app.exec_())
