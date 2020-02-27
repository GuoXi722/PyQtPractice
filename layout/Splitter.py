"""
拖动控件之间的边界（QSplitter）
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Splitter(QWidget):
    def __init__(self):
        super(Splitter, self).__init__()
        self.setWindowTitle('拖动控件之间的边界（QSplitter）')
        self.setGeometry(300, 300, 300, 200)
        hlayout = QHBoxLayout()

        textEdit = QTextEdit()
        topLeft = QFrame()
        topLeft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topLeft)
        splitter1.addWidget(textEdit)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hlayout.addWidget(splitter2)
        self.setLayout(hlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Splitter()
    window.show()
    sys.exit(app.exec_())
