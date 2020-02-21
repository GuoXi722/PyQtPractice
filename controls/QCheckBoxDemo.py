import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('复选框控件显示')

        layout = QHBoxLayout()

        self.check_box1 = QCheckBox('复选框1')
        self.check_box1.setChecked(True)
        self.check_box1.stateChanged.connect(lambda: self.check_box_state(self.check_box1))
        layout.addWidget(self.check_box1)

        self.check_box2 = QCheckBox('复选框2')
        self.check_box2.stateChanged.connect(lambda: self.check_box_state(self.check_box2))
        layout.addWidget(self.check_box2)

        self.check_box3 = QCheckBox('复选框3')
        self.check_box3.setTristate(True)
        self.check_box3.setCheckState(Qt.PartiallyChecked)
        self.check_box3.stateChanged.connect(lambda: self.check_box_state(self.check_box3))
        layout.addWidget(self.check_box3)

        self.setLayout(layout)

    def check_box_state(self, cb):
        check_state1 = f'{self.check_box1.text()}, isChecked={self.check_box1.isChecked()}, ' \
                       f'checkState={self.check_box1.checkState()}\n'
        check_state2 = f'{self.check_box2.text()}, isChecked={self.check_box2.isChecked()}, ' \
                       f'checkState={self.check_box2.checkState()}\n'
        check_state3 = f'{self.check_box3.text()}, isChecked={self.check_box3.isChecked()}, ' \
                       f'checkState={self.check_box3.checkState()}\n'

        print(check_state1 + check_state2 + check_state3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QCheckBoxDemo()
    window.show()
    sys.exit(app.exec_())
