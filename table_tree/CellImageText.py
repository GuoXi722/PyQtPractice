import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CellImageText(QWidget):
    def __init__(self):
        super(CellImageText, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('显示图片文本')
        self.resize(400, 300)

        layout = QVBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(3)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '显示图片'])
        newItem = QTableWidgetItem('果西')
        tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('男')
        tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem(QIcon('./images/bao1.png'), '背包')
        tableWidget.setItem(0, 2, newItem)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CellImageText()
    window.show()
    sys.exit(app.exec_())
