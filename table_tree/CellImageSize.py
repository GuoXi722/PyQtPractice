"""
改变表格中图片尺寸
setIconSize(QSize(width, height))
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CellImageSize(QWidget):
    def __init__(self):
        super(CellImageSize, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('改变表格中图片尺寸')
        self.resize(1000, 900)

        layout = QVBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setIconSize(QSize(300, 200))
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(3)

        tableWidget.setHorizontalHeaderLabels(['图片1', '图片2', '图片3'])
        # 让列的宽度和图片的宽度相同
        for i in range(3):
            tableWidget.setColumnWidth(i, 300)
        # 让行的高度和图片的高度相同
        for i in range(5):
            tableWidget.setRowHeight(i, 200)
        for k in range(15):
            i = k / 3  # 行
            j = k % 3  # 列
            item = QTableWidgetItem()
            item.setIcon(QIcon(f'./images/bao{k}.png'))
            tableWidget.setItem(i, j, item)

        layout.addWidget(tableWidget)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CellImageSize()
    window.show()
    sys.exit(app.exec_())
