from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from cards_list_view import CardsListView
from page_window import PageWindow


class ThirdPage(PageWindow):
    def __init__(self, cards_list, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.cards_list = cards_list
        self.lists = []
        self.cards_list_copy = cards_list
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setStyleSheet("background-color: rgb(231, 242, 248);\n")
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setContentsMargins(20, 20, 20, 20)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item, 2, 1, 1, 1)
        self.list_cards = CardsListView(self)
        self.list_cards.setMinimumWidth(465)
        self.list_cards.setStyleSheet("background-color: rgb(205, 224, 229);\n"
                                      "border : 0px;")
        self.grid_layout.addWidget(self.list_cards, 2, 0, 1, 1)
        self.grid_layout_3 = QtWidgets.QGridLayout()
        self.grid_layout_3.setContentsMargins(0, 10, 0, 10)
        self.value_6 = QtWidgets.QLabel(self.central_widget)
        self.value_6.setContentsMargins(40, 0, 20, 0)
        self.value_6.setFont(QtGui.QFont('Roboto', 18))
        self.value_6.setStyleSheet("color: rgb(3, 67, 155);")
        self.grid_layout_3.addWidget(self.value_6, 0, 2, 1, 1)
        self.value_2 = QtWidgets.QLabel(self.central_widget)
        self.value_2.setContentsMargins(0, 0, 20, 0)
        self.value_2.setFont(QtGui.QFont('Roboto', 18))
        self.value_2.setStyleSheet("color: rgb(3, 67, 155);")
        self.grid_layout_3.addWidget(self.value_2, 2, 0, 1, 1)
        self.value_4 = QtWidgets.QLabel(self.central_widget)
        self.value_4.setContentsMargins(0, 0, 20, 0)
        self.value_4.setFont(QtGui.QFont('Roboto', 18))
        self.value_4.setStyleSheet("color: rgb(3, 67, 155);")
        self.grid_layout_3.addWidget(self.value_4, 6, 0, 1, 1)

        self.list_value_1 = CardsListView(self)
        self.list_value_1.setStyleSheet("background-color: rgb(252, 249, 240);\n"
                                        "border-color: rgb(56, 156, 216);\n"
                                        "border-width: 3px;\n"
                                        "border-style: dashed;\n"
                                        "border-radius : 22;")
        self.list_value_1.setMinimumWidth(470)
        self.grid_layout_3.addWidget(self.list_value_1, 0, 1, 1, 1)
        self.lists.append(self.list_value_1)

        self.list_value_2 = CardsListView(self)
        self.list_value_2.setStyleSheet("background-color: rgb(252, 249, 240);\n"
                                        "border-color: rgb(56, 156, 216);\n"
                                        "border-width: 3px;\n"
                                        "border-style: dashed;\n"
                                        "border-radius : 22;")
        self.grid_layout_3.addWidget(self.list_value_2, 2, 1, 1, 1)
        self.lists.append(self.list_value_2)

        self.list_value_3 = CardsListView(self)
        self.list_value_3.setStyleSheet("background-color: rgb(252, 249, 240);\n"
                                        "border-color: rgb(56, 156, 216);\n"
                                        "border-width: 3px;\n"
                                        "border-style: dashed;\n"
                                        "border-radius : 22;")
        self.grid_layout_3.addWidget(self.list_value_3, 4, 1, 1, 1)
        self.lists.append(self.list_value_3)

        self.list_value_4 = CardsListView(self)
        self.list_value_4.setStyleSheet("background-color: rgb(252, 249, 240);\n"
                                        "border-color: rgb(56, 156, 216);\n"
                                        "border-width: 3px;\n"
                                        "border-style: dashed;\n"
                                        "border-radius : 22;")
        self.grid_layout_3.addWidget(self.list_value_4, 6, 1, 1, 1)
        self.lists.append(self.list_value_4)

        self.list_value_5 = CardsListView(self)
        self.list_value_5.setStyleSheet("background-color: rgb(252, 249, 240);\n"
                                        "border-color: rgb(56, 156, 216);\n"
                                        "border-width: 3px;\n"
                                        "border-style: dashed;\n"
                                        "border-radius : 22;")
        self.grid_layout_3.addWidget(self.list_value_5, 8, 1, 1, 1)
        self.lists.append(self.list_value_5)

        self.list_value_6 = CardsListView(self)
        self.list_value_6.setStyleSheet("background-color: rgb(252, 249, 240);\n"
                                        "border-color: rgb(56, 156, 216);\n"
                                        "border-width: 3px;\n"
                                        "border-style: dashed;\n"
                                        "border-radius : 22;")
        self.grid_layout_3.addWidget(self.list_value_6, 0, 3, 1, 1)
        self.lists.append(self.list_value_6)

        self.list_value_7 = CardsListView(self)
        self.list_value_7.setStyleSheet("background-color: rgb(252, 249, 240);\n"
                                        "border-color: rgb(56, 156, 216);\n"
                                        "border-width: 3px;\n"
                                        "border-style: dashed;\n"
                                        "border-radius : 22;")
        self.grid_layout_3.addWidget(self.list_value_7, 2, 3, 1, 1)
        self.lists.append(self.list_value_7)

        self.list_value_8 = CardsListView(self)
        self.list_value_8.setStyleSheet("background-color: rgb(252, 249, 240);\n"
                                        "border-color: rgb(56, 156, 216);\n"
                                        "border-width: 3px;\n"
                                        "border-style: dashed;\n"
                                        "border-radius : 22;")
        self.grid_layout_3.addWidget(self.list_value_8, 4, 3, 1, 1)
        self.lists.append(self.list_value_8)

        self.list_value_9 = CardsListView(self)
        self.list_value_9.setMinimumWidth(470)
        self.list_value_9.setStyleSheet("background-color: rgb(252, 249, 240);\n"
                                        "border-color: rgb(56, 156, 216);\n"
                                        "border-width: 3px;\n"
                                        "border-style: dashed;\n"
                                        "border-radius : 22;")
        self.grid_layout_3.addWidget(self.list_value_9, 6, 3, 1, 1)
        self.lists.append(self.list_value_9)

        self.list_value_10 = CardsListView(self)
        self.list_value_10.setStyleSheet("background-color: rgb(252, 249, 240);\n"
                                         "border-color: rgb(56, 156, 216);\n"
                                         "border-width: 3px;\n"
                                         "border-style: dashed;\n"
                                         "border-radius : 22;")
        self.grid_layout_3.addWidget(self.list_value_10, 8, 3, 1, 1)
        self.lists.append(self.list_value_10)

        self.value_8 = QtWidgets.QLabel(self.central_widget)
        self.value_8.setStyleSheet("color: rgb(3, 67, 155);")
        self.value_8.setContentsMargins(40, 0, 20, 0)
        self.value_8.setFont(QtGui.QFont('Roboto', 18))
        self.grid_layout_3.addWidget(self.value_8, 4, 2, 1, 1)
        self.value_7 = QtWidgets.QLabel(self.central_widget)
        self.value_7.setContentsMargins(40, 0, 20, 0)
        self.value_7.setFont(QtGui.QFont('Roboto', 18))
        self.value_7.setStyleSheet("color: rgb(3, 67, 155);")
        self.grid_layout_3.addWidget(self.value_7, 2, 2, 1, 1)
        self.value_9 = QtWidgets.QLabel(self.central_widget)
        self.value_9.setContentsMargins(40, 0, 20, 0)
        self.value_9.setFont(QtGui.QFont('Roboto', 18))
        self.value_9.setStyleSheet("color: rgb(3, 67, 155);")
        self.grid_layout_3.addWidget(self.value_9, 6, 2, 1, 1)
        self.value_10 = QtWidgets.QLabel(self.central_widget)
        self.value_10.setContentsMargins(40, 0, 20, 0)
        self.value_10.setFont(QtGui.QFont('Roboto', 18))
        self.value_10.setStyleSheet("color: rgb(3, 67, 155);")
        self.grid_layout_3.addWidget(self.value_10, 8, 2, 1, 1)
        spacer_item1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_layout_3.addItem(spacer_item1, 3, 1, 1, 1)
        self.grid_layout_3.addItem(spacer_item1, 5, 1, 1, 1)
        self.grid_layout_3.addItem(spacer_item1, 7, 1, 1, 1)
        self.grid_layout_3.addItem(spacer_item1, 1, 1, 1, 1)
        self.value_5 = QtWidgets.QLabel(self.central_widget)
        self.value_5.setContentsMargins(0, 0, 20, 0)
        self.value_5.setFont(QtGui.QFont('Roboto', 18))
        self.value_5.setStyleSheet("color: rgb(3, 67, 155);")
        self.grid_layout_3.addWidget(self.value_5, 8, 0, 1, 1)
        self.value_3 = QtWidgets.QLabel(self.central_widget)
        self.value_3.setContentsMargins(0, 0, 20, 0)
        self.value_3.setFont(QtGui.QFont('Roboto', 18))
        self.value_3.setStyleSheet("color: rgb(3, 67, 155);")
        self.grid_layout_3.addWidget(self.value_3, 4, 0, 1, 1)
        self.value_1 = QtWidgets.QLabel(self.central_widget)
        self.value_1.setContentsMargins(0, 0, 20, 0)
        self.value_1.setFont(QtGui.QFont('Roboto', 18))
        self.value_1.setStyleSheet("color: rgb(3, 67, 155);")
        self.grid_layout_3.addWidget(self.value_1, 0, 0, 1, 1)

        self.grid_layout.addLayout(self.grid_layout_3, 2, 2, 1, 1)
        self.label_cards = QtWidgets.QLabel(self.central_widget)
        self.label_cards.setStyleSheet("background-color: rgb(135, 198, 213);\n"
                                       "color: rgb(30, 72, 154);"
                                       "font: 57 14pt \"Roboto\";")
        self.label_cards.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.label_cards, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        spacer_item5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item5)
        self.label_important = QtWidgets.QLabel(self.central_widget)
        self.label_important.setMargin(24)
        self.label_important.setMinimumSize(QtCore.QSize(200, 0))
        self.label_important.setStyleSheet("background-color: rgb(237, 207, 159);\n"
                                           "color: rgb(96, 59, 0);"
                                           "font: 57 14pt \"Roboto\";")
        self.label_important.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.label_important)
        self.horizontalLayout.addItem(spacer_item)
        self.grid_layout.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.grid_layout.addItem(spacer_item, 2, 3, 1, 1)
        self.grid_layout_2 = QtWidgets.QGridLayout()
        self.grid_layout_2.setContentsMargins(10, 10, 10, 0)
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
        self.prev_button = QtWidgets.QPushButton(self.central_widget)
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
        self.prev_button.setFont(QtGui.QFont('Roboto', 14))
        self.grid_layout_2.addWidget(self.prev_button, 0, 1, 1, 1)
        self.grid_layout_2.addItem(spacer_item, 0, 5, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_2, 3, 0, 1, 4)
        self.setCentralWidget(self.central_widget)

        self.load_icons()
        self.init_buttons()
        self.init_buttons()
        self.retranslate_ui()

    def load_icons(self):
        if self.cards_list:
            for data in self.cards_list:
                item = QListWidgetItem()
                item.setIcon(QIcon(data.path))
                item.setData(Qt.UserRole, data)
                self.list_cards.addItem(item)

    def init_buttons(self):
        pass
        self.next_button.clicked.connect(self.next_page)
        self.prev_button.clicked.connect(self.prev_page)

    def prev_page(self):
        from second_page_new import SecondPageNew
        self.parent.register(SecondPageNew(self.cards_list_copy, self.parent), "second_new")
        self.goto("second_new")

    def next_page(self):
        cards_list = []
        for x in self.lists:
            if x.item(0):
                cards_list.append(x.item(0).data(Qt.UserRole))
        from fourth_page import FourthPage
        self.parent.register(FourthPage(cards_list, self.parent), "fourth")
        self.goto("fourth")

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.value_6.setText(_translate("MainWindow", "6"))
        self.value_2.setText(_translate("MainWindow", "2"))
        self.value_4.setText(_translate("MainWindow", "4"))
        self.value_8.setText(_translate("MainWindow", "8"))
        self.value_7.setText(_translate("MainWindow", "7"))
        self.value_9.setText(_translate("MainWindow", "9"))
        self.value_10.setText(_translate("MainWindow", "10"))
        self.value_5.setText(_translate("MainWindow", "5"))
        self.value_3.setText(_translate("MainWindow", "3"))
        self.value_1.setText(_translate("MainWindow", "1"))
        self.label_cards.setText(_translate("MainWindow", "VERY IMPORTANT TO ME"))
        self.label_important.setText(_translate("MainWindow", "MY TOP VALUES"))
        self.next_button.setText(_translate("MainWindow", "NEXT"))
        self.info_button.setText(_translate("MainWindow", "?"))
        self.prev_button.setText(_translate("MainWindow", "BACK"))
