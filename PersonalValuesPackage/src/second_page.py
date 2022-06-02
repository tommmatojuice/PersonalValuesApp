from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from PersonalValuesPackage.src.cards_list_view import CardsListView
from PersonalValuesPackage.src.instruction_2 import Instruction2
from PersonalValuesPackage.src.page_window import PageWindow
from PersonalValuesPackage.src.third_page import ThirdPage


class SecondPage(PageWindow):
    """
    Class with the second page test
    """
    def __init__(self, cards_list, parent=None):
        """
        Initializing the page
        :param cards_list: list of very important cards
        :param parent: class-parent
        """
        super().__init__(parent)
        self.parent = parent
        self.cards_list = cards_list
        self.setWindowTitle("Personal Values Test")
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setStyleSheet("background-color: rgb(243, 234, 227);")
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setContentsMargins(20, 20, 20, 20)
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
        self.grid_layout_2.addWidget(self.info_button, 0, 3, 1, 1)
        self.grid_layout_2.addItem(spacer_item, 0, 0, 1, 1)
        self.grid_layout_2.addWidget(self.next_button, 0, 4, 1, 1)
        self.grid_layout_2.addWidget(self.prev_button, 0, 1, 1, 1)
        self.grid_layout_2.addItem(spacer_item, 0, 5, 1, 1)
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

        self.grid_layout.addItem(spacer_item, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.list_ghost, 1, 3, 1, 1)
        self.setCentralWidget(self.central_widget)

        self.retranslate_ui()
        self.load_icons()
        self.init_buttons()

    def retranslate_ui(self):
        """
        Setting text to labels
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.info_button.setText(_translate("MainWindow", "?"))
        self.next_button.setText(_translate("MainWindow", "NEXT"))
        self.prev_button.setText(_translate("MainWindow", "BACK"))
        self.label_important.setText(_translate("MainWindow", "VERY IMPORTANT TO ME "))
        self.label_cards.setText(_translate("MainWindow", "UNUSED CARDS"))

    def init_buttons(self):
        """
        Initializing buttons
        :return: None
        """
        self.next_button.clicked.connect(self.next_page)
        self.prev_button.clicked.connect(lambda: self.goto("first_new"))
        self.info_button.clicked.connect(self.info_page)

    def info_page(self):
        """
        Showing the page with instruction
        :return: None
        """
        dialog = Instruction2(self.parent)
        dialog.show()

    def load_icons(self):
        """
        Loading cards in list
        :return: None
        """
        if self.cards_list:
            for data in self.cards_list:
                item = QListWidgetItem()
                item.setIcon(QIcon(data.path))
                item.setData(Qt.UserRole, data)
                self.list_old_important.addItem(item)

    def next_page(self):
        """
        Going to next page
        :return: None
        """
        cards_list = []
        for x in range(self.list_new_important.count()):
            cards_list.append(self.list_new_important.item(x).data(Qt.UserRole))
        self.parent.register(ThirdPage(cards_list, self.parent), "third")
        self.goto("third")
