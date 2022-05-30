import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyleFactory

from database import AppDataBase
from first_page import FirstPageNew
from fourth_page import FourthPage
from instruction_page import InstructionPage
from page_window import PageWindow
from saves_page import SavesPage
from saves_page_new import SavesPageNew
from start_page import StartPage
from datetime import datetime

# заголовик
# icon
# вопрос о выходе
# изменить время
# изменить бд
# pyuic5 -x start.ui -o start_page.py


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = AppDataBase()
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")[:-3])
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.menu_bar = QtWidgets.QMenuBar(self)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 863, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
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
        self.register(FirstPageNew(self), "first_new")
        self.register(InstructionPage(self), "instruction")

        self.showMaximized()
        self.goto("start")

    def goto_saves(self):
        self.register(SavesPageNew(self), "saves_new")
        self.goto("saves_new")

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.menu_menu.setTitle(_translate("MainWindow", "Menu"))
        self.action_results.setText(_translate("MainWindow", "Results"))
        self.action_test.setText(_translate("MainWindow", "Test"))

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":
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
    # sys.exit(app.exec_())
    sys.exit(app.exec())
