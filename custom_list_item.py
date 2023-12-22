from typing import Union

import PySide6
from PySide6 import QtCore, QtGui, QtWidgets


class CustomListModel(QtCore.QAbstractListModel):
    def __init__(self, data=None):
        super().__init__()
        self.data = data or []

    def rowCount(self, parent=None):
        return len(self.data)

    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex],
             role: int)-> None:
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            return self.data[index.row()]


class CustomDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, painter, option, index):
        # Here you can define how to display your items. You can draw text, icons, etc.
        pass

    def sizeHint(self, option, index):
        # Here you can define the size of your items.
        pass


c
