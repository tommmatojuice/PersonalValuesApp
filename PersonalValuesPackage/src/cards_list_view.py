from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import QSize
from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class CardsListView(QListWidget):
    """
    Class describes own QListWidget with changed parameters
    """
    def __init__(self, parent=None):
        """
        Initializing a ListView:

        :param parent: class-parent with page with this list
        """
        super().__init__(parent)
        self.parent = parent
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setAcceptDrops(True)
        self.parent.setStyleSheet("selection-background-color: #0000FFFF;")
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def viewOptions(self) -> QStyleOptionViewItem:
        """
        Changing the position of card in list to top-position
        :return:
        """
        self.setIconSize(QSize(self.size().width() - 45, 150))
        option = QListWidget.viewOptions(self)
        option.decorationPosition = QStyleOptionViewItem.Top
        return option
