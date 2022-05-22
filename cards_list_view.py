from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui


class CardsListView(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setAcceptDrops(True)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def viewOptions(self) -> QStyleOptionViewItem:
        print(self.size())
        self.setIconSize(QSize(self.size().width()-75, 150))
        option = QListWidget.viewOptions(self)
        option.decorationPosition = QStyleOptionViewItem.Top
        return option
