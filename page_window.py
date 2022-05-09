from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore


class PageWindow(QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)
