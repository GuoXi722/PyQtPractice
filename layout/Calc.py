"""
栅格布局实现计算器的ui
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Calc(QWidget):
    def __init__(self):
        super(Calc, self).__init__()
        self.setWindowTitle('栅格布局')

        layout = QGridLayout()
        self.setLayout(layout)

        names = ['Cls', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for name, position in zip(names, positions):
            if name == '':
                continue
            button = QPushButton(name)
            layout.addWidget(button, *position)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calc()
    window.show()
    sys.exit(app.exec_())
