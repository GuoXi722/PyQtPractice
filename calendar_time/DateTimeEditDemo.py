import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DateTimeEditDemo(QWidget):
    def __init__(self):
        super(DateTimeEditDemo, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('设置不同风格的日期和时间')
        self.resize(300, 90)
        vlayout = QVBoxLayout()
        dateTimeEdit1 = QDateTimeEdit()
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))
        dateTimeEdit1.dateChanged.connect(self.onDateChanged)
        dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)
        self.dateTimeEdit = dateTimeEdit1

        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
        dateTimeEdit2.setCalendarPopup(True)
        dateEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())

        dateTimeEdit1.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        dateTimeEdit2.setDisplayFormat('yyyy/MM/dd HH-mm-ss')
        dateEdit.setDisplayFormat('yyyy.MM.dd')
        timeEdit.setDisplayFormat('HH:mm:ss')

        vlayout.addWidget(dateTimeEdit1)
        vlayout.addWidget(dateTimeEdit2)
        vlayout.addWidget(dateEdit)
        vlayout.addWidget(timeEdit)

        self.button = QPushButton('获取日期和时间')
        self.button.clicked.connect(self.onButtonClick)
        vlayout.addWidget(self.button)

        self.setLayout(vlayout)

    def onDateChanged(self, date):
        print(date)

    def onTimeChanged(self, time):
        print(time)

    def onDateTimeChanged(self, datetime):
        print(datetime)

    def onButtonClick(self):
        datetime = self.dateTimeEdit.dateTime()
        print(datetime)

        print(self.dateTimeEdit.maximumDate())
        print(self.dateTimeEdit.maximumDateTime())
        print(self.dateTimeEdit.minimumDateTime())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DateTimeEditDemo()
    window.show()
    sys.exit(app.exec_())
