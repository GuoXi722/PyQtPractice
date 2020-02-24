import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class TreeEvent(QMainWindow):
    def __init__(self):
        super(TreeEvent, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('设置树的响应事件')
        self.tree = QTreeWidget()
        # 为树指定列数
        self.tree.setColumnCount(2)
        # 指定列标签
        self.tree.setHeaderLabels(['key', 'value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, '根节点')
        root.setText(1, '0')
        self.tree.setColumnWidth(0, 160)

        # 添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, '子节点1')
        child1.setText(1, '1')

        # 添加子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, '子节点2')
        child2.setText(1, '2')

        # 为子节点2添加一个子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, '子节点2-1')
        child3.setText(1, '3')

        self.tree.clicked.connect(self.onTreeClicked)

        self.setCentralWidget(self.tree)

    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print(f'(key={item.text(0)}, value={item.text(1)})')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TreeEvent()
    window.show()
    sys.exit(app.exec_())
