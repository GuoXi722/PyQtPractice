"""
绘图API：绘制文本
1. 文本
2. 各种图形（直线，点，椭圆，弧，扇形，多边形等）
3. 图像

QPainter
painter = QPainter()
painter.begin()
painter.drawText(...)
painter.end()

必须在paintEvent事件方法中绘制各种元素
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DrawText(QWidget):
    def __init__(self):
        super(DrawText, self).__init__()
        self.setWindowTitle('在窗口绘制图形')
        self.resize(300, 200)
        self.text = 'Hello World'

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        painter.setPen(QColor(166, 178, 23))
        painter.setFont(QFont('SimSun', 25))

        painter.drawText(event.rect(), Qt.AlignCenter, self.text)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrawText()
    window.show()
    sys.exit(app.exec_())
