from PyQt5.QtWidgets import QLabel
from  PyQt5 import QtCore
class DI(QLabel):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setStyleSheet('background-color: #bfcddb; border: 3px outset grey;')
        self.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

    def setActive(self):
        self.setStyleSheet('background-color: #00CC00; border: 3px outset grey;')

    def setInActive(self):
        self.setStyleSheet('background-color: #bfcddb; border: 3px outset grey;')


class DO(DI):
    def __init__(self, name, widget):
        super().__init__(name, widget)

    def setActive(self):
        self.setStyleSheet('background-color: #FF0000; border: 3px outset grey;')