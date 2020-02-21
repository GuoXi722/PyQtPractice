import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QSpinBox演示')
        self.resize(300, 100)

        layout = QVBoxLayout()

        self.label = QLabel('当前值')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.spin_box = QSpinBox()
        self.spin_box.setValue(18)
        self.spin_box.setRange(10, 40)
        self.spin_box.setSingleStep(3)
        self.spin_box.valueChanged.connect(self.value_change)
        layout.addWidget(self.spin_box)

        self.setLayout(layout)

    def value_change(self):
        self.label.setText(f'当前值: {self.spin_box.value()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QSpinBoxDemo()
    window.show()
    sys.exit(app.exec_())
