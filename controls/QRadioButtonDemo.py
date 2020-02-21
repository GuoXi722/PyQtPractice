# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
import sys


class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        self.button1 = QRadioButton('单选按钮1')
        self.button1.setChecked(True)
        self.button1.toggled.connect(self.button_state)

        self.button2 = QRadioButton('单选按钮2')
        self.button2.toggled.connect(self.button_state)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def button_state(self):
        radio_button = self.sender()

        if radio_button.isChecked() is True:
            print(f'<{radio_button.text()}>被选中')
        else:
            print(f'<{radio_button.text()}>未被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QRadioButtonDemo()
    window.show()
    sys.exit(app.exec_())
