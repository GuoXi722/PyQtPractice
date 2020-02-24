import sys
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrintDialog, QPrinter


class PrintDialog(QWidget):
    def __init__(self):
        super(PrintDialog, self).__init__()
        self.printer = QPrinter()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('打印对话框')

        self.editor = QTextEdit(self)
        self.editor.setGeometry(20, 20, 300, 270)

        self.openButton = QPushButton('打开文件', self)
        self.openButton.move(350, 20)

        self.settingsButton = QPushButton('打印设置', self)
        self.settingsButton.move(350, 50)

        self.printButton  = QPushButton('打印文档', self)
        self.printButton.move(350, 80)

        self.openButton.clicked.connect(self.openFile)
        self.settingsButton.clicked.connect(self.showSettingsDialog)
        self.printButton.clicked.connect(self.showPrintDialog)

    # 打开文件
    def openFile(self):
        file = QFileDialog.getOpenFileName(self, '打开文件')
        if file[0]:
            with open(file[0], 'r', encoding='utf-8', errors='ignore') as f:
                self.editor.setText(f.read())

    # 显示d打印设置对话
    def showSettingsDialog(self):
        printDialog =QPageSetupDialog(self.printer, self)
        printDialog.exec()

    # 显示打印对话框
    def showPrintDialog(self):
        printDailog = QPrintDialog(self.printer, self)
        if QDialog.Accepted == printDailog.exec():
            self.editor.print(self.printer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PrintDialog()
    window.show()
    sys.exit(app.exec_())
