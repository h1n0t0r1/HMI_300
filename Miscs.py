from PyQt5.QtWidgets import QLabel, QDesktopWidget
from PyQt5 import QtCore


class EngMode(QLabel):
    def __init__(self, widget):
        super().__init__('', widget)
        self.setStyleSheet('background-color: #F2A408; font-size: 20px; border: 3px outset #9C9C9C;')
        self.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.blink)
        self.blinked = False

    def blink(self):
        self.setText('') if self.blinked else self.setText('Engineering Mode')
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

    def setState(self, state):
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
