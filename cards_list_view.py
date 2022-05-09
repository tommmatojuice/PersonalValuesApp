from PyQt5.QtWidgets import QListView, QAbstractItemView
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import *


class CardsListView(QListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.m_model = QStandardItemModel(self)
        self.setModel(self.m_model)
        self.setAcceptDrops(True)
        self.setIconSize(QSize(459, 250))
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.setResizeMode(QListView.ResizeMode.Adjust)
        self.setViewMode(QListView.ViewMode.IconMode)
        self.new_model = None
        self.number = None

    def dropEvent(self, event):
        super().dropEvent(event)
        data = self.new_model.item(self.new_model.rowCount() - 1).data()
        if data.column != self.number:
            if data.column == 1:
                self.parent.list_important.model().removeRow(self.parent.list_important.currentIndex().row())
            elif data.column == 2:
                self.parent.list_very_important.model().removeRow(self.parent.list_very_important.currentIndex().row())
            elif data.column == 3:
                self.parent.list_not_important.model().removeRow(self.parent.list_not_important.currentIndex().row())
            else:
                self.parent.list_cards.model().removeRow(self.parent.list_cards.currentIndex().row())
            data.column = self.number
            self.new_model.item(self.new_model.rowCount() - 1).setData(data)
