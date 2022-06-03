import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyleFactory

from PersonalValuesPackage.src.database import AppDataBase
from PersonalValuesPackage.src.first_page import FirstPage
from PersonalValuesPackage.src.instruction_page import InstructionPage
from PersonalValuesPackage.src.page_window import PageWindow
from PersonalValuesPackage.src.saves_page import SavesPage
from PersonalValuesPackage.src.start_page import StartPage


class Main(QtWidgets.QMainWindow):
    """
    Class with the main page of the application where all pages change
    """

    def __init__(self, parent=None):
        """
        Initializing the class:

        :param parent: class-parent
        """
        super().__init__(parent)
        self.setWindowTitle("Personal Values Test")
        self.db = AppDataBase()
        self.setWindowIcon(QtGui.QIcon('icons/logo.png'))
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.menu_bar = QtWidgets.QMenuBar(self)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 863, 20))
        font = QtGui.QFont("Roboto", 8)
        self.menu_bar.setFont(font)
        self.menu_bar.setStyleSheet("background-color: rgb(191, 225, 235);")
        self.menu_menu = QtWidgets.QMenu(self.menu_bar)
        self.menu_menu.setFont(font)
        self.setMenuBar(self.menu_bar)
        self.action_results = QtWidgets.QAction(self)
        self.action_results.setFont(font)
        self.action_results.triggered.connect(self.goto_saves)
        self.action_test = QtWidgets.QAction(self)
        self.action_test.setFont(font)
        self.action_test.triggered.connect(lambda: self.goto('start'))
        self.menu_menu.addAction(self.action_test)
        self.menu_menu.addAction(self.action_results)
        self.menu_bar.addAction(self.menu_menu.menuAction())
        self.retranslate_ui()

        self.m_pages = {}
        self.register(StartPage(self), "start")
        self.register(FirstPage(self), "first_new")
        self.register(InstructionPage(self), "instruction")

        self.showMaximized()
        self.goto("start")

    def goto_saves(self):
        """
        Moving to the page with saves:

        :return: None
        """
        self.register(SavesPage(self), "saves_new")
        self.goto("saves_new")

    def register(self, widget, name):
        """
        Registration the pages to move:

        :param widget: class of page
        :param name: tag of page

        :return: None
        """
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    def retranslate_ui(self):
        """
        Setting text to labels:

        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.menu_menu.setTitle(_translate("MainWindow", "Menu"))
        self.action_results.setText(_translate("MainWindow", "Results"))
        self.action_test.setText(_translate("MainWindow", "Test"))

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        """
        Moving to another page:

        :param name: tag of page

        :return: None
        """
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":
    """
    Initializing the application
    """
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    app.setStyleSheet('''
        QWidget {
            font: "Roboto";
            background-color: rgb(231, 242, 248);
            color: rgb(0, 0, 0);
        }
    ''')
    w = Main()
    w.show()
    sys.exit(app.exec())
