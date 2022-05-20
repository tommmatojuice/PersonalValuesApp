from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import QSize
from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class CardsListView(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setIconSize(QSize(443, 250))
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setAcceptDrops(True)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
