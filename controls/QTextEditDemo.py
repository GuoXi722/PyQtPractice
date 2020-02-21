# -*- coding: utf-8 -*-
"""
QTextEdit控件
"""

from PyQt5.QtWidgets import *
import sys


class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QTextEdit控件显示')

        self.resize(300, 280)

        self.text_edit = QTextEdit()
        self.button_text = QPushButton('显示文本')
        self.button_html = QPushButton('显示html')
        self.button_to_text = QPushButton('获取文本')
        self.button_to_html = QPushButton('获取html')

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button_text)
        layout.addWidget(self.button_html)
        layout.addWidget(self.button_to_text)
        layout.addWidget(self.button_to_html)

        self.setLayout(layout)

        self.button_text.clicked.connect(self.on_click_button_text)
        self.button_html.clicked.connect(self.on_click_button_html)
        self.button_to_text.clicked.connect(self.on_click_button_to_text)
        self.button_to_html.clicked.connect(self.on_click_button_to_html)

    def on_click_button_text(self):
        self.text_edit.setPlainText('Hello World, 世界你好吗？')

    def on_click_button_to_text(self):
        print(self.text_edit.toPlainText())

    def on_click_button_html(self):
        self.text_edit.setHtml('<h1>Hello World, 世界你好吗？</h1>')

    def on_click_button_to_html(self):
        print(self.text_edit.toHtml())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTextEditDemo()
    window.show()
    sys.exit(app.exec_())
