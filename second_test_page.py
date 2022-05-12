from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from datetime import datetime

from cards_list_view import CardsListView
from database import AppDataBase
from page_window import PageWindow


class SecondPage(PageWindow):
    def __init__(self, cards_list, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.cards_list = cards_list
        self.setWindowTitle("Personal Values")
        self.stacked_widget = QWidget()
        self.db = AppDataBase()

        main_layout = QVBoxLayout()
        lists_layout = QHBoxLayout()
        titles_layout = QHBoxLayout()
        buttons_layout = QHBoxLayout()
        self.stacked_widget.setLayout(main_layout)
        self.setCentralWidget(self.stacked_widget)
        self.spaceItem = QSpacerItem(0, 0, QSizePolicy.Expanding)

        self.label_new_important = QLabel('Resulted values', self)
        self.label_new_important.setMinimumWidth(460)
        self.label_old_important = QLabel('Very important to me', self)
        self.label_old_important.setMinimumWidth(460)
        self.label_new_important.setAlignment(Qt.AlignCenter)
        self.label_old_important.setAlignment(Qt.AlignCenter)
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

        self.save_button = QPushButton('Save')
        self.prev_button = QPushButton('Back')

        self.save_button.clicked.connect(self.save_result)
        buttons_layout.addWidget(self.prev_button)
        buttons_layout.addSpacerItem(self.spaceItem)
        buttons_layout.addWidget(self.save_button)

        main_layout.addLayout(titles_layout)
        main_layout.addLayout(lists_layout)
        main_layout.addLayout(buttons_layout)

        self.load_icons()

    def init_buttons(self):
        pass

    def load_icons(self):
        if self.cards_list:
            for data in self.cards_list:
                item = QListWidgetItem()
                item.setIcon(QIcon(data.path))
                item.setData(Qt.UserRole, data)
                self.list_old_important.addItem(item)

    def save_result(self):
        text, ok = QInputDialog.getText(self, 'Saving', 'Enter your name:')
        if ok:
            check_id = self.db.get_user_id(text)
            if check_id is None:
                user_id = self.db.insert_user(text)
            else:
                user_id = check_id
            for x in range(self.list_new_important.count()):
                self.db.insert_result(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                      user_id,
                                      self.list_new_important.item(x).data(Qt.UserRole).path)
