"""
滑动控件（QSlider）
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('滑块控件显示')
        self.resize(300, 700)

        layout = QVBoxLayout()
        self.label = QLabel('Hello World')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(12)
        self.slider.setMaximum(48)
        # 步长
        self.slider.setSingleStep(3)
        # 设置当前值
        self.slider.setValue(18)
        # 设置刻度的位置，刻度在下方
        self.slider.setTickPosition(QSlider.TicksBelow)
        # 设置刻度的间隔
        self.slider.setTickInterval(6)
        self.slider.valueChanged.connect(self.value_change)
        layout.addWidget(self.slider)

        self.slider1 = QSlider(Qt.Vertical)
        self.slider1.setMinimum(10)
        self.slider1.setMaximum(60)
        # 步长
        self.slider1.setSingleStep(4)
        # 设置当前值
        self.slider1.setValue(18)
        # 设置刻度的位置，刻度在下方
        self.slider1.setTickPosition(QSlider.TicksLeft)
        # 设置刻度的间隔
        self.slider1.setTickInterval(2)
        self.slider1.valueChanged.connect(self.value_change1)
        layout.addWidget(self.slider1)

        self.setLayout(layout)

    def value_change(self):
        print(f'当前值：{self.slider.value()}')
        size = self.slider.value()
        self.label.setFont(QFont('Arial', size))

    def value_change1(self):
        print(f'当前值：{self.slider1.value()}')
        size = self.slider1.value()
        self.label.setFont(QFont('Arial', size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QSliderDemo()
    window.show()
    sys.exit(app.exec_())
