from PyQt5 import QtCore, QtGui, QtWidgets

from PersonalValuesPackage.src.page_window import PageWindow


class StartPage(PageWindow):
    """
    Class with the start page of the app
    """
    def __init__(self, parent=None):
        """
        Initializing the page
        :param parent: class-parent
        """
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Personal Values Test")
        self.central_widget = QtWidgets.QWidget()
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacer_item)

        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setFont(QtGui.QFont('Roboto', 28))
        self.label.setStyleSheet("color: rgb(3, 67, 155);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setMargin(50)
        self.vertical_layout.addWidget(self.label)
        self.horizontal_layout = QtWidgets.QHBoxLayout()

        self.start_button = QtWidgets.QPushButton(self.central_widget)
        self.start_button.setMinimumSize(QtCore.QSize(112, 44))
        self.start_button.setMaximumSize(QtCore.QSize(112, 44))
        self.start_button.setFont(QtGui.QFont('Roboto', 14))
        self.start_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.start_button.setStyleSheet('''QPushButton
                                        {
                                        background-color: rgb(240, 177, 72);
                                        color: rgb(255, 255, 255);
                                        border-radius : 22;
                                        border-bottom : 2px solid rgb(227, 166, 67);
                                        border-right: 2px solid rgb(227, 166, 67);
                                        }
                                        QPushButton::hover
                                        {
                                        background-color: rgb(227, 166, 67);
                                        color: rgb(255, 255, 255);
                                        border-radius : 22;
                                        }''')
        self.start_button.clicked.connect(lambda: self.goto('instruction'))

        self.horizontal_layout.addWidget(self.start_button)
        self.vertical_layout.addLayout(self.horizontal_layout)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacer_item)
        self.setCentralWidget(self.central_widget)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        """
        Setting text to labels
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Personal Values Test"))
        self.start_button.setText(_translate("MainWindow", "START"))
