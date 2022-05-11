import os
import glob

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
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
        self.label_very_important = QLabel('Very important to me', self)
        self.label_not_important = QLabel('Not important to me', self)
        self.label_cards = QLabel('All cards', self)
        titles_layout.addWidget(self.label_important, alignment=Qt.AlignCenter)
        titles_layout.addWidget(self.label_very_important, alignment=Qt.AlignCenter)
        titles_layout.addWidget(self.label_not_important, alignment=Qt.AlignCenter)
        titles_layout.addWidget(self.label_cards, alignment=Qt.AlignCenter)

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

        self.next_button.clicked.connect(self.next_page)
        buttons_layout.addWidget(self.prev_button)
        buttons_layout.addSpacerItem(self.spaceItem)
        buttons_layout.addWidget(self.next_button)

        main_layout.addLayout(titles_layout)
        main_layout.addLayout(lists_layout)
        main_layout.addLayout(buttons_layout)

        self.load_icons()

    def init_buttons(self):
        pass

    def load_icons(self):
        icon_folder = os.path.join(os.getcwd(), 'icons')
        i = 0
        for icon in glob.glob(os.path.join(icon_folder, '*.svg')):
            item = QListWidgetItem()
            item.setIcon(QIcon(icon))
            item.setData(Qt.UserRole, Card(i, icon[icon.rfind('\\') + 1:-4], icon))
            i += 1
            self.list_cards.addItem(item)

    def next_page(self):
        cards_list = []
        for x in range(self.list_very_important.count()):
            cards_list.append(self.list_very_important.item(x).data(Qt.UserRole))
        self.parent.register(SecondPage(cards_list, self), "second")
        self.goto("second")
