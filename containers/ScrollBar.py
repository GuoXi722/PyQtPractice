"""
滚动条控件：QScrollBar
滚动条的作用
1.通过滚动条值的变化控制其他控件状态的变化
2.通过滚动条值的变化控制控件位置的变化
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ScrollBar(QWidget):
    def __init__(self):
        super(ScrollBar, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('')
        layout = QHBoxLayout()
        self.label = QLabel('拖动滚动条改变颜色位置')
        layout.addWidget(self.label)

        self.scrollbar1 = QScrollBar()
        self.scrollbar1.setMaximum(255)
        self.scrollbar1.sliderMoved.connect(self.sliderMoved)

        self.scrollbar2 = QScrollBar()
        self.scrollbar2.setMaximum(255)
        self.scrollbar2.sliderMoved.connect(self.sliderMoved)

        self.scrollbar3 = QScrollBar()
        self.scrollbar3.setMaximum(255)
        self.scrollbar3.sliderMoved.connect(self.sliderMoved)

        self.scrollbar4 = QScrollBar()
        self.scrollbar4.setMaximum(255)
        self.scrollbar4.sliderMoved.connect(self.sliderMoved1)

        layout.addWidget(self.scrollbar1)
        layout.addWidget(self.scrollbar2)
        layout.addWidget(self.scrollbar3)
        layout.addWidget(self.scrollbar4)

        self.setGeometry(300, 300, 300, 200)
        self.setLayout(layout)

        self.y = self.label.pos().y()

    def sliderMoved(self):
        print(self.scrollbar1.value(), self.scrollbar2.value(), self.scrollbar3.value())
        palette = QPalette()
        c = QColor(self.scrollbar1.value(), self.scrollbar2.value(), self.scrollbar3.value(), 255)
        palette.setColor(QPalette.Foreground, c)
        self.label.setPalette(palette)

    def sliderMoved1(self):
        self.label.move(self.label.x(), self.y + self.scrollbar4.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScrollBar()
    window.show()
    sys.exit(app.exec_())
