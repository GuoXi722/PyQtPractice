"""
容纳多文档窗口
QMdiArea
QMdiSubWindow
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MultiWindows(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MultiWindows, self).__init__(parent)
        self.setWindowTitle('容纳多文档窗口')

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('New')
        file.addAction('Cascade')
        file.addAction('Tiled')

        file.triggered.connect(self.windowAction)

    def windowAction(self, q):
        print(q.text())
        if q.text() == 'New':
            MultiWindows.count = MultiWindows.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle(f'子窗口{MultiWindows.count}')
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == 'Cascade':
            self.mdi.cascadeSubWindows()
        elif q.text() == 'Tiled':
            self.mdi.tileSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MultiWindows()
    window.show()
    sys.exit(app.exec_())
