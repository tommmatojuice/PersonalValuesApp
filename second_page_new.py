from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *
from datetime import datetime

from cards_list_view import CardsListView
from page_window import PageWindow
from third_page import ThirdPage


class SecondPageNew(PageWindow):
    def __init__(self, cards_list, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.cards_list = cards_list
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setStyleSheet("background-color: rgb(243, 234, 227);")
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setContentsMargins(20, 20, 20, 20)
        # self.grid_layout.setContentsMargins(10, -1, -1, -1)
        self.grid_layout_2 = QtWidgets.QGridLayout()
        self.grid_layout_2.setContentsMargins(10, 10, 10, 0)
        spacer_item = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.info_button = QtWidgets.QPushButton(self.central_widget)
        self.info_button.setMinimumSize(QtCore.QSize(44, 44))
        self.info_button.setMaximumSize(QtCore.QSize(44, 44))
        self.info_button.setFont(QtGui.QFont('Roboto', 16))
        self.info_button.setStyleSheet("QPushButton {\n"
                                       "background-color: rgb(88, 188, 212);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius : 22;\n"
                                       "border-bottom : 2px solid rgb(61, 161, 185);\n"
                                       "border-right: 2px solid rgb(61, 161, 185);\n"
                                       "}\n"
                                       "QPushButton::hover {\n"
                                       "background-color: rgb(61, 161, 185);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius : 22;\n"
                                       "}")
        # self.grid_layout_2.addWidget(self.info_button, 0, 2, 1, 1)
        self.next_button = QtWidgets.QPushButton(self.central_widget)
        self.next_button.setMinimumSize(QtCore.QSize(112, 44))
        self.next_button.setMaximumSize(QtCore.QSize(112, 44))
        self.next_button.setFont(QtGui.QFont('Roboto', 14))
        self.next_button.setStyleSheet("QPushButton {\n"
                                       "background-color: rgb(240, 177, 72);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius : 22;\n"
                                       "border-bottom : 2px solid rgb(227, 166, 67);\n"
                                       "border-right: 2px solid rgb(227, 166, 67);\n"
                                       "}\n"
                                       "QPushButton::hover {\n"
                                       "background-color: rgb(227, 166, 67);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius : 22;\n"
                                       "}")
        # self.grid_layout_2.addWidget(self.next_button, 0, 3, 1, 1)
        self.prev_button = QtWidgets.QPushButton(self.central_widget)
        self.prev_button.setFont(QtGui.QFont('Roboto', 14))
        self.prev_button.setMinimumSize(QtCore.QSize(112, 44))
        self.prev_button.setMaximumSize(QtCore.QSize(112, 44))
        self.prev_button.setStyleSheet("QPushButton {\n"
                                       "background-color: rgb(150, 176, 203);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius : 22;\n"
                                       "border-bottom : 2px solid rgb(140, 165, 189);\n"
                                       "border-right: 2px solid rgb(140, 165, 189);\n"
                                       "}\n"
                                       "QPushButton::hover {\n"
                                       "background-color: rgb(140, 165, 189);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius : 22;\n"
                                       "}")
        # self.grid_layout_2.addWidget(self.prev_button, 0, 1, 1, 1)
        self.grid_layout_2.addWidget(self.info_button, 0, 3, 1, 1)
        self.grid_layout_2.addItem(spacer_item, 0, 0, 1, 1)
        self.grid_layout_2.addWidget(self.next_button, 0, 4, 1, 1)
        self.grid_layout_2.addWidget(self.prev_button, 0, 1, 1, 1)
        self.grid_layout_2.addItem(spacer_item, 0, 5, 1, 1)
        # self.grid_layout.addLayout(self.grid_layout_2, 2, 2, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_2, 2, 1, 1, 4)
        self.label_important = QtWidgets.QLabel(self.central_widget)
        self.label_important.setMargin(24)
        self.label_important.setStyleSheet("background-color: rgb(237, 207, 159);\n"
                                           "color: rgb(96, 59, 0);"
                                           "font: 57 14pt \"Roboto\";")
        self.label_important.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.label_important, 0, 2, 1, 1)
        self.list_new_important = CardsListView(self)
        self.list_new_important.setMinimumWidth(443)
        self.list_new_important.setMaximumWidth(465)
        self.list_new_important.setStyleSheet("background-color: rgb(234, 222, 213);\n"
                                              "border : 0px;")
        self.grid_layout.addWidget(self.list_new_important, 1, 2, 1, 1)
        self.label_cards = QtWidgets.QLabel(self.central_widget)
        self.label_cards.setStyleSheet("background-color: rgb(135, 198, 213);\n"
                                       "color: rgb(30, 72, 154);"
                                       "font: 57 14pt \"Roboto\";")
        self.label_cards.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.label_cards, 0, 4, 1, 1)
        self.list_old_important = CardsListView(self)
        self.list_ghost = QtWidgets.QListView(self.central_widget)
        self.list_old_important.setMinimumWidth(443)
        self.list_old_important.setMaximumWidth(465)
        self.list_ghost.setMaximumWidth(220)
        self.list_ghost.setEnabled(True)
        self.list_old_important.setStyleSheet("background-color: rgb(205, 224, 229);\n"
                                      "border : 0px;")
        self.list_ghost.setStyleSheet("border : 0px;")
        self.grid_layout.addWidget(self.list_old_important, 1, 4, 1, 1)


        spacer_item_1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacer_item_2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.grid_layout_2.addItem(spacer_item_2, 0, 0, 1, 1)
        # self.grid_layout_2.addItem(spacer_item_1, 0, 4, 1, 1)
        self.grid_layout.addItem(spacer_item, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.list_ghost, 1, 3, 1, 1)
        self.setCentralWidget(self.central_widget)

        self.retranslate_ui()
        self.load_icons()
        self.init_buttons()

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.info_button.setText(_translate("MainWindow", "?"))
        self.next_button.setText(_translate("MainWindow", "NEXT"))
        self.prev_button.setText(_translate("MainWindow", "BACK"))
        self.label_important.setText(_translate("MainWindow", "VERY IMPORTANT TO ME "))
        self.label_cards.setText(_translate("MainWindow", "UNUSED CARDS"))

    def init_buttons(self):
        self.next_button.clicked.connect(self.next_page)
        self.prev_button.clicked.connect(lambda: self.goto("first_new"))

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
                self.db.insert_result(datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                                      user_id,
                                      self.list_new_important.item(x).data(Qt.UserRole).path)

    def next_page(self):
        cards_list = []
        for x in range(self.list_new_important.count()):
            cards_list.append(self.list_new_important.item(x).data(Qt.UserRole))
        self.parent.register(ThirdPage(cards_list, self.parent), "third")
        self.goto("third")
