import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyleFactory

from first_page_new import FirstPageNew
from first_test_page import FirstPage
from page_window import PageWindow
from saves_page import SavesPage
from second_page_new import SecondPageNew
from start_page import StartPage

# нужно добавить окна с информацией
# нужно проверки на последнем этапе теста
# нужно проверки на ввод
# pyuic5 -x start.ui -o start_page.py
from third_page import ThirdPage


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

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
        self.action_results.triggered.connect(lambda: self.goto('saves'))
        self.menu_menu.addAction(self.action_results)
        self.menu_bar.addAction(self.menu_menu.menuAction())
        self.retranslate_ui()

        self.m_pages = {}
        self.register(FirstPage(self), "first")
        self.register(SavesPage(self), "saves")
        self.register(StartPage(self), "start")
        self.register(FirstPageNew(self), "first_new")

        self.showMaximized()
        self.goto("start")

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.menu_menu.setTitle(_translate("MainWindow", "Menu"))
        self.action_results.setText(_translate("MainWindow", "Results"))

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
    sys.exit(app.exec_())
