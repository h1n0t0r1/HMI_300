from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap


class EngMode(QLabel):
    text = ''
    def __init__(self, widget):
        super().__init__('', widget)
        self.setStyleSheet('background-color: #F2A408; font-size: 20px; border: 3px outset #9C9C9C;')
        self.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.blink)
        self.setLanguage(0)
        self.blinked = False

    #Engineering Mode
    def setLanguage(self, idx):
        if idx == 0:
            EngMode.text = 'Инженерен Режим'
        elif idx == 1:
            EngMode.text = 'Engineering Mode'

    def blink(self):
        self.setText('') if self.blinked else self.setText(EngMode.text)
        self.blinked = not self.blinked

    def setOn(self):
        self.show()
        self.timer.start(1000)

    def setOff(self):
        self.hide()
        self.timer.stop()

class PLCState(QLabel):
    def __init__(self, widget):
        super().__init__(widget)
        self.setStyleSheet('background-color: #BFCDDB; font-size: 20px; border: 3px outset #9C9C9C;')
        self.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

    def setState(self, state, lang):
        if lang == 0:
            if state == 0:
                self.setText('Машината не Работи')
            elif state == 1:
                self.setText('Машината се Инциализира')
            elif state == 2:
                self.setText('Машината е в Готовност')
            elif state == 3:
                self.setText('Машината е в Работен Режим')
            elif state == 4:
                self.setText('Машината е в Пауза')
        elif lang == 1:
            if state == 0:
                self.setText('The Machine is Idle')
            elif state == 1:
                self.setText('The Machine is Initializing')
            elif state == 2:
                self.setText('The Machine is Ready')
            elif state == 3:
                self.setText('The Machine Works')
            elif state == 4:
                self.setText('The Machine is Paused')
            elif state == 5:
                self.setText('The Machine is Halted')


class MachineError(QLabel):
    def __init__(self, widget):
        super().__init__(widget)
        self.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.setStyleSheet('background-color: #BFCDDB; font-size: 16px; border: 3px outset #9C9C9C;')

class GoldenSample(QLabel):
    def __init__(self, widget):
        super().__init__(widget)
        self.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.setStyleSheet('background-color: #F2A408; font-size: 16px; border: 3px outset #9C9C9C;')

class ClickableLabel(QLabel):
    clicked = pyqtSignal()
    def __init__(self,name, widget):
        super().__init__(name, widget)
    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()

class LanguageIcon(ClickableLabel):
    #clicked = pyqtSignal()
    def __init__(self, widget,  name=''):
        super().__init__(name, widget)
        self.bg = QPixmap('img\\bg.png')
        self.gb = QPixmap('img\\gb.png')
        self.setPixmap(self.gb)
        self.lang = 0   # 0 == BG; 1 == EN

    def change(self):
        if self.lang == 0:
            self.setPixmap(self.bg)
            self.lang = 1
        elif self.lang == 1:
            self.setPixmap(self.gb)
            self.lang = 0



