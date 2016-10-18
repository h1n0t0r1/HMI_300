from PyQt5.QtWidgets import QPushButton, QCheckBox, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

##      ReSize function resize button depending by window width and height. Will fit on all resolution and can be used
##      to resize buttons when window is resized.
from Miscs import ClickableLabel


class Button(QPushButton):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setStyleSheet('font-size: 20px;')

class GreenButton(Button):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setStyleSheet('background-color: #85CD9A;'
                           'font-size: 20px;')

class OrangeButton(Button):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setStyleSheet('background-color: #8F2A408;'
                           'font-size: 20px;')

class ToggleButton(Button):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setCheckable(True)
        self.setStyleSheet('font-size: 20px;')
    ##      Can be on / off with setChecked(bool)   ##


class GreenTogleButton(ToggleButton):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setStyleSheet('background-color: #85CD9A;'
                           'font-size: 20px;')

class InitButton(Button):
    def __init__(self, widget):
        super().__init__('INIT', widget)
        self.setStyleSheet('background-color: #85CD9A;'
                           'font-size: 20px;')
        self.setLanguage(0)

    def setLanguage(self, idx):
        if idx == 0:
            self.setText('Инициализирай')
            self.setStyleSheet('background-color: #85CD9A;'
                               'font-size: 12px;'
                               'font-weight: 500')
        elif idx == 1:
            self.setText('INIT')
            self.setStyleSheet('background-color: #85CD9A;'
                               'font-size: 20px;')
class StartButton(GreenButton):
    def __init__(self, widget):
        super().__init__('', widget)
        self.setLanguage(0)

    def setLanguage(self, idx):
        if idx == 0:
            self.setText('Старт')
        elif idx == 1:
            self.setText('START')

class PauseButton(ToggleButton):
    def __init__(self, widget):
        super().__init__('', widget)
        self.setStyleSheet('background-color: #F2A408;'
                           'font-size: 20px;')
        self.setLanguage(0)

    def setLanguage(self, idx):
        if idx == 0:
            self.setText('Пауза')
        elif idx == 1:
            self.setText('PAUSE')

class TestModeButton(ToggleButton):
    def __init__(self, widget):
        super().__init__('', widget)
        self.setStyleSheet('background-color: #F2A408;'
                           'font-size: 20px;'
                           'font-weight: 500')
        self.setLanguage(0)

    def setLanguage(self, idx):
        if idx == 0:
            self.setText('Тестови Режим')
            self.setStyleSheet('background-color: #F2A408;'
                               'font-size: 12px;'
                               'font-weight: 500')
        elif idx == 1:
            self.setText('Test Mode')
            self.setStyleSheet('background-color: #F2A408;'
                               'font-size: 20px;')

class ResetButton(Button):
    def __init__(self, widget):
        super().__init__('Reset', widget)
        self.setStyleSheet('background-color: #9F000F;'
                           'font-size: 20px;')





class UnloadButton(ToggleButton):
    def __init__(self, widget):
        super().__init__('', widget)
        self.setStyleSheet('background-color: #357EC7;'
                           'font-size: 20px;')
        self.setLanguage(0)

    def setLanguage(self, idx):
        if idx == 0:
            self.setText('Разтоварване')
            self.setStyleSheet('background-color: #357EC7;'
                               'font-size: 12px;'
                               'font-weight: 500')

        elif idx == 1:
            self.setText('Unload')
            self.setStyleSheet('background-color: #357EC7;'
                               'font-size: 20px;')

class LockButton(Button):
    lock_label = ''
    unlock_label = ''
    def __init__(self, widget):
        super().__init__('', widget)
        self.status = 0 # 0 == Unlock; 1 == Lock
        self.setLanguage(0)
    def setLocked(self):
        self.setStyleSheet('background-color: #96B0D2;'
                           'font-size: 20px;')
        self.setText(LockButton.unlock_label)
        self.status = 1

    def setUnlocked(self):
        self.setStyleSheet('background-color: #F2A408;'
                           'font-size: 20px;')
        self.setText(LockButton.lock_label)
        self.status = 0

    def setLanguage(self, idx):
        if idx == 0:
            LockButton.lock_label = 'Заключи'
            LockButton.unlock_label = 'Отключи'
        elif idx == 1:
            LockButton.lock_label = 'Lock'
            LockButton.unlock_label = 'Unlock'

        if self.status == 1:
            self.setLocked()
        elif self.status == 0:
            self.setUnlocked()

class StepModeButton(GreenTogleButton):
    def __init__(self, widget):
        super().__init__('', widget)
        self.setLanguage(0)

    def setLanguage(self, idx):
        if idx == 0:
            self.setText('Стъпков Режим')
            self.setStyleSheet('background-color: #85CD9A;'
                               'font-size: 12px;'
                               'font-weight: 500')

        elif idx == 1:
            self.setText('Step Mode')
            self.setStyleSheet('background-color: #85CD9A;'
                               'font-size: 20px;')

class InitStationButton(GreenButton):
    def __init__(self, widget):
        super().__init__('', widget)
        self.setLanguage(0)

    def setLanguage(self, idx):
        if idx == 0:
            self.setText('Инициализирай')
            self.setStyleSheet('background-color: #85CD9A;'
                               'font-size: 12px;'
                               'font-weight: 500')

        elif idx == 1:
            self.setText('Init Station')
            self.setStyleSheet('background-color: #85CD9A;'
                               'font-size: 20px;')

class ScrapItemButton(GreenButton):
    def __init__(self, widget):
        super().__init__('', widget)
        self.setLanguage(0)

    def setLanguage(self, idx):
        if idx == 0:
            self.setText('Бракувай')
            self.setStyleSheet('background-color: #85CD9A;'
                               'font-size: 12px;'
                               'font-weight: 700')

        elif idx == 1:
            self.setText('Scrap')
            self.setStyleSheet('background-color: #85CD9A;'
                               'font-size: 20px;')

class UnscrapItemButton(GreenButton):
    def __init__(self, widget):
        super().__init__('', widget)
        self.setLanguage(0)

    def setLanguage(self, idx):
        if idx == 0:
            self.setText('Годен')
            self.setStyleSheet('background-color: #85CD9A;'
                               'font-size: 12px;'
                               'font-weight: 700')

        elif idx == 1:
            self.setText('Unscrap')
            self.setStyleSheet('background-color: #85CD9A;'
                               'font-size: 20px;')

class IndexerCWButton(GreenButton):
    def __init__(self, widget):
        super().__init__('Indexer \u21bb', widget)
        self.setStyleSheet('background-color: #85CD9A;'
                           'font-size: 20px;')

class IndexerCCWButton(GreenButton):
    def __init__(self, widget):
        super().__init__('Indexer \u21ba', widget)

class BlueButton(Button):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setStyleSheet('background-color: #96B0D2;'
                           'font-size: 20px')

class CheckBox(QCheckBox):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setStyleSheet('background-color: #96B0D2;'
                           'border-width: 3px;'
                           'border-color: #9C9C9C;'
                           'border-style: outset;')
        ##      Can be on / off with setChecked(bool)   ##

