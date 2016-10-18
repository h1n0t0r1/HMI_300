from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow, QGroupBox
from Miscs import LanguageIcon

class SimpleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.move(100, 100)
        self.setStyleSheet('background-color: #C0C0C0;')
        self.logo = QPixmap('img\\logo.png')
        self.logo_label = QLabel('', self)
        self.logo_label.setScaledContents(True)
        self.logo_label.setPixmap(self.logo)
        self.logo_label.resize(140, 100)
        self.language = LanguageIcon(self)
        self.box = QGroupBox(self)
        self.box.setStyleSheet('QGroupBox{background-color: #C8DBFE; border-width: 3px; border-color: #9C9C9C;\
                                border-style: outset;}')

    def fitToScreen(self, width, height):
        self.resize(width, height)
        self.logo_label.resize(width * 0.1, height * 0.11)
        self.logo_label.move(width * 0.01, height * 0.02)
        self.box.resize(width * 0.703, height * 0.761)
        self.box.move(width * 0.007, height * 0.142)
        self.language.resize(width * 0.033, height * 0.037)
        self.language.move(width * 0.937, height * 0.01)