import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('下拉列表控件显示')
        self.resize(300, 100)

        layout = QVBoxLayout()

        self.label = QLabel('请选择编程语言')

        self.combo = QComboBox()
        self.combo.addItem('Python')
        self.combo.addItem('C++')
        self.combo.addItems(['Java', 'C#', 'Ruby'])

        self.combo.currentIndexChanged.connect(self.selection_change)

        layout.addWidget(self.label)
        layout.addWidget(self.combo)

        self.setLayout(layout)

    def selection_change(self, i):
        self.label.setText(self.combo.currentText())
        self.label.adjustSize()

        for count in range(self.combo.count()):
            print(f'item{count}={self.combo.itemText(count)}')
            print(f'current index{i}, selection changed{self.combo.currentText()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QComboBoxDemo()
    window.show()
    sys.exit(app.exec_())
