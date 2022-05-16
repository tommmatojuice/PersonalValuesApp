from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from cards_list_view import CardsListView
from page_window import PageWindow


class UserSavePage(PageWindow):
    def __init__(self, cards_list, parent=None):
        super().__init__(parent)
        self.cards_list = cards_list
        self.parent = parent
        self.setWindowTitle("Personal Values")
        self.stacked_widget = QWidget()

        self.view = CardsListView(self)
        self.view.setFixedWidth(470)
        self.view.setAcceptDrops(False)
        self.view.setDragEnabled(False)
        self.prev_button = QPushButton('Back')
        self.spaceItem = QSpacerItem(0, 0, QSizePolicy.Expanding)

        layout = QVBoxLayout()
        lists_layout = QHBoxLayout()
        titles_layout = QHBoxLayout()
        buttons_layout = QHBoxLayout()

        lists_layout.addSpacerItem(self.spaceItem)
        lists_layout.addWidget(self.view)
        lists_layout.addSpacerItem(self.spaceItem)

        prev_button = QPushButton('Back')
        prev_button.clicked.connect(self.prev_page)
        buttons_layout.addWidget(prev_button)
        buttons_layout.addSpacerItem(self.spaceItem)

        label_title = QLabel(f'{cards_list["name"][0]} {cards_list["date"][0]}', self)
        label_title.setAlignment(Qt.AlignCenter)
        titles_layout.addSpacerItem(self.spaceItem)
        titles_layout.addWidget(label_title)
        titles_layout.addSpacerItem(self.spaceItem)

        layout.addLayout(titles_layout)
        layout.addLayout(lists_layout)
        layout.addLayout(buttons_layout)

        self.stacked_widget.setLayout(layout)
        self.setCentralWidget(self.stacked_widget)

        self.load_icons()

    def load_icons(self):
        for index, row in self.cards_list.iterrows():
            item = QListWidgetItem()
            icon = row['card_path']
            item.setIcon(QIcon(icon))
            self.view.addItem(item)

    def prev_page(self):
        self.goto("saves")
