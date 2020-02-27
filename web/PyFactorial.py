import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import QWebChannel
from factorial import Factorial

channel = QWebChannel()
factorial = Factorial()


class PyFactorial(QWidget):
    def __init__(self):
        super(PyFactorial, self).__init__()
        self.setWindowTitle('Python计算阶乘')
        self.resize(600, 500)

        layout = QVBoxLayout()
        self.browser = QWebEngineView()
        url = os.getcwd() + '/templates/test3.html'
        self.browser.load(QUrl.fromLocalFile(url))

        channel.registerObject('obj', factorial)
        self.browser.page().setWebChannel(channel)

        layout.addWidget(self.browser)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PyFactorial()
    window.show()
    sys.exit(app.exec_())
