# _*_ coding: utf-8 _*_
# @Time : 2022/5/8 19:40
# @Author : Michael
# @File : calendar_demo.py
# @desc :
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QCalendarWidget, QLabel, QApplication


class CalendarDemo(QWidget):
    def __init__(self):
        super(CalendarDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.move(20, 50)
        self.cal.setMinimumDate(QDate(2000, 1, 1))
        self.cal.setMaximumDate(QDate(2100, 12, 31))
        self.cal.clicked[QDate].connect(self.showDate)
        self.label1 = QLabel(self)
        date = self.cal.selectedDate()
        self.label1.setText(date.toString('yyyy-MM-dd dddd'))
        self.label1.move(20, 10)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Calendar')

    def showDate(self, date):
        self.label1.setText(date.toString('yyyy-MM-dd dddd'))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = CalendarDemo()
    w.show()
    sys.exit(app.exec_())