import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QFontDialog(QWidget):
    def __init__(self):
        super(QFontDialog, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Font Dialog案例')

        layout = QVBoxLayout()

        self.font_button = QPushButton('选择字体')
        self.font_button.clicked.connect(self.get_font)
        self.label = QLabel('Hello World')
        layout.addWidget(self.font_button)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def get_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QFontDialog()
    window.show()
    sys.exit(app.exec_())
