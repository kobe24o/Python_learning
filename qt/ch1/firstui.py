# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doublespinboxlUZDGJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QSizePolicy, QAction, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QDoubleSpinBox, QFrame, \
    QMenuBar, QPushButton, QSpacerItem, QGridLayout, QStatusBar, QApplication
from PyQt5.QtGui import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(598, 492)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actiondiv = QAction(MainWindow)
        self.actiondiv.setObjectName(u"actiondiv")
        self.actiondiv.setCheckable(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 110, 401, 191))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.doubleSpinBox = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout.addWidget(self.doubleSpinBox, 1, 0, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.gridLayout.addWidget(self.doubleSpinBox_3, 3, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")

        self.gridLayout.addWidget(self.doubleSpinBox_4, 1, 1, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.gridLayout.addWidget(self.doubleSpinBox_2, 2, 0, 1, 1)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")

        self.gridLayout.addWidget(self.doubleSpinBox_6, 3, 1, 1, 1)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")

        self.gridLayout.addWidget(self.doubleSpinBox_5, 2, 1, 1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.horizontalSpacer = QSpacerItem(1000, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 598, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.doubleSpinBox, self.doubleSpinBox_4)
        QWidget.setTabOrder(self.doubleSpinBox_4, self.doubleSpinBox_2)
        QWidget.setTabOrder(self.doubleSpinBox_2, self.doubleSpinBox_5)
        QWidget.setTabOrder(self.doubleSpinBox_5, self.doubleSpinBox_3)
        QWidget.setTabOrder(self.doubleSpinBox_3, self.doubleSpinBox_6)
        QWidget.setTabOrder(self.doubleSpinBox_6, self.pushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actiondiv.setText(QCoreApplication.translate("MainWindow", u"div", None))
        # if QT_CONFIG(tooltip)
        self.actiondiv.setToolTip(QCoreApplication.translate("MainWindow",
                                                             u"<html><head/><body><p>\u65b9\u5dee\u5feb\u6377\u952e</p></body></html>",
                                                             None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.actiondiv.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+Q", None))
        # endif // QT_CONFIG(shortcut)
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u503c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u503c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u5dee", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f812", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f811", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u76d1\u6d4b", None))
    # retranslateUi


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.setupUi()
    sys.exit(app.exec_())
