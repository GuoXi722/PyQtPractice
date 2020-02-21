import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QColorDialog(QWidget):
    def __init__(self):
        super(QColorDialog, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Color Dialog案例')

        layout = QVBoxLayout()

        self.color_button = QPushButton('选择颜色')
        self.color_button.clicked.connect(self.get_color)
        self.label = QLabel('Hello World')
        layout.addWidget(self.color_button)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def get_color(self):
        color= QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.label.setPalette(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QColorDialog()
    window.show()
    sys.exit(app.exec_())
