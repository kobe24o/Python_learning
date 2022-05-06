# _*_ coding: utf-8 _*_
# @Time : 2022/5/5 22:18
# @Author : Michael
# @File : qfont_dialog1.py
# @desc :
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFontDialog, QApplication


class fontDialog(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.fontButton = QPushButton('选择字体')
        self.fontButton.clicked.connect(self.chooseFont)
        layout.addWidget(self.fontButton)

        self.line1 = QLabel('hello michael, 你好啊')
        layout.addWidget(self.line1)

        self.setLayout(layout)
        self.setWindowTitle('字体对话框')
    def chooseFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.line1.setFont(font)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = fontDialog()
    ui.show()
    sys.exit(app.exec_())