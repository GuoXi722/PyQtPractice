# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon


class IconForm(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.setWindowTitle('设置窗口图标')
        # self.setWindowIcon(QIcon('./images/001.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/001.ico'))
    window = IconForm()
    window.show()
    sys.exit(app.exec_())
