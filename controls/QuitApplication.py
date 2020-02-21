# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal


class QuitApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 120)
        self.setWindowTitle('退出应用程序')

        # 添加button控件
        self.button1 = QPushButton('退出程序')
        # 将信号与槽连接
        self.button1.clicked.connect(self.on_click_button)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame = QWidget()
        main_frame.setLayout(layout)

        self.setCentralWidget(main_frame)

    # 按钮点击时间的方法（自定义的槽）
    def on_click_button(self):
        sender = self.sender()
        print(sender.text(), '按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
