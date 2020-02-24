import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CellFontAndColor(QWidget):
    def __init__(self):
        super(CellFontAndColor, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('在表格中设置字体和眼色')
        self.resize(430, 230)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        layout.addWidget(tableWidget)
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])
        nameItem = QTableWidgetItem('果西')
        nameItem.setFont(QFont('Times', 14, Qt.black))
        tableWidget.setItem(0, 0, nameItem)

        sexItem = QTableWidgetItem('男')
        sexItem.setForeground(QBrush(QColor(255, 255, 0)))
        sexItem.setBackground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 1, sexItem)

        tzItem = QTableWidgetItem('120')
        tzItem.setFont(QFont('Times', 20, Qt.black))
        tzItem.setForeground(QBrush(QColor(255, 0, 0)))
        tableWidget.setItem(0, 2, tzItem)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CellFontAndColor()
    window.show()
    sys.exit(app.exec_())
