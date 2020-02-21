# -*- coding: utf-8 -*-
"""
QLineEdit控件与回显模式
基本功能：输入单行的文本
EchoMode（回显模式）
4种回显模式：
1. Normal
2. NoEcho
3. Password
4. PasswordEchoOnEdit
"""

import sys
from PyQt5.QtWidgets import *


class QLineEditEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('文本输入框的回显模式')

        form_layout = QFormLayout()

        no_rmal_line_edit = QLineEdit()
        no_echo_line_edit = QLineEdit()
        password_line_edit = QLineEdit()
        password_echo_on_edit_line_edit = QLineEdit()

        form_layout.addRow('Normal', no_rmal_line_edit)
        form_layout.addRow('NoEcho', no_echo_line_edit)
        form_layout.addRow('Password', password_line_edit)
        form_layout.addRow('PasswordEchoOnEdit', password_echo_on_edit_line_edit)

        no_rmal_line_edit.setPlaceholderText('Normal')
        no_echo_line_edit.setPlaceholderText('NoEcho')
        password_line_edit.setPlaceholderText('Password')
        password_echo_on_edit_line_edit.setPlaceholderText('PasswordEchoOnEdit')

        no_rmal_line_edit.setEchoMode(QLineEdit.Normal)
        no_echo_line_edit.setEchoMode(QLineEdit.NoEcho)
        password_line_edit.setEchoMode(QLineEdit.Password)
        password_echo_on_edit_line_edit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(form_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())

