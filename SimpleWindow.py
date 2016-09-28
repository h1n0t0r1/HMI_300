from PyQt5.QtWidgets import QMainWindow, QGroupBox

class SimpleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.move(100, 100)
        self.setStyleSheet('background-color: #C0C0C0;')
        self.box = QGroupBox(self)
        self.box.setStyleSheet('QGroupBox{background-color: #C8DBFE; border-width: 3px; border-color: #9C9C9C; border-style: outset;}')

    def fitToScreen(self, width, height):
        self.resize(width, height)
        self.box.resize(width * 0.703, height * 0.761)
        self.box.move(width * 0.007, height * 0.142)