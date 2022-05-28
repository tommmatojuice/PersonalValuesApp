from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt, QModelIndex
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy

from database import AppDataBase
from page_window import PageWindow
from user_save_page import UserSavePage


class SavesPage(PageWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Personal Values")
        self.stacked_widget = QWidget()
        self.db = AppDataBase()

        prev_button = QPushButton('Back')
        prev_button.clicked.connect(lambda: self.goto("menu"))
        space_item = QSpacerItem(0, 0, QSizePolicy.Expanding)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(prev_button)
        buttons_layout.addSpacerItem(space_item)

        self.view = ListView(self)
        self.view.clicked.connect(self.goto_save)
        self.title = QLabel('Saves', self)
        self.title.setContentsMargins(0, 0, 0, 20)
        self.title.setFont(QFont('Roboto', 17))
        self.view.add_items()

        main_layout = QVBoxLayout()
        layout = QVBoxLayout()
        layout.setContentsMargins(100, 50, 100, 50)
        layout.addWidget(self.title, alignment=Qt.AlignLeft)
        layout.addWidget(self.view)
        main_layout.addLayout(layout)
        main_layout.addLayout(buttons_layout)

        self.stacked_widget.setLayout(main_layout)
        self.setCentralWidget(self.stacked_widget)

    def goto_save(self, index: QModelIndex):
        name = self.view.model().data(index)
        date = self.view.model().data(self.view.model().index(index.row(), 1))
        df = self.db.get_save(name, date)
        self.parent.register(UserSavePage(df, self), "user_save")
        self.goto("user_save")


class ListView(QtWidgets.QTreeView):
    def __init__(self, *args, **kwargs):
        super(ListView, self).__init__(*args, **kwargs)
        self.setModel(QtGui.QStandardItemModel(self))
        self.model().setColumnCount(2)
        self.setRootIsDecorated(False)
        self.setAllColumnsShowFocus(True)
        self.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.setHeaderHidden(True)
        self.header().setStretchLastSection(False)
        self.header().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.header().setSectionResizeMode(
            1, QtWidgets.QHeaderView.ResizeToContents)
        self.db = AppDataBase()

    def add_items(self):
        saves = self.db.get_all_saver()
        for index, row in saves.iterrows():
            first = QtGui.QStandardItem(row['name'])
            first.setSizeHint(QSize(0, 50))
            second = QtGui.QStandardItem(row['date'][:-3])
            second.setTextAlignment(Qt.AlignCenter)
            self.model().appendRow([first, second])
