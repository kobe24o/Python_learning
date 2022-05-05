# _*_ coding: utf-8 _*_
# @Time : 2022/5/5 9:30
# @Author : Michael
# @File : qmessagebox1.py
# @desc :
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QApplication


class QMessageBox1(QWidget):
    def __init__(self):
        super(QMessageBox1, self).__init__()

        self.setWindowTitle("QMessageBox1例子")
        self.resize(300, 200)

        self.button1 = QPushButton('点击弹出消息', self)
        self.button1.move(50, 50)
        self.button1.clicked.connect(self.msg)
    def msg(self):
        reply = QMessageBox.warning(self, 'Message标题', '你好，世界！', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print('点击了Yes')
        else:
            print('点击了No')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = QMessageBox1()
    main.show()
    sys.exit(app.exec_())