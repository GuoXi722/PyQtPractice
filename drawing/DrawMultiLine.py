"""
绘制不同类型直线
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle('绘制不同直线')

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        pen = QPen(Qt.red, 3, Qt.SolidLine)

        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 10, 5, 8])
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrawMultiLine()
    window.show()
    sys.exit(app.exec_())
