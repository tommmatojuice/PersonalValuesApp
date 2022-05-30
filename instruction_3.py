from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Instruction3(QMainWindow):
    def __init__(self, parent=None):
        super(Instruction3, self).__init__(parent)
        self.resize(866, 603)
        self.central_widget = QtWidgets.QWidget()
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setContentsMargins(30, 30, 30, 20)
        self.text = QtWidgets.QLabel(self.central_widget)
        self.text.setFont(QtGui.QFont('Roboto', 18))
        self.text.setStyleSheet("color: rgb(96, 59, 0);\n"
                                "background-color: rgb(234, 222, 213);\n"
                                "border-radius : 26;")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.text, 1, 0, 1, 3)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item, 3, 2, 1, 1)
        self.grid_layout.addItem(spacer_item, 3, 0, 1, 1)
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
        self.grid_layout.addWidget(self.ok_button, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.central_widget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_2.setText("")
        self.grid_layout.addWidget(self.label_2, 2, 1, 1, 1)
        self.setCentralWidget(self.central_widget)

        self.retranslate_ui()

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.text.setText(_translate("MainWindow", "In this step, we suggest that you put values \n"
                                                   "in order, starting from most important to less\n"
                                                   "important.\n"
                                                   "\n"
                                                   "This is the last task of the test."))
        self.ok_button.setText(_translate("MainWindow", "OK"))
