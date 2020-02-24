"""
扩展的列表控件：QListWidget
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ListWidget(QMainWindow):
    def __init__(self):
        super(ListWidget, self).__init__()
        self.setWindowTitle('QListWidget 演示')
        self.resize(300, 270)
        self.listwidget = QListWidget()
        self.listwidget.addItem('item1')
        self.listwidget.addItem('item2')
        self.listwidget.addItem('item3')
        self.listwidget.addItem('item4')
        self.listwidget.itemClicked.connect(self.clicked)
        self.setCentralWidget(self.listwidget)

    def clicked(self, index):
        QMessageBox.information(self, 'QListWidget', f'您选择了：{self.listwidget.item(self.listwidget.row(index)).text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ListWidget()
    window.show()
    sys.exit(app.exec_())
