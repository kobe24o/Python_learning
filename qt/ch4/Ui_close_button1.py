import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowTitle("michael close window")
        self.resize(400, 300)
        self.closeButton = QtWidgets.QPushButton("关闭窗口按钮！！")
        self.closeButton.setGeometry(QtCore.QRect(110, 190, 91, 31))
        self.closeButton.setObjectName("closeButton")

        layout = QHBoxLayout()
        layout.addWidget(self.closeButton)
        main_frame = QtWidgets.QWidget()
        main_frame.setLayout(layout)

        self.setCentralWidget(main_frame)

        # 关闭窗口
        self.closeButton.clicked.connect(self.onClick)


    def onClick(self):
        sender = self.sender()
        print(sender.text() + "被点击了")
        # 关闭窗口按钮！！被点击了
        time.sleep(2)
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec_())
