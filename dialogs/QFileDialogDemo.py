import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('File Dialog案例')
        layout = QVBoxLayout()

        self.button1 = QPushButton('加载图片')
        self.button1.clicked.connect(self.loadImage)
        layout.addWidget(self.button1)

        self.imageLabel = QLabel()
        layout.addWidget(self.imageLabel)

        self.button2 = QPushButton('打开文件')
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)

    def loadImage(self):
        f, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件(*.jpg, *.png)')
        self.imageLabel.setPixmap(QPixmap(f))

    def loadText(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            f = open(filenames[0], 'r')
            with f:
                data = f.read()
                self.contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QFileDialogDemo()
    window.show()
    sys.exit(app.exec_())
