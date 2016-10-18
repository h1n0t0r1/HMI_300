from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
from functions import percentage

class Station():
    def __init__(self, widget, width = 100, height = 20, pos_x = 10, pos_y = 10):

        self.name = QLabel('', widget)

        self.barcode = QLabel('', widget)

        self.error = QLabel('', widget)

        self.station_status = QLabel('', widget)

        self.item_status = QLabel('', widget)

        self.station_skip = QLabel('', widget)

        self.collection = (
            self.name,
            self.barcode,
            self.error,
            self.station_status,
            self.item_status,
            self.station_skip
        )



        self.setStyle()

    def setResize(self, x, y):
        self.name.resize(percentage(16, x), y)
        self.barcode.resize(percentage(19, x), y)
        self.error.resize(percentage(45, x), y)
        self.station_status.resize(percentage(8, x), y)
        self.item_status.resize(percentage(8, x), y)
        self.station_skip.resize(percentage(12, x), y)
        self.setPosition(self.name.x(), self.name.y())


    def setPosition(self, x, y):
        self.name.move(x, y)
        pos_x = self.name.x() + self.name.frameGeometry().width()
        self.barcode.move(pos_x, y)
        pos_x = self.barcode.x() + self.barcode.frameGeometry().width()
        self.error.move(pos_x, y)
        pos_x = self.error.x() + self.error.frameGeometry().width()
        self.station_status.move(pos_x, y)
        pos_x = self.station_status.x() + self.station_status.frameGeometry().width()
        self.item_status.move(pos_x, y)
        pos_x = self.item_status.x() + self.item_status.frameGeometry().width()
        self.station_skip.move(pos_x, y)

    def setStyle(self):

        for item in self.collection:
            item.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            item.setStyleSheet('background-color: #bfcddb; border: 3px outset grey;')

    def setName(self, name):
        self.name.setText(name)

    def setBarcode(self, barcode):
        self.barcode.setText(barcode)

    def setError(self, error):
        self.error.setText(error)

    def getError(self):
        return self.error.text()

    def setReady(self, bool):
        if bool == True:
            self.station_status.setText('Ready')
            self.station_status.setStyleSheet('background-color: #4366FF; border: 3px outset grey;')
        elif bool == False:
            self.station_status.setText('')
            self.station_status.setStyleSheet('background-color: #bfcddb; border: 3px outset grey;')

    def setItemOk(self):
        self.item_status.setText('OK')
        self.item_status.setStyleSheet('background-color: #00B200; border: 3px outset grey;')

    def setItemFail(self):
        self.item_status.setText('Fail')
        self.item_status.setStyleSheet('background-color: #D40000; border: 3px outset grey;')

    def setStationSkip(self, status):
        self.station_skip.setText(status)

    def setAsTitle(self):
        self.name.setText('Station')
        self.barcode.setText('Barcode')
        self.error.setText('Error')
        self.station_status.setText('Ready')
        self.item_status.setText('OK/Fail')
        self.station_skip.setText('Status')

        for item in self.collection:
            item.setStyleSheet('font-weight: bold; background-color: #bfcddb; border: 3px outset grey;')




