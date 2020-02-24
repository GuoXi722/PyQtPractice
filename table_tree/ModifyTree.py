import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ModifyTree(QWidget):
    def __init__(self):
        super(ModifyTree, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('添加、修改、删除节点')

        hlayout = QHBoxLayout()

        addButton = QPushButton('添加节点')
        updateButton = QPushButton('修改节点')
        deleteButton = QPushButton('删除节点')

        hlayout.addWidget(addButton)
        hlayout.addWidget(updateButton)
        hlayout.addWidget(deleteButton)

        addButton.clicked.connect(self.addNode)
        updateButton.clicked.connect(self.updateNode)
        deleteButton.clicked.connect(self.deleteNode)

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

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.tree)
        self.setLayout(vlayout)

    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print(f'(key={item.text(0)}, value={item.text(1)})')

    def addNode(self):
        print('添加节点')
        item = self.tree.currentItem()
        print(item)
        node = QTreeWidgetItem(item)
        node.setText(0, '新节点')
        node.setText(1, '新值')

    def updateNode(self):
        print('修改节点')
        item = self.tree.currentItem()
        item.setText(0, '修改节点')
        item.setText(1, '修改值')

    def deleteNode(self):
        print('删除节点')
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():

            (item.parent() or root).removeChild(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModifyTree()
    window.show()
    sys.exit(app.exec_())
