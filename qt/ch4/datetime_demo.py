# _*_ coding: utf-8 _*_
# @Time : 2022/5/8 19:58
# @Author : Michael
# @File : datetime_demo.py
# @desc :
from PyQt5.QtCore import QDateTime, QDate
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDateTimeEdit, QPushButton, QApplication


class DateTimeDemo(QWidget):
    def __init__(self):
        super(DateTimeDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("DateTimeDemo")
        self.resize(300, 200)

        layout = QVBoxLayout()
        self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime())
        self.dateEdit.setCalendarPopup(True)  # 弹出日历
        self.dateEdit.setDisplayFormat("yyyy-MM-dd hh:mm:ss")  # 设置显示格式
        self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365))  # 设置最小日期
        self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365))  # 设置最大日期

        self.dateEdit.dateChanged.connect(self.ondateChanged)
        self.dateEdit.timeChanged.connect(self.ontimeChanged)
        self.dateEdit.dateTimeChanged.connect(self.ondateTimeChanged)

        self.btn = QPushButton("获取当前日期时间")
        self.btn.clicked.connect(self.onbtnClicked)

        layout.addWidget(self.dateEdit)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def ondateChanged(self, date):
        print(date)
        print("date changed:", date.toString("yyyy-MM-dd"))

    def ontimeChanged(self, time):
        print(time)
        print("time changed:", time.toString("hh:mm:ss"))

    def ondateTimeChanged(self, dateTime):
        print(dateTime)
        print("dateTime changed:", dateTime.toString("yyyy-MM-dd hh:mm:ss"))

    def onbtnClicked(self):
        dateTime = self.dateEdit.dateTime()
        maxdate = self.dateEdit.maximumDate()
        mindate = self.dateEdit.minimumDate()
        maxtime = self.dateEdit.maximumTime()
        mintime = self.dateEdit.minimumTime()
        maxdatetime = self.dateEdit.maximumDateTime()
        mindatetime = self.dateEdit.minimumDateTime()
        print(dateTime)
        print(maxdate)
        print(mindate)
        print(maxtime)
        print(mintime)
        print(maxdatetime)
        print(mindatetime)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = DateTimeDemo()
    main.show()
    sys.exit(app.exec_())
