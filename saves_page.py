from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt, QModelIndex
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QListWidgetItem, QListWidget

from database import AppDataBase
from page_window import PageWindow


class SavesPageNew(PageWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.db = self.parent.db
        self.setWindowTitle("Personal Values Test")
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setObjectName("centralwidget")
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setContentsMargins(40, 20, 40, 20)
        self.grid_layout.setObjectName("gridLayout")
        self.label_saves = QtWidgets.QLabel(self.central_widget)
        self.label_saves.setMargin(8)
        self.label_saves.setFont(QtGui.QFont('Roboto', 14))
        self.label_saves.setStyleSheet("background-color: rgb(237, 207, 159);\n"
                                       "color: rgb(96, 59, 0);")
        self.label_saves.setAlignment(QtCore.Qt.AlignCenter)
        self.label_saves.setObjectName("label_3")
        self.grid_layout.addWidget(self.label_saves, 0, 1, 2, 1)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item, 2, 0, 1, 1)
        self.label_bottom = QtWidgets.QLabel(self.central_widget)
        self.label_bottom.setMargin(5)
        self.label_bottom.setFont(QtGui.QFont('Roboto', 10))
        self.label_bottom.setStyleSheet("background-color: rgb(135, 198, 212);\n"
                                        "color: rgb(30, 72, 154);")
        self.label_bottom.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bottom.setObjectName("label")
        self.grid_layout.addWidget(self.label_bottom, 3, 3, 1, 1)
        self.results_list = QListWidget(self)
        self.results_list.setMinimumWidth(600)
        self.results_list.setStyleSheet("background-color: rgb(205, 224, 229);\n"
                                        "alternate-background-color: rgb(135, 198, 213);"
                                        "border : 0px;")
        self.results_list.setAlternatingRowColors(True)
        self.results_list.setObjectName("listView")
        self.grid_layout.addWidget(self.results_list, 2, 3, 1, 1)
        self.label_top = QtWidgets.QLabel(self.central_widget)
        self.label_top.setFont(QtGui.QFont('Roboto', 14))
        self.label_top.setStyleSheet("background-color: rgb(135, 198, 212);\n"
                                     "color: rgb(30, 72, 154);")
        self.label_top.setAlignment(QtCore.Qt.AlignCenter)
        self.label_top.setObjectName("label_2")
        self.grid_layout.addWidget(self.label_top, 0, 3, 2, 1)
        self.saves_list = ListView(self)
        self.saves_list.clicked.connect(self.print_results)
        self.saves_list.setFont(QtGui.QFont('Roboto', 12))
        self.saves_list.add_items(self.db)
        self.saves_list.setMinimumWidth(900)
        self.saves_list.setStyleSheet("background-color: rgb(243, 234, 227);\n"
                                      "alternate-background-color: rgb(225, 216, 209);"
                                      "border : 0px;"
                                      "color: rgb(96, 59, 0);"
                                      "selection-background-color: #389CD8;"
                                      "selection-color: rgb(252, 249, 240);")
        self.saves_list.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.saves_list.setAlternatingRowColors(True)
        self.saves_list.setObjectName("results")
        self.grid_layout.addWidget(self.saves_list, 2, 1, 2, 1)
        spacer_item1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_layout.addItem(spacer_item1, 2, 2, 1, 1)
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item2, 2, 4, 1, 1)
        self.setCentralWidget(self.central_widget)

        self.retranslate_ui()

    def print_results(self, index: QModelIndex):
        name = self.saves_list.model().data(index)
        date = self.saves_list.model().data(self.saves_list.model().index(index.row(), 1))
        df = self.db.get_save(name, date)
        self.results_list.clear()
        self.results_list.setEnabled(False)
        for index, row in df.iterrows():
            text = row['card_path'][row['card_path'].rfind('\\') + 1:-4]
            item = QListWidgetItem(str(text).upper())
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(QtGui.QFont('Roboto', 14))
            item.setForeground(QBrush(QColor('#1E489A')))
            item.setSizeHint(QSize(100, 88))
            self.results_list.addItem(item)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_saves.setText(_translate("MainWindow", "SAVES"))
        self.label_bottom.setText(_translate("MainWindow", "Choose a user to see their results"))
        self.label_top.setText(_translate("MainWindow", "TOP VALUES"))


class ListView(QtWidgets.QTreeView):
    def __init__(self, *args, **kwargs):
        super(ListView, self).__init__(*args, **kwargs)
        self.setModel(QtGui.QStandardItemModel(self))
        self.model().setColumnCount(2)
        self.setRootIsDecorated(False)
        self.setAllColumnsShowFocus(True)
        self.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.setHeaderHidden(True)
        self.header().setStretchLastSection(False)
        self.header().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.header().setSectionResizeMode(
            1, QtWidgets.QHeaderView.ResizeToContents)

    def add_items(self, db):
        saves = db.get_all_saver()
        for index, row in saves.iterrows():
            first = QtGui.QStandardItem(row['name'])
            first.setSizeHint(QSize(0, 50))
            second = QtGui.QStandardItem(row['date'])
            second.setTextAlignment(Qt.AlignCenter)
            self.model().appendRow([first, second])
