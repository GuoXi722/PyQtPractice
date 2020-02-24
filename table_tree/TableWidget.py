"""
扩展的表格控件：QTableWidget
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class TableWidget(QWidget):
    def __init__(self):
        super(TableWidget, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('QTableWidget 演示')
        self.resize(430, 230)
        layout = QHBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['ID', '姓名', '年龄'])
        idItem = QTableWidgetItem('1')
        tableWidget.setItem(0, 0, idItem)
        nameItem = QTableWidgetItem('果西')
        tableWidget.setItem(0, 1, nameItem)
        ageItem = QTableWidgetItem('18')
        tableWidget.setItem(0, 2, ageItem)

        # 禁止编辑
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 整行选择
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 按内容调整列和行
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()
        # 隐藏列头和行头
        tableWidget.horizontalHeader().setVisible(False)
        # tablewidget.verticalHeader().setVisible(False)
        tableWidget.setVerticalHeaderLabels(['a', 'b', 'c'])
        # 隐藏表格线
        tableWidget.setShowGrid(False)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableWidget()
    window.show()
    sys.exit(app.exec_())
