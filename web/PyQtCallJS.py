import sys
import os
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class PyQtCallJS(QWidget):
    def __init__(self):
        super(PyQtCallJS, self).__init__()
        self.setWindowTitle('PyQt5调用JavaScript')
        self.setGeometry(5, 30, 1355, 730)

        url = os.getcwd() + '/templates/test2.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        button = QPushButton('设置全名')
        layout.addWidget(button)
        button.clicked.connect(self.fullname)
        self.setLayout(layout)

    def js_callback(self, result):
        print(result)

    def fullname(self):
        self.value = 'Hello World'
        self.browser.page().runJavaScript(f'fullname("{self.value}");', self.js_callback)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PyQtCallJS()
    window.show()
    sys.exit(app.exec_())
