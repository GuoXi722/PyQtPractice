# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QWidget, QPushButton


class ScreenGeometry(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        button = QPushButton('按钮', self)
        button.clicked.connect(self.on_click_button)

        button.move(24, 52)

        self.resize(300, 240)
        self.move(250, 200)
        self.setWindowTitle('屏幕坐标系')

    def on_click_button(self):
        print('1')
        print(f'x = {self.x()}')  # 窗口横坐标
        print(f'y = {self.y()}')  # 窗口纵坐标
        print(f'width = {self.width()}')    # 工作区宽度
        print(f'height = {self.height()}')  # 工作区高度

        print('2')
        print(f'geometry().x = {self.geometry().x()}')  # 工作区横坐标
        print(f'geometry().y = {self.geometry().y()}')  # 工作区纵坐标
        print(f'geometry().width = {self.geometry().width()}')    # 工作区宽度
        print(f'geometry().height = {self.geometry().height()}')  # 工作区高度

        print('3')
        print(f'frameGeometry().x = {self.frameGeometry().x()}')  # 窗口横坐标
        print(f'frameGeometry().y = {self.frameGeometry().y()}')  # 窗口纵坐标
        print(f'frameGeometry().width = {self.frameGeometry().width()}')    # 窗口宽度
        print(f'frameGeometry().height = {self.frameGeometry().height()}')  # 窗口高度


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScreenGeometry()
    window.show()

    sys.exit(app.exec_())
