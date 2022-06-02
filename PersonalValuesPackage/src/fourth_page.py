from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from PersonalValuesPackage.src.enter_name_page import EnterNamePage
from PersonalValuesPackage.src.page_window import PageWindow


class FourthPage(PageWindow):
    """
    Class with the fourth page of test
    """
    def __init__(self, cards_list, parent=None):
        """
        Initializing the page:

        :param cards_list: list of very important cards
        :param parent: class-parent
        """
        super().__init__(parent)
        self.setWindowTitle("Personal Values Test")
        self.parent = parent
        self.cards_list = cards_list
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setStyleSheet("background-color: rgb(231, 242, 248);\n")
        self.grid_layout_main = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setContentsMargins(100, 40, 250, 20)
        self.table_view = QListWidget(self)
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setMinimumSize(QtCore.QSize(600, 0))
        self.table_view.setMaximumSize(QtCore.QSize(600, 16777215))
        self.table_view.setStyleSheet("background-color: rgb(243, 234, 227);\n"
                                      "alternate-background-color: rgb(225, 216, 209);"
                                      "border : 0px;")
        self.grid_layout.addWidget(self.table_view, 1, 2, 1, 1)
        self.vertical_layout_text = QtWidgets.QVBoxLayout()
        self.label_cong = QtWidgets.QLabel(self.central_widget)
        self.label_cong.setMinimumSize(QtCore.QSize(0, 40))
        self.label_cong.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_cong.setFont(QtGui.QFont('Roboto', 20))
        self.label_cong.setStyleSheet("color: rgb(30, 72, 154);\n")
        self.label_cong.setAlignment(QtCore.Qt.AlignCenter)
        self.vertical_layout_text.addWidget(self.label_cong)
        self.label_having = QtWidgets.QLabel(self.central_widget)
        self.label_having.setFont(QtGui.QFont('Roboto', 16))
        self.label_having.setStyleSheet("color: rgb(30, 72, 154);")
        self.label_having.setAlignment(QtCore.Qt.AlignCenter)
        self.vertical_layout_text.addWidget(self.label_having)
        self.label_blue = QtWidgets.QLabel(self.central_widget)
        self.label_blue.setFont(QtGui.QFont('Roboto', 22))
        self.label_blue.setMargin(40)
        self.label_blue.setStyleSheet("background-color: rgb(56, 156, 216);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius : 16;")
        self.label_blue.setAlignment(QtCore.Qt.AlignCenter)
        self.vertical_layout_text.addWidget(self.label_blue)
        self.label_take = QtWidgets.QLabel(self.central_widget)
        self.label_take.setFont(QtGui.QFont('Roboto', 18, italic=True))
        self.label_take.setStyleSheet("color: rgb(30, 72, 154);")
        self.label_take.setAlignment(QtCore.Qt.AlignCenter)
        self.vertical_layout_text.addWidget(self.label_take)
        self.grid_layout.addLayout(self.vertical_layout_text, 0, 4, 2, 1)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item, 1, 3, 1, 1)
        self.label_title = QtWidgets.QLabel(self.central_widget)
        self.label_title.setMargin(24)
        self.label_title.setFont(QtGui.QFont('Roboto', 16))
        self.label_title.setStyleSheet("background-color: rgb(135, 198, 212);\n"
                                       "color: rgb(30, 72, 154);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.label_title, 0, 2, 1, 1)
        self.vertical_layout_3 = QtWidgets.QVBoxLayout()
        self.label_1 = QtWidgets.QLabel(self.central_widget)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setContentsMargins(40, 0, 20, 0)
        self.label_1.setFont(QtGui.QFont('Roboto', 16))
        self.label_1.setStyleSheet("color: rgb(3, 67, 155);")
        self.vertical_layout_3.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(self.central_widget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setContentsMargins(40, 0, 20, 0)
        self.label_2.setFont(QtGui.QFont('Roboto', 16))
        self.label_2.setStyleSheet("color: rgb(3, 67, 155);")
        self.vertical_layout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.central_widget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setContentsMargins(40, 0, 20, 0)
        self.label_3.setFont(QtGui.QFont('Roboto', 16))
        self.label_3.setStyleSheet("color: rgb(3, 67, 155);")
        self.vertical_layout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.central_widget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setContentsMargins(40, 0, 20, 0)
        self.label_4.setFont(QtGui.QFont('Roboto', 16))
        self.label_4.setStyleSheet("color: rgb(3, 67, 155);")
        self.vertical_layout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.central_widget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setContentsMargins(40, 0, 20, 0)
        self.label_5.setFont(QtGui.QFont('Roboto', 16))
        self.label_5.setStyleSheet("color: rgb(3, 67, 155);")
        self.vertical_layout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.central_widget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setContentsMargins(40, 0, 20, 0)
        self.label_6.setFont(QtGui.QFont('Roboto', 16))
        self.label_6.setStyleSheet("color: rgb(3, 67, 155);")
        self.vertical_layout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.central_widget)
        self.label_7.setContentsMargins(40, 0, 20, 0)
        self.label_7.setFont(QtGui.QFont('Roboto', 16))
        self.label_7.setStyleSheet("color: rgb(3, 67, 155);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.vertical_layout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.central_widget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setContentsMargins(40, 0, 20, 0)
        self.label_8.setFont(QtGui.QFont('Roboto', 16))
        self.label_8.setStyleSheet("color: rgb(3, 67, 155);")
        self.vertical_layout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.central_widget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setContentsMargins(40, 0, 20, 0)
        self.label_9.setFont(QtGui.QFont('Roboto', 16))
        self.label_9.setStyleSheet("color: rgb(3, 67, 155);")
        self.vertical_layout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.central_widget)
        self.label_10.setContentsMargins(40, 0, 20, 0)
        self.label_10.setFont(QtGui.QFont('Roboto', 16))
        self.label_10.setStyleSheet("color: rgb(3, 67, 155);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.vertical_layout_3.addWidget(self.label_10)
        self.grid_layout.addLayout(self.vertical_layout_3, 1, 1, 1, 1)
        self.horizontal_layout_bottom = QtWidgets.QHBoxLayout()
        self.label_bottom = QtWidgets.QLabel(self.central_widget)
        self.label_bottom.setFont(QtGui.QFont('Roboto', 12))
        self.grid_layout_bottom = QtWidgets.QGridLayout()
        self.grid_layout_bottom.setContentsMargins(0, 0, 20, 0)
        self.label_bottom = QtWidgets.QLabel(self.central_widget)
        self.label_bottom.setMargin(20)
        self.label_bottom.setFont(QtGui.QFont('Roboto', 12))
        self.grid_layout_bottom.addWidget(self.label_bottom, 0, 0, 1, 1)
        self.quit_button = QtWidgets.QPushButton(self.central_widget)
        self.quit_button.setFont(QtGui.QFont('Roboto', 14))
        self.quit_button.setMinimumSize(QtCore.QSize(112, 44))
        self.quit_button.setMaximumSize(QtCore.QSize(112, 44))
        self.quit_button.setStyleSheet("QPushButton {\n"
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
        self.grid_layout_bottom.addWidget(self.quit_button, 0, 3, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.central_widget)
        self.save_button.setFont(QtGui.QFont('Roboto', 14))
        self.save_button.setMinimumSize(QtCore.QSize(112, 44))
        self.save_button.setMaximumSize(QtCore.QSize(112, 44))
        self.save_button.setStyleSheet("QPushButton {\n"
                                       "background-color: #389CD8;\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius : 22;\n"
                                       "border-bottom : 2px solid #2E93CF;\n"
                                       "border-right: 2px solid #2E93CF;\n"
                                       "}\n"
                                       "QPushButton::hover {\n"
                                       "background-color: #2E93CF;\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius : 22;\n"
                                       "}")
        self.grid_layout_bottom.addWidget(self.save_button, 0, 1, 1, 1)
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout_bottom.addItem(spacer_item2, 0, 2, 1, 1)
        self.grid_layout_main.addLayout(self.grid_layout_bottom, 2, 0, 1, 6)
        self.grid_layout_main.addLayout(self.grid_layout, 0, 0, 1, 6)
        self.setCentralWidget(self.central_widget)

        self.retranslate_ui()
        self.set_table()
        self.init_buttons()

    def set_table(self):
        """
        Setting list with final cards
        :return:
        """
        self.table_view.setEnabled(False)
        for i in self.cards_list:
            item = QListWidgetItem(str(i.title).upper().replace('_', ' '))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(QtGui.QFont('Roboto', 14))
            item.setForeground(QBrush(QColor('#603B00')))
            item.setSizeHint(QSize(100, 77))
            self.table_view.addItem(item)

    def init_buttons(self):
        """
        Initializing buttons
        :return: None
        """
        self.save_button.clicked.connect(self.save_click)
        self.quit_button.clicked.connect(lambda: self.goto("start"))

    def save_click(self):
        """
        Opening page to enter the name to save the result
        :return: None
        """
        dialog = EnterNamePage(self.cards_list, self.parent)
        dialog.show()

    def retranslate_ui(self):
        """
        Setting text to labels
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.label_cong.setText(_translate("MainWindow", "Congratulations!"))
        self.label_having.setText(_translate("MainWindow", "Having this exercise completed, you now have your\n"
                                                           " top 5 values listed in order of priority. Great job!\n"
                                                           "\n"
                                                           "One last thing to do is to ask yourself:"))
        self.label_blue.setText(_translate("MainWindow", "• Do I live up to my own values?\n"
                                                         "\n"
                                                         "• How are these values\n"
                                                         "represented in my current state\n"
                                                         "of life?\n"
                                                         "\n"
                                                         "• How do I implement them into\n"
                                                         "my life so that I’m happier?"))
        self.label_take.setText(_translate("MainWindow", "Take your time to think."))
        self.label_title.setText(_translate("MainWindow", "MY TOP VALUES"))
        self.label_1.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "4"))
        self.label_5.setText(_translate("MainWindow", "5"))
        self.label_6.setText(_translate("MainWindow", "6"))
        self.label_7.setText(_translate("MainWindow", "7"))
        self.label_8.setText(_translate("MainWindow", "8"))
        self.label_9.setText(_translate("MainWindow", "9"))
        self.label_10.setText(_translate("MainWindow", "10"))
        self.label_bottom.setText(
            _translate("MainWindow", "You can save your results so that you can resee them later."))
        self.save_button.setText(_translate("MainWindow", "SAVE"))
        self.quit_button.setText(_translate("MainWindow", "QUIT"))
