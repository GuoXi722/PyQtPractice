import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        bar = self.menuBar()  # 获取菜单栏

        file = bar.addMenu('File')
        file.addAction('New')

        save = QAction('Save', self)
        save.setShortcut('Ctrl + S')
        file.addAction(save)

        save.triggered.connect(self.process)

        edit = bar.addMenu('Edit')
        edit.addAction('Copy')
        edit.addAction('Paste')
        quit = QAction('Quit', self)
        file.addAction(quit)

    def process(self, a):
        print(self.sender().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec_())
