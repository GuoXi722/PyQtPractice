import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class FillRect(QWidget):
    def __init__(self):
        super(FillRect, self).__init__()
        self.setWindowTitle('用画刷填充区域')
        self.resize(600, 600)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 15, 90, 60)

        brush = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 15, 90, 60)

        brush = QBrush(Qt.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 15, 90, 60)

        brush = QBrush(Qt.Dense3Pattern)
        painter.setBrush(brush)
        painter.drawRect(10, 105, 90, 60)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FillRect()
    window.show()
    sys.exit(app.exec_())
