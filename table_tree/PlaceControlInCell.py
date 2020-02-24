import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class PlaceControlInCell(QWidget):
    def __init__(self):
        super(PlaceControlInCell, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('在单元表格中放置控件')
        self.resize(430, 300)
        layout = QVBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])
        textItem = QTableWidgetItem('果西')
        tableWidget.setItem(0, 0, textItem)

        combo = QComboBox()
        combo.addItem('男')
        combo.addItem('女')
        # QSS
        combo.setStyleSheet('QComboBox{margin:3px}')
        tableWidget.setCellWidget(0, 1, combo)

        modifyButton = QPushButton('修改')
        modifyButton.setDown(True)
        modifyButton.setStyleSheet('QPushButton{margin:3px}')
        tableWidget.setCellWidget(0, 2, modifyButton)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlaceControlInCell()
    window.show()
    sys.exit(app.exec_())
