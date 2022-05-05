# _*_ coding: utf-8 _*_
# @Time : 2022/5/5 9:49
# @Author : Michael
# @File : input_dialog1.py
# @desc :
from PyQt5.QtWidgets import QWidget, QFormLayout, QPushButton, QLineEdit, QInputDialog, QApplication


class input_dialog1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()

        self.btn1 = QPushButton('获取列表里的选项')
        self.btn1.clicked.connect(self.get_list_item)

        self.lineEdit1 = QLineEdit()
        layout.addRow(self.btn1, self.lineEdit1)

        self.btn2 = QPushButton('获取字符串')
        self.btn2.clicked.connect(self.get_str)
        self.lineEdit2 = QLineEdit()
        layout.addRow(self.btn2, self.lineEdit2)

        self.btn3 = QPushButton('获取整数')
        self.btn3.clicked.connect(self.get_int)
        self.lineEdit3 = QLineEdit()
        layout.addRow(self.btn3, self.lineEdit3)

        self.setLayout(layout)
        self.setWindowTitle('获取输入')
    def get_list_item(self):
        items = ('C', 'C++', 'Java', 'Python')
        item, ok = QInputDialog.getItem(self, '请选择语言', '语言列表', items, 0, False)
        if ok and item:
            self.lineEdit1.setText(item)
    def get_str(self):
        text, ok = QInputDialog.getText(self, '输入字符串对话框', '请输入字符串')
        if ok:
            self.lineEdit2.setText(text)
    def get_int(self):
        num, ok = QInputDialog.getInt(self, '输入整数对话框', '请输入整数')
        if ok:
            self.lineEdit3.setText(str(num))
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = input_dialog1()
    win.show()
    sys.exit(app.exec_())