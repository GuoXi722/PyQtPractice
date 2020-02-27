import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class RightBottomButton(QWidget):
    def __init__(self):
        super(RightBottomButton, self).__init__()
        self.setWindowTitle('让按钮永远在右下角')
        self.resize(300, 400)

        okButton = QPushButton('确定')
        cancelButton = QPushButton('取消')

        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(okButton)
        hlayout.addWidget(cancelButton)

        vlayout = QVBoxLayout()
        button1 = QPushButton('按钮1')
        button2 = QPushButton('按钮2')
        button3 = QPushButton('按钮3')

        vlayout.addStretch(0)
        vlayout.addWidget(button1)
        vlayout.addWidget(button2)
        vlayout.addWidget(button3)
        vlayout.addStretch(1)
        vlayout.addLayout(hlayout)

        self.setLayout(vlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RightBottomButton()
    window.show()
    sys.exit(app.exec_())
