from PyQt5.QtWidgets import QTabWidget, QMainWindow

class StationsScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #C0C0C0;')

        self.tab = QTabWidget(self)
        self.tab.showMaximized()
        self.tab.move(0, 0)

    def fitToScreen(self, width, height):
        self.tab.resize(width, height)