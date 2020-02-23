import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('日历演示')
        self.resize(400, 350)

        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate(1998, 1, 1))
        self.calendar.setMaximumDate(QDate(2098, 1, 1))
        self.calendar.setGridVisible(True)
        self.calendar.move(20, 20)
        self.calendar.clicked.connect(self.showDate)

        self.label = QLabel(self)
        date = self.calendar.selectedDate()
        self.label.setText(date.toString('yyyy-MM-dd-dddd'))
        self.label.move(20, 300)

    def showDate(self, date):
        self.label.setText((date.toString('yyyy-MM-dd-dddd')))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyCalendar()
    window.show()
    sys.exit(app.exec_())
