# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_signal_slog1 import Ui_Form


class Form(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(Form, self).__init__(parent)
        self.setupUi(self)
        self.select_box.setChecked(True) # 设置默认是选中状态
    
    @pyqtSlot(bool)
    def on_select_box_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        self.label_display.setVisible(checked)
        self.lineEdit.setEnabled(checked)
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
