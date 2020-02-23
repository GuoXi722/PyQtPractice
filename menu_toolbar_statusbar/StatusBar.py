import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class StatusBar(QMainWindow):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('状态栏演示')
        self.resize(300, 200)

        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('Show')
        file.triggered.connect(self.processTrigger)
        self.setCentralWidget(QTextEdit())
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def processTrigger(self, q):
        if q.text() == 'Show':
            self.statusBar.showMessage(q.text() + '菜单被点击了', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StatusBar()
    window.show()
    sys.exit(app.exec_())
