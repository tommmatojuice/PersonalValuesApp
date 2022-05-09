import sys

from PyQt5.QtGui import QStandardItem, QIcon
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

from cards_list_view import CardsListView
from page_window import PageWindow


class SecondPage(PageWindow):
    def __init__(self, cards_list, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.cards_list = cards_list
        self.setWindowTitle("Personal Values")
        self.stacked_widget = QWidget()

        main_layout = QVBoxLayout()
        lists_layout = QHBoxLayout()
        titles_layout = QHBoxLayout()
        buttons_layout = QHBoxLayout()
        self.stacked_widget.setLayout(main_layout)
        self.setCentralWidget(self.stacked_widget)
        self.spaceItem = QSpacerItem(0, 0, QSizePolicy.Expanding)

        self.label_new_important = QLabel('5 very important to me', self)
        self.label_new_important.setAlignment(Qt.AlignCenter)
        self.label_new_important.setMinimumWidth(460)
        self.label_old_important = QLabel('Very important to me', self)
        self.label_old_important.setAlignment(Qt.AlignCenter)
        self.label_old_important.setMinimumWidth(460)
        titles_layout.addSpacerItem(self.spaceItem)
        titles_layout.addWidget(self.label_new_important)
        titles_layout.addWidget(self.label_old_important)
        titles_layout.addSpacerItem(self.spaceItem)

        lists_layout.addSpacerItem(self.spaceItem)
        self.list_new_important = CardsListView(self)
        lists_layout.addWidget(self.list_new_important)

        self.list_old_important = CardsListView(self)
        lists_layout.addWidget(self.list_old_important)
        lists_layout.addSpacerItem(self.spaceItem)

        self.next_button = QPushButton('Next')
        self.prev_button = QPushButton('Back')

        self.next_button.clicked.connect(self.print_list)
        buttons_layout.addWidget(self.prev_button)
        buttons_layout.addSpacerItem(self.spaceItem)
        buttons_layout.addWidget(self.next_button)

        main_layout.addLayout(titles_layout)
        main_layout.addLayout(lists_layout)
        main_layout.addLayout(buttons_layout)

        self.list_new_important.new_model = self.list_new_important.model()
        self.list_old_important.new_model = self.list_old_important.model()

        self.list_new_important.number = 1
        self.list_old_important.number = 2

        self.load_icons()

    def init_buttons(self):
        pass

    def load_icons(self):
        if self.cards_list:
            for data in self.cards_list:
                item = QStandardItem()
                item.setIcon(QIcon(data.path))
                data.column = 2
                item.setData(data)
                self.list_old_important.m_model.appendRow(item)

    def print_list(self):
        model = self.list_very_important.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            print(item.data().title)
