"""
显示列表数据：QListView控件
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel


class ListView(QWidget):
    def __init__(self):
        super(ListView, self).__init__()
        self.setWindowTitle('QListView 演示')
        self.resize(300, 270)
        layout = QVBoxLayout()

        listView = QListView()
        listModel = QStringListModel()
        self.list = ['列表项1', '列表项2', '列表项3']

        listModel.setStringList(self.list)
        listView.setModel(listModel)
        listView.clicked.connect(self.clicked)
        layout.addWidget(listView)

        self.setLayout(layout)

    def clicked(self, item):
        QMessageBox.information(self, 'QListView', f'您选择了：{self.list[item.row()]}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ListView()
    window.show()
    sys.exit(app.exec_())
