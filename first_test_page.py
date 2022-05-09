import sys
import os
import glob

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QStandardItem
from PyQt5.QtWidgets import *

from card import Card
from cards_list_view import CardsListView
from page_window import PageWindow
from second_test_page import SecondPage


class FirstPage(PageWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Personal Values")
        self.stacked_widget = QWidget()

        main_layout = QVBoxLayout()
        lists_layout = QHBoxLayout()
        titles_layout = QHBoxLayout()
        buttons_layout = QHBoxLayout()
        self.stacked_widget.setLayout(main_layout)
        self.setCentralWidget(self.stacked_widget)

        self.label_important = QLabel('Important to me', self)
        self.label_important.setAlignment(Qt.AlignCenter)
        self.label_very_important = QLabel('Very important to me', self)
        self.label_very_important.setAlignment(Qt.AlignCenter)
        self.label_not_important = QLabel('Not important to me', self)
        self.label_not_important.setAlignment(Qt.AlignCenter)
        self.label_cards = QLabel('All cards', self)
        self.label_cards.setAlignment(Qt.AlignCenter)
        titles_layout.addWidget(self.label_important)
        titles_layout.addWidget(self.label_very_important)
        titles_layout.addWidget(self.label_not_important)
        titles_layout.addWidget(self.label_cards)

        self.list_important = CardsListView(self)
        lists_layout.addWidget(self.list_important)

        self.list_very_important = CardsListView(self)
        lists_layout.addWidget(self.list_very_important)

        self.list_not_important = CardsListView(self)
        lists_layout.addWidget(self.list_not_important)

        self.list_cards = CardsListView(self)
        lists_layout.addWidget(self.list_cards)

        self.next_button = QPushButton('Next')
        self.prev_button = QPushButton('Back')
        self.spaceItem = QSpacerItem(0, 0, QSizePolicy.Expanding)

        self.next_button.clicked.connect(self.print_list)
        buttons_layout.addWidget(self.prev_button)
        buttons_layout.addSpacerItem(self.spaceItem)
        buttons_layout.addWidget(self.next_button)

        main_layout.addLayout(titles_layout)
        main_layout.addLayout(lists_layout)
        main_layout.addLayout(buttons_layout)

        self.list_important.new_model = self.list_important.model()
        self.list_very_important.new_model = self.list_very_important.model()
        self.list_not_important.new_model = self.list_not_important.model()
        self.list_cards.new_model = self.list_cards.model()

        self.list_important.number = 1
        self.list_very_important.number = 2
        self.list_not_important.number = 3
        self.list_cards.number = 4

        self.load_icons()

    def init_buttons(self):
        pass

    def load_icons(self):
        icon_folder = os.path.join(os.getcwd(), 'icons')
        i = 0
        for icon in glob.glob(os.path.join(icon_folder, '*.svg')):
            item = QStandardItem()
            item.setIcon(QIcon(icon))
            item.setData(Card(i, 4, icon[icon.rfind('\\') + 1:-4], icon))
            i += 1
            self.list_cards.m_model.appendRow(item)

    def print_list(self):
        cards_list = []
        model = self.list_very_important.model()
        for index in range(self.list_very_important.model().rowCount()):
            cards_list.append(model.item(index).data())

        self.parent.register(SecondPage(cards_list, self), "second")
        self.goto("second")
