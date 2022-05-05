# _*_ coding: utf-8 _*_
# @Time : 2022/5/5 8:57
# @Author : Michael
# @File : qdialog1.py
# @desc :
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDialog, QApplication
from PyQt5.QtCore import Qt

class qdialog_demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog例子")
        self.resize(300, 200)

        self.button = QPushButton("弹出对话框", self)
        self.button.move(50, 50)
        self.button.clicked.connect(self.showdialog)

    def showdialog(self):
        dialog = QDialog()
        btn = QPushButton("ok", dialog)
        btn.move(50, 50)
        dialog.setWindowTitle("提交文件")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = qdialog_demo()
    main.show()
    sys.exit(app.exec_())