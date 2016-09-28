from PyQt5.QtWidgets import QTabWidget, QMainWindow

class Settings(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #C0C0C0;')

        self.settings_tab = QTabWidget(self)
        self.settings_tab.showMaximized()
        self.settings_tab.move(0, 0)

    def fitToScreen(self, width, height):
        self.settings_tab.resize(width, height)

