# -*- coding: utf-8 -*-
"""
QAbstractButton
QPushButton
AToolButton
QRadioButton
QCheckButton
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
import sys


class QPushButtonDemo(QWidget):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QPushButton Demo')

        layout = QVBoxLayout()

        self.button1 = QPushButton('第1个按钮')
        self.button1.setText('First Button')
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(lambda: self.which_button(self.button1))
        self.button1.clicked.connect(self.button_state)

        self.button2 = QPushButton('图片按钮')
        self.button2.setIcon(QIcon(QPixmap('./images/python.jpg')))
        self.button2.clicked.connect(lambda: self.which_button(self.button2))

        self.button3 = QPushButton('不可用的按钮')
        self.button3.setEnabled(False)

        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda: self.which_button(self.button4))

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)
        self.resize(400, 300)

    def which_button(self, btn):
        print(f'被点击的按钮时{btn.text()}')

    def button_state(self):
        if self.button1.isChecked():
            print('button1已被选中')
        else:
            print('button1未被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QPushButtonDemo()
    window.show()
    sys.exit(app.exec_())

