import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DateDialog(QDialog):
    def __init__(self):
        super(DateDialog, self).__init__()
        self.setWindowTitle('DateDialog')

        layout = QVBoxLayout(self)
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.datetime)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

    def dateTime(self):
        return self.datetime.dateTime()

    @staticmethod
    def getDateTime():
        dialog = DateDialog()
        result = dialog.exec()
        date = dialog.dateTime()
        return (date.date(), date.time(), result == QDialog.Accepted)


class MultiWindow1(QWidget):
    def __init__(self):
        super(MultiWindow1, self).__init__()
        self.setWindowTitle("多窗口交互（1）：不使用信号与槽")

        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.onButton1Click)

        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.onButton2Click)

        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def onButton1Click(self):
        dialog = DateDialog()
        result = dialog.exec()
        date = dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        dialog.destroy()

    def onButton2Click(self):
        date, time, result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        if result == QDialog.Accepted:
            print('点击确定按钮')
        else:
            print('单击取消按钮')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MultiWindow1()
    window.show()
    sys.exit(app.exec_())
