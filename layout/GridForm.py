"""
栅格布局：表单设计
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class GridForm(QWidget):
    def __init__(self):
        super(GridForm, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('栅格布局：表单设计')
        self.resize(350, 300)

        titleLabel = QLabel('标题')
        authLabel = QLabel('作者')
        contentLabel = QLabel('内容')

        titleEdit = QLineEdit()
        authEdit = QLineEdit()
        contentEdit = QTextEdit()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.addWidget(titleLabel, 0, 0)
        layout.addWidget(titleEdit, 0, 1)
        layout.addWidget(authLabel, 1, 0)
        layout.addWidget(authEdit, 1, 1)
        layout.addWidget(contentLabel, 2, 0)
        layout.addWidget(contentEdit, 2, 1, 5, 1)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GridForm()
    window.show()
    sys.exit(app.exec_())
