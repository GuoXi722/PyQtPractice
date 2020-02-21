# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class CenterForm(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.setWindowTitle('让窗口居中')
        self.center()

    # 控制窗口显示在屏幕中心的方法
    def center(self):
        size = self.geometry()
        screen = QDesktopWidget().screenGeometry()
        new_left = (screen.width() - size.width()) / 2
        new_top = (screen.height() - size.height()) / 2
        self.move(new_left, new_top)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CenterForm()
    window.show()
    sys.exit(app.exec_())
