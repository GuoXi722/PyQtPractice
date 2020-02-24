import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ColumnSort(QWidget):
    def __init__(self):
        super(ColumnSort, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('按列排序')
        self.resize(430, 230)
        layout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)

        layout.addWidget(self.tableWidget)
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])
        newItem = QTableWidgetItem('果西')
        self.tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('120')
        self.tableWidget.setItem(0, 2, newItem)
        newItem = QTableWidgetItem('Asaf')
        self.tableWidget.setItem(1, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('130')
        self.tableWidget.setItem(1, 2, newItem)
        newItem = QTableWidgetItem('国师')
        self.tableWidget.setItem(2, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('110')
        self.tableWidget.setItem(2, 2, newItem)

        self.button = QPushButton('排序')
        self.button.clicked.connect(self.order)
        layout.addWidget(self.button)

        self.orderType = Qt.DescendingOrder
        self.setLayout(layout)

    def order(self):
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder
        self.tableWidget.sortItems(2, self.orderType)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColumnSort()
    window.show()
    sys.exit(app.exec_())
