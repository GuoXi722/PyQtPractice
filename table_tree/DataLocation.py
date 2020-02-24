import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DataLocation(QWidget):
    def __init__(self):
        super(DataLocation, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('在表格中查找指定数据')
        self.resize(600, 800)

        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()

        self.searchEdit = QLineEdit()
        searchButton = QPushButton('查找')
        searchButton.clicked.connect(self.search)
        hlayout.addWidget(self.searchEdit)
        hlayout.addWidget(searchButton)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(40)
        self.tableWidget.setColumnCount(4)

        for i in range(40):
            for j in range(4):
                itemContent = f'({i}, {j})'
                self.tableWidget.setItem(i, j, QTableWidgetItem(itemContent))

        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.tableWidget)
        self.setLayout(vlayout)

    def search(self):
        text = self.searchEdit.text()
        items = self.tableWidget.findItems(text, Qt.MatchStartsWith)
        if len(items) > 0:

            print(self.tableWidget.itemFromIndex(1))

            for item in items:
                item.setBackground(QBrush(QColor(0, 255, 0)))
                item.setForeground(QBrush(QColor(255, 0, 0)))
            row = items[0].row()
            # 定位到指定的行
            self.tableWidget.verticalScrollBar().setSliderPosition(row)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataLocation()
    window.show()
    sys.exit(app.exec_())
