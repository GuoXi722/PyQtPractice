# -*- coding: utf-8 -*-
"""
QLineEdit综合案例
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys


class QLineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        form_layout = QFormLayout()

        edit1 = QLineEdit()
        # 设置int校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)
        edit1.setAlignment(Qt.AlignRight)

        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        edit3 = QLineEdit()
        edit3.setInputMask('99_9999_999999;#')

        edit4 = QLineEdit()
        edit4.textChanged.connect(self.text_hanged)

        edit5 = QLineEdit()
        # 设置密码回显模式
        edit5.setEchoMode(QLineEdit.Password)

        edit6 = QLineEdit('Hello World')
        edit6.setReadOnly(True)

        form_layout.addRow('整数校验', edit1)
        form_layout.addRow('浮点数校验', edit2)
        form_layout.addRow('Input Mask', edit3)
        form_layout.addRow('文本变化', edit4)
        form_layout.addRow('密码', edit5)
        form_layout.addRow('只读', edit6)

        self.setLayout(form_layout)

    def text_hanged(self, text):
        print('文本变化', text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditDemo()
    window.show()
    sys.exit(app.exec_())
