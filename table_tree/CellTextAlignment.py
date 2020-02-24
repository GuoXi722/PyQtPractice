import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CellTextAlignment(QWidget):
    def __init__(self):
        super(CellTextAlignment, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('')
        self.resize(430, 230)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(4)

        layout.addWidget(tableWidget)
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])
        newItem = QTableWidgetItem('果西')
        tableWidget.setItem(0, 0, newItem)
        tableWidget.setSpan(0, 0, 3, 1)
        newItem = QTableWidgetItem('男')
        tableWidget.setItem(0, 1, newItem)
        tableWidget.setSpan(0, 1, 2, 1)
        newItem = QTableWidgetItem('160')
        tableWidget.setItem(0, 2, newItem)
        tableWidget.setSpan(0, 2, 4, 2)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CellTextAlignment()
    window.show()
    sys.exit(app.exec_())
