import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Toolbar(QMainWindow):
    def __init__(self):
        super(Toolbar, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('工具栏例子')
        self.resize(300, 200)

        tb1 = self.addToolBar('File')

        new = QAction(QIcon('./images/new.png'), 'new', self)
        tb1.addAction(new)

        open = QAction(QIcon('./images/open.png'), 'open', self)
        tb1.addAction(open)
        save = QAction(QIcon('./images/save.png'), 'save', self)
        tb1.addAction(save)

        tb2 = self.addToolBar('File1')
        new1 = QAction(QIcon('./images/new.png'), '新建', self)
        tb2.addAction(new1)

        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        tb1.actionTriggered.connect(self.toolButtonProcessed)

    def toolButtonProcessed(self, a):
        print(a.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Toolbar()
    window.show()
    sys.exit(app.exec_())
