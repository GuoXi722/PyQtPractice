"""
对话框：QDialog

QMessageBox
QColorDialog
QFileDialog
QFontDialog
QInputDialog
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QDialog案例')
        self.resize(300, 200)

        self.button = QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(50, 50)
        self.button.clicked.connect(self.show_dialog)

    def show_dialog(self):
        dialog = QDialog()
        button = QPushButton('确定', dialog)
        button.clicked.connect(dialog.close)
        button.move(50, 50)
        dialog.setWindowTitle('对话框')
        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialogDemo()
    window.show()
    sys.exit(app.exec_())