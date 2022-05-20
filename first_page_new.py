import os
import glob

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from card import Card
from cards_list_view import CardsListView
from database import AppDataBase
from page_window import PageWindow
from second_page_new import SecondPageNew
from second_test_page import SecondPage


class FirstPageNew(PageWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Personal Values Test")
        parent.resize(851, 714)
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setStyleSheet("background-color: rgb(243, 234, 227);\n")
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setContentsMargins(20, 20, 20, 20)
        self.list_not_important = CardsListView(self)
        self.list_not_important.setStyleSheet("background-color: rgb(234, 222, 213);\n"
                                              "border : 0px;")
        self.grid_layout.addWidget(self.list_not_important, 1, 1, 1, 1)
        self.label_not_important = QtWidgets.QLabel(self.central_widget)
        self.label_not_important.setMargin(24)
        self.label_not_important.setStyleSheet("background-color: rgb(237, 207, 159);\n"
                                               "color: rgb(96, 59, 0);"
                                               "font: 57 14pt \"Roboto\";")
        self.label_not_important.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.label_not_important, 0, 1, 1, 1)
        self.label_very_important = QtWidgets.QLabel(self.central_widget)
        self.label_very_important.setStyleSheet("background-color: rgb(237, 207, 159);\n"
                                                "color: rgb(96, 59, 0);"
                                                "font: 57 14pt \"Roboto\";")
        self.label_very_important.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.label_very_important, 0, 3, 1, 1)
        self.label_cards = QtWidgets.QLabel(self.central_widget)
        self.label_cards.setStyleSheet("background-color: rgb(135, 198, 213);\n"
                                       "color: rgb(30, 72, 154);"
                                       "font: 57 14pt \"Roboto\";")
        self.label_cards.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.label_cards, 0, 4, 1, 1)
        self.list_very_important = CardsListView(self)
        self.list_very_important.setStyleSheet("background-color: rgb(234, 222, 213);\n"
                                               "border : 0px;")
        self.grid_layout.addWidget(self.list_very_important, 1, 3, 1, 1)
        self.list_cards = CardsListView(self)
        self.list_cards.setStyleSheet("background-color: rgb(205, 224, 229);\n"
                                      "border : 0px;")
        self.grid_layout.addWidget(self.list_cards, 1, 4, 1, 1)
        self.list_important = CardsListView(self)
        self.list_important.setStyleSheet("background-color: rgb(234, 222, 213);\n"
                                          "border : 0px;")
        self.grid_layout.addWidget(self.list_important, 1, 2, 1, 1)
        self.label_important = QtWidgets.QLabel(self.central_widget)
        self.label_important.setStyleSheet("background-color: rgb(237, 207, 159);\n"
                                           "color: rgb(96, 59, 0);"
                                           "font: 57 14pt \"Roboto\";")
        self.label_important.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.label_important, 0, 2, 1, 1)
        self.grid_layout_2 = QtWidgets.QGridLayout()
        self.grid_layout_2.setContentsMargins(10, 10, 10, 0)
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
        self.grid_layout_2.addWidget(self.info_button, 0, 3, 1, 1)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout_2.addItem(spacer_item, 0, 0, 1, 1)
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
        self.grid_layout_2.addWidget(self.next_button, 0, 4, 1, 1)
        self.prev_button = QtWidgets.QPushButton(self.central_widget)
        self.prev_button.setMinimumSize(QtCore.QSize(112, 44))
        self.prev_button.setMaximumSize(QtCore.QSize(112, 44))
        self.prev_button.setFont(QtGui.QFont('Roboto', 14))
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
        self.grid_layout_2.addWidget(self.prev_button, 0, 1, 1, 1)
        spacer_item_1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout_2.addItem(spacer_item_1, 0, 5, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_2, 2, 1, 1, 4)
        self.setCentralWidget(self.central_widget)
        self.retranslate_ui()
        self.load_icons()
        self.init_buttons()

    def init_buttons(self):
        self.next_button.clicked.connect(self.next_page)
        self.prev_button.clicked.connect(lambda: self.goto("start"))

    def load_icons(self):
        icon_folder = os.path.join(os.getcwd(), 'icons')
        i = 0
        for icon in glob.glob(os.path.join(icon_folder, '*.svg')):
            item = QListWidgetItem()
            item.setIcon(QIcon(icon))
            item.setData(Qt.UserRole, Card(i, icon[icon.rfind('\\') + 1:-4], icon))
            i += 1
            self.list_cards.addItem(item)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_not_important.setText(_translate("MainWindow", "NOT IMPORTANT TO ME"))
        self.label_very_important.setText(_translate("MainWindow", "VERY IMPORTANT TO ME"))
        self.label_cards.setText(_translate("MainWindow", "VALUES CARDS"))
        self.label_important.setText(_translate("MainWindow", "IMPORTANT TO ME"))
        self.info_button.setText(_translate("MainWindow", "?"))
        self.next_button.setText(_translate("MainWindow", "NEXT"))
        self.prev_button.setText(_translate("MainWindow", "BACK"))

    def next_page(self):
        cards_list = []
        for x in range(self.list_very_important.count()):
            cards_list.append(self.list_very_important.item(x).data(Qt.UserRole))
        self.parent.register(SecondPageNew(cards_list, self), "second_new")
        self.goto("second_new")
