import sys
import os
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class LocalHTML(QMainWindow):
    def __init__(self):
        super(LocalHTML, self).__init__()
        self.setWindowTitle('装载本地Web页面')
        self.setGeometry(5, 30, 1355, 730)

        url = os.getcwd() + '/templates/test1.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))

        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LocalHTML()
    window.show()
    sys.exit(app.exec_())
