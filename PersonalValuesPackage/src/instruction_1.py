from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Instruction1(QMainWindow):
    """
    Class with instruction for the second step of test
    """

    def __init__(self, parent=None):
        """
        Initializing the page:

        :param parent: class-parent
        """
        super(Instruction1, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle("Instruction")
        self.resize(866, 600)
        self.central_widget = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setContentsMargins(30, 30, 30, 20)
        self.widget = QtWidgets.QWidget(self.central_widget)
        self.widget.setStyleSheet("background-color: rgb(234, 222, 213);\n"
                                  "border-radius: 26px;")
        self.grid_layout_2 = QtWidgets.QGridLayout(self.widget)
        self.grid_layout_2.setContentsMargins(20, 20, 20, 20)
        self.second_text = QtWidgets.QLabel(self.widget)
        self.second_text.setMinimumSize(QtCore.QSize(200, 20))
        self.second_text.setMaximumSize(QtCore.QSize(1000, 40))
        self.second_text.setFont(QtGui.QFont('Roboto', 14))
        self.second_text.setStyleSheet("color: rgb(96, 59, 0);")
        self.second_text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.grid_layout_2.addWidget(self.second_text, 7, 2, 1, 1)
        self.first_text = QtWidgets.QLabel(self.widget)
        self.first_text.setMaximumSize(QtCore.QSize(16777215, 120))
        self.first_text.setFont(QtGui.QFont('Roboto Medium', 14))
        self.first_text.setStyleSheet("color: rgb(96, 59, 0);")
        self.first_text.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout_2.addWidget(self.first_text, 6, 0, 1, 6)
        self.third_text = QtWidgets.QLabel(self.widget)
        self.third_text.setMaximumSize(QtCore.QSize(300, 16777215))
        self.third_text.setFont(QtGui.QFont('Roboto Medium', 14))
        self.third_text.setStyleSheet("color: rgb(96, 59, 0);")
        self.grid_layout_2.addWidget(self.third_text, 7, 3, 1, 1)
        self.bottom_text = QtWidgets.QLabel(self.widget)
        self.bottom_text.setMaximumSize(QtCore.QSize(16777215, 70))
        self.bottom_text.setFont(QtGui.QFont('Roboto', 14))
        self.bottom_text.setStyleSheet("color: rgb(96, 59, 0);")
        self.bottom_text.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout_2.addWidget(self.bottom_text, 8, 0, 1, 6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.not_important_label = QtWidgets.QLabel(self.widget)
        self.not_important_label.setMinimumSize(QtCore.QSize(0, 50))
        self.not_important_label.setMaximumSize(QtCore.QSize(16777215, 80))
        self.not_important_label.setFont(QtGui.QFont('Roboto', 12))
        self.not_important_label.setStyleSheet("color: rgb(96, 59, 0);\n"
                                               "background-color: rgb(237, 207, 159);\n"
                                               "border-radius:0px;")
        self.not_important_label.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.not_important_label)
        self.important_label = QtWidgets.QLabel(self.widget)
        self.important_label.setMaximumSize(QtCore.QSize(16777215, 80))
        self.important_label.setFont(QtGui.QFont('Roboto', 12))
        self.important_label.setStyleSheet("color: rgb(96, 59, 0);\n"
                                           "background-color: rgb(237, 207, 159);\n"
                                           "border-radius:0px;")
        self.important_label.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.important_label)
        self.very_important_label = QtWidgets.QLabel(self.widget)
        self.very_important_label.setMaximumSize(QtCore.QSize(16777215, 80))
        self.very_important_label.setFont(QtGui.QFont('Roboto', 12))
        self.very_important_label.setStyleSheet("color: rgb(96, 59, 0);\n"
                                                "background-color: rgb(237, 207, 159);\n"
                                                "border-radius:0px;")
        self.very_important_label.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.very_important_label)
        self.grid_layout_2.addLayout(self.horizontalLayout, 3, 0, 1, 6)
        self.top_label = QtWidgets.QLabel(self.widget)
        self.top_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top_label.setFont(QtGui.QFont('Roboto', 14))
        self.top_label.setStyleSheet("color: rgb(96, 59, 0);")
        self.top_label.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout_2.addWidget(self.top_label, 0, 0, 1, 6)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 3)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item, 2, 2, 1, 1)
        self.ok_button = QtWidgets.QPushButton(self.central_widget)
        self.ok_button.clicked.connect(lambda: self.close())
        self.ok_button.setFont(QtGui.QFont('Roboto', 14))
        self.ok_button.setMinimumSize(QtCore.QSize(112, 44))
        self.ok_button.setMaximumSize(QtCore.QSize(112, 44))
        self.ok_button.setStyleSheet("QPushButton {\n"
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
        self.gridLayout.addWidget(self.ok_button, 2, 1, 1, 1)
        self.gridLayout.addItem(spacer_item, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.central_widget)
        self.label_9.setMinimumSize(QtCore.QSize(0, 10))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_9.setText("")
        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 1)
        self.setCentralWidget(self.central_widget)

        self.retranslate_ui()

    def retranslate_ui(self):
        """
        Setting text to labels:

        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.second_text.setText(_translate("MainWindow", "We also would like you to sort"))
        self.first_text.setText(_translate("MainWindow", "On the right is a stack of 50 cards. Each card describes \n"
                                                         "something that may represent a personal value for you. We \n"
                                                         "would like you to look at each card and place each card \n"
                                                         "under one of the three title cards. "))
        self.third_text.setText(_translate("MainWindow", "all 50 cards."))
        self.bottom_text.setText(
            _translate("MainWindow", "After you are finished with this part, you will be asked to do \n"
                                     "one other small task."))
        self.not_important_label.setText(_translate("MainWindow", "NOT IMPORTANT TO ME"))
        self.important_label.setText(_translate("MainWindow", "IMPORTANT TO ME"))
        self.very_important_label.setText(_translate("MainWindow", "VERY IMPORTANT TO ME"))
        self.top_label.setText(_translate("MainWindow", "There are three title cards in front of you:"))
        self.ok_button.setText(_translate("MainWindow", "OK"))
