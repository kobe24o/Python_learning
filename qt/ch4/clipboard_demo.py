# _*_ coding: utf-8 _*_
# @Time : 2022/5/7 9:38
# @Author : Michael
# @File : clipboard_demo.py
# @desc :
import sys

from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QGridLayout, QApplication


class myForm(QDialog):
    def __init__(self):
        super().__init__()

        textCopyButton = QPushButton("&Copy Text")
        textPasteButton = QPushButton("Paste &Text")
        htmlCopyButton = QPushButton("C&opy HTML")
        htmlPasteButton = QPushButton("Paste &HTML")
        imageCopyButton = QPushButton("Co&py Image")
        imagePasteButton = QPushButton("Paste &Image")

        self.textlabel = QLabel('原始文字')
        self.imagelabel = QLabel()
        self.imagelabel.setPixmap(QPixmap('../store.png'))

        layout = QGridLayout()
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(textPasteButton, 0, 1)
        layout.addWidget(htmlCopyButton, 1, 0)
        layout.addWidget(htmlPasteButton, 1, 1)
        layout.addWidget(imageCopyButton, 2, 0)
        layout.addWidget(imagePasteButton, 2, 1)
        layout.addWidget(self.textlabel, 3, 0, 1, 2)
        layout.addWidget(self.imagelabel, 4, 0, 1, 2)
        self.setLayout(layout)

        self.setWindowTitle("Clipboard Demo")
        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText("Hello PyQt5")

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textlabel.setText(clipboard.text())

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml("<b><font color=red>你好，michael</font></b>")
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textlabel.setText(mimeData.html())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('logo.png'))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imagelabel.setPixmap(clipboard.pixmap())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())