# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\gitcode\Python_learning\qt\ch1\signal_slog1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.select_box = QtWidgets.QCheckBox(Form)
        self.select_box.setGeometry(QtCore.QRect(110, 110, 91, 19))
        self.select_box.setObjectName("select_box")
        self.label_display = QtWidgets.QLabel(Form)
        self.label_display.setGeometry(QtCore.QRect(90, 160, 72, 15))
        self.label_display.setObjectName("label_display")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 160, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.select_box.setText(_translate("Form", "选择"))
        self.label_display.setText(_translate("Form", "显示1"))
        self.lineEdit.setInputMask(_translate("Form", "显示2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
