"""
让控件支持拖拽
A.setDragEnable(True)

B.setAcceptDrops(True)

B需要两个事件
1. dragEnterEvent   将A拖到B触发
2. dropEvent        在B的区域放下A时触发
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyComboBox(QComboBox):
    def __init__(self):
        super(MyComboBox, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())


class DragDropDemo(QWidget):
    def __init__(self):
        super(DragDropDemo, self).__init__()
        self.setWindowTitle('拖拽案例')
        layout = QFormLayout()
        layout.addRow(QLabel('请将左边的文本拖拽到右边的下拉列表中'))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)

        combo = MyComboBox()
        layout.addRow(lineEdit, combo)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DragDropDemo()
    window.show()
    sys.exit(app.exec_())
