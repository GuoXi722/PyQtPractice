# -*- coding: utf-8 -*-
"""
QLabel控件
setAlignment(): 设置文本对齐方式
setIndent(): 设置文本缩进
text(): 获取文本内容
setBuddy(): 设置伙伴关系
setText(): 设置文本内容
selectedText(): 返回所选择的字符串
setWordWrap(): 设置是否允许换行

QLabel常用的信号（事件）
1.当鼠标滑过QLabel控件时触发: linkHovered
2.当鼠标点击QLabel空间是触发: linkActivate
"""

import sys
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QLabel
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color="yellow">这是一个文本标签</font>')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText('<a href="#">欢迎使用Python GUI程序</a>')

        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap('./images/python.jpg'))

        label4.setOpenExternalLinks(True)
        label4.setText('<a href="https://www.python.org/">Python官网</a>')
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接')

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.link_hovered)
        label4.linkActivated.connect(self.link_activated)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')

    def link_hovered(self):
        print('当鼠标滑过label2时触发事件')

    def link_activated(self):
        print('当鼠标点击label4时触发事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLabelDemo()
    window.show()
    sys.exit(app.exec_())

