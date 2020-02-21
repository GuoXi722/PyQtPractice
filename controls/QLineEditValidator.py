# -*- coding: utf-8 -*-
"""
QLinkEdit控件的输入（校验器）
如只能限制输入整数、浮点数、或满足一定条件的字符串
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class QLineEditValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('校验器')

        # 创建表单布局
        form_layout = QFormLayout()

        int_line_edit = QLineEdit()
        double_line_edit = QLineEdit()
        validator_line_edit = QLineEdit()

        form_layout.addRow('整数类型', int_line_edit)
        form_layout.addRow('浮点类型', double_line_edit)
        form_layout.addRow('数字和字母类型', validator_line_edit)

        int_line_edit.setPlaceholderText('整型')
        double_line_edit.setPlaceholderText('浮点型')
        validator_line_edit.setPlaceholderText('数字和字母')

        # 整数校验器 [1,2]
        int_validator = QIntValidator(self)
        int_validator.setRange(1, 99)

        # 浮点型校验器 [-360,360]，精度：小数点后2位
        double_validator = QDoubleValidator(self)
        double_validator.setRange(-360, 360)
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度，小数点2位
        double_validator.setDecimals(2)

        # 字符和数字
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置校验器
        int_line_edit.setValidator(int_validator)
        double_line_edit.setValidator(double_validator)
        validator_line_edit.setValidator(validator)

        self.setLayout(form_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())
