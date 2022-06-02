from PyQt5 import QtCore, QtGui, QtWidgets

from PersonalValuesPackage.src.page_window import PageWindow


class InstructionPage(PageWindow):
    """
    Class with the instruction for the test
    """
    def __init__(self, parent=None):
        """
        Initializing the page
        :param parent: class-parent
        """
        super().__init__(parent)
        self.parent = parent
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setStyleSheet("background-color: #E7F2F8;")
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setContentsMargins(40, 40, 40, 40)
        self.got_button = QtWidgets.QPushButton(self.central_widget)
        self.got_button.setFont(QtGui.QFont('Roboto', 14))
        self.got_button.setMinimumSize(QtCore.QSize(112, 44))
        self.got_button.setMaximumSize(QtCore.QSize(112, 44))
        self.got_button.setStyleSheet("QPushButton {\n"
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
        self.got_button.clicked.connect(lambda: self.goto('first_new'))
        self.grid_layout.addWidget(self.got_button, 4, 2, 1, 1)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item, 2, 0, 1, 1)
        self.title = QtWidgets.QLabel(self.central_widget)
        self.title.setMinimumSize(QtCore.QSize(0, 90))
        self.title.setMaximumSize(QtCore.QSize(16777215, 90))
        self.title.setFont(QtGui.QFont('Roboto', 26))
        self.title.setStyleSheet("color: rgb(3, 67, 155);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.title, 0, 1, 1, 3)
        self.grid_layout.addItem(spacer_item, 4, 1, 1, 1)
        self.grid_layout.addItem(spacer_item, 4, 3, 1, 1)
        self.ghost = QtWidgets.QLabel(self.central_widget)
        self.ghost.setMinimumSize(QtCore.QSize(0, 20))
        self.ghost.setMaximumSize(QtCore.QSize(16777215, 20))
        self.ghost.setText("")
        self.grid_layout.addWidget(self.ghost, 3, 2, 1, 1)
        self.text = QtWidgets.QLabel(self.central_widget)
        self.text.setFont(QtGui.QFont('Roboto', 20))
        self.text.setStyleSheet("background-color: rgb(234, 222, 213);\n"
                                "color: rgb(96, 59, 0);\n"
                                "border-radius:22px;")
        self.text.setScaledContents(False)
        self.text.setMinimumWidth(1200)
        self.text.setMaximumWidth(1200)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.text, 2, 1, 1, 3)
        self.grid_layout.addItem(spacer_item, 2, 4, 1, 1)
        self.setCentralWidget(self.central_widget)

        self.retranslate_ui()

    def retranslate_ui(self):
        """
        Setting text to labels
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.got_button.setText(_translate("MainWindow", "GOT IT!"))
        self.title.setText(_translate("MainWindow", "Personal Values Test"))
        self.text.setText(
            _translate("MainWindow", "This test was developed with the aim of helping one to understand \n"
                                     "their personal values by W. R. Miller, J. C’de Baca, D. B. Matthews, \n"
                                     "P. L. Willbourne in University of New Mexico, 2001.\n"
                                     "\n"
                                     "This app is a digital implementation of the test, allowing to save \n"
                                     "one’s results and keep track of it.\n"
                                     "\n"
                                     "The given tests consists of 3 simple steps, each provided with the \n"
                                     "short instruction which can be found under the «?» button.\n"
                                     "\n"
                                     "If interested, you can always save your results after completing \n"
                                     "the test, or, alternatively, go to Menu - Results... to see the results \n"
                                     "of previous attempts and see whether you have changed."))
