import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Color Dialog案例')

        layout = QVBoxLayout()

        self.colorButton = QPushButton('选择颜色')
        self.colorButton.clicked.connect(self.getColor)
        self.label = QLabel('Hello World')
        layout.addWidget(self.colorButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def getColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.label.setPalette(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QColorDialogDemo()
    window.show()
    sys.exit(app.exec_())
