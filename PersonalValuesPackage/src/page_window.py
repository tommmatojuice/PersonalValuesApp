from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore


class PageWindow(QMainWindow):
    """
    Class describes the page of application
    """
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        """
        Moving to another page:

        :param name: tag of page

        :return: None
        """
        self.gotoSignal.emit(name)
