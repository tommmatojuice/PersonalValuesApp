from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow
from database import AppDataBase
from datetime import datetime


class EnterNamePage(QMainWindow):
    def __init__(self, cards_list, parent=None):
        super(EnterNamePage, self).__init__(parent)
        self.resize(QSize(514, 343))
        self.cards_list = cards_list
        self.db = self.parent.db
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setMaximumSize(QSize(514, 343))
        self.central_widget.setStyleSheet("background-color: #F3EAE3;\n")
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setContentsMargins(40, 40, 40, 70)
        self.save_button = QtWidgets.QPushButton("SAVE")
        self.save_button.setMinimumSize(QtCore.QSize(112, 30))
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
        self.save_button.setFont(QtGui.QFont('Roboto', 14))
        self.save_button.clicked.connect(self.save_results)
        self.grid_layout.addWidget(self.save_button, 8, 2, 1, 1)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item, 8, 0, 1, 2)
        self.line_name = QtWidgets.QLineEdit(self)
        self.line_name.setMinimumSize(QtCore.QSize(340, 50))
        self.line_name.setMaximumSize(QtCore.QSize(340, 16777215))
        self.line_name.setStyleSheet("background-color: rgb(240, 177, 72);\n"
                                     "color: rgb(252, 249, 240);\n"
                                     "border-radius: 16px;"
                                     "padding: 16px;")
        self.line_name.setFont(QtGui.QFont('Roboto', 14))
        self.grid_layout.addWidget(self.line_name, 4, 1, 1, 3)
        self.grid_layout.addItem(spacer_item, 4, 0, 1, 1)
        self.label_title = QtWidgets.QLabel("Type your name to save the results:")
        self.label_title.setMargin(30)
        self.label_title.setFont(QtGui.QFont('Roboto', 14))
        self.label_title.setStyleSheet("color: rgb(96, 59, 0);")
        self.label_title.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.grid_layout.addWidget(self.label_title, 0, 0, 1, 5)
        self.grid_layout.addItem(spacer_item, 4, 4, 1, 1)
        self.grid_layout.addItem(spacer_item, 8, 3, 1, 2)
        self.grid_layout.addItem(spacer_item, 5, 0, 1, 5)
        self.setCentralWidget(self.central_widget)

    def save_results(self):
        name = self.line_name.text()
        print(name)
        check_id = self.db.get_user_id(name)
        if check_id is None:
            user_id = self.db.insert_user(name)
        else:
            user_id = check_id
        for x in self.cards_list:
            self.db.insert_result(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                  user_id,
                                  x.path)
        self.db.connection.close()
        self.close()

