# _*_ coding: utf-8 _*_
# @Time : 2022/5/4 21:58
# @Author : Michael
# @File : check_box1.py
# @desc :
from PyQt5.QtWidgets import QWidget, QGroupBox, QHBoxLayout, QCheckBox, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt


class checkBox(QWidget):
    def __init__(self):
        super().__init__()

        groupbox = QGroupBox("CheckBoxes")
        groupbox.setFlat(False)

        layout = QHBoxLayout()

        self.checkbox1 = QCheckBox("&CheckBox1")
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(lambda: self.checkbox_state(self.checkbox1))
        layout.addWidget(self.checkbox1)

        self.checkbox2 = QCheckBox("CheckBox2")
        self.checkbox2.toggled.connect(lambda: self.checkbox_state(self.checkbox2))
        layout.addWidget(self.checkbox2)

        self.checkbox3 = QCheckBox("CheckBox3")
        self.checkbox3.setTristate(True)
        self.checkbox3.setCheckState(Qt.PartiallyChecked)
        self.checkbox3.stateChanged.connect(lambda: self.checkbox_state(self.checkbox3))
        layout.addWidget(self.checkbox3)

        groupbox.setLayout(layout)
        main_layout = QVBoxLayout()
        main_layout.addWidget(groupbox)

        self.setLayout(main_layout)
        self.setWindowTitle("CheckBoxes例子")

    def checkbox_state(self, checkbox):
        checkbox1_state = self.checkbox1.text() + ', isChecked=' + str(
            self.checkbox1.isChecked()) + ', checkState=' + str(self.checkbox1.checkState()) + '\n'
        checkbox2_state = self.checkbox2.text() + ', isChecked=' + str(
            self.checkbox2.isChecked()) + ', checkState=' + str(self.checkbox2.checkState()) + '\n'
        checkbox3_state = self.checkbox3.text() + ', isChecked=' + str(
            self.checkbox3.isChecked()) + ', checkState=' + str(self.checkbox3.checkState()) + '\n'
        print(checkbox1_state, checkbox2_state, checkbox3_state)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = checkBox()
    main.show()
    sys.exit(app.exec_())