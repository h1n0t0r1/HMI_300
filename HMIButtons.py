from PyQt5.QtWidgets import QPushButton, QCheckBox
from PyQt5.QtCore import Qt


##      ReSize function resize button depending by window width and height. Will fit on all resolution and can be used
##      to resize buttons when window is resized.
class Button(QPushButton):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setStyleSheet('font-size: 20px;')

class GreenButton(Button):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setStyleSheet('background-color: #85CD9A; font-size: 20px;')

class OrangeButton(Button):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setStyleSheet('background-color: #8F2A408; font-size: 20px;')

class ToggleButton(Button):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setCheckable(True)
        self.setStyleSheet('font-size: 20px;')
    ##      Can be on / off with setChecked(bool)   ##


class GreenTogleButton(ToggleButton):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setStyleSheet('background-color: #85CD9A; font-size: 20px;')

class InitButton(Button):
    def __init__(self, widget):
        super().__init__('INIT', widget)
        self.setStyleSheet('background-color: #85CD9A; font-size: 20px;')

class StartButton(GreenButton):
    def __init__(self, widget):
        super().__init__('START', widget)

class PauseButton(ToggleButton):
    def __init__(self, widget):
        super().__init__('PAUSE', widget)
        self.setStyleSheet('background-color: #F2A408; font-size: 20px;')

class TestModeButton(ToggleButton):
    def __init__(self, widget):
        super().__init__('Test Mode', widget)
        self.setStyleSheet('background-color: #F2A408; font-size: 20px;')

class ResetButton(Button):
    def __init__(self, widget):
        super().__init__('Reset', widget)
        self.setStyleSheet('background-color: #9F000F; font-size: 20px;')

class UnloadButton(ToggleButton):
    def __init__(self, widget):
        super().__init__('Unload', widget)
        self.setStyleSheet('background-color: #357EC7; font-size: 20px;')

class LockButton(Button):
    def __init__(self, widget):
        super().__init__('', widget)

    def setLocked(self):
        self.setStyleSheet('background-color: #96B0D2; font-size: 20px;')
        self.setText('Unlock')

    def setUnlocked(self):
        self.setStyleSheet('background-color: #F2A408; font-size: 20px;')
        self.setText('Lock')

class StepModeButton(GreenTogleButton):
    def __init__(self, widget):
        super().__init__('Step Mode', widget)

class InitStationButton(GreenButton):
    def __init__(self, widget):
        super().__init__('Init Station', widget)

class ScrapItemButton(GreenButton):
    def __init__(self, widget):
        super().__init__('Scrap', widget)

class UnscrapItemButton(GreenButton):
    def __init__(self, widget):
        super().__init__('Unscrap', widget)

class IndexerCWButton(GreenButton):
    def __init__(self, widget):
        super().__init__('Indexer CW', widget)

class IndexerCCWButton(GreenButton):
    def __init__(self, widget):
        super().__init__('Indexer CCW', widget)

class BlueButton(Button):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setStyleSheet('background-color: #96B0D2; font-size: 20px')

class CheckBox(QCheckBox):
    def __init__(self, name, widget):
        super().__init__(name, widget)
        self.setStyleSheet('background-color: #96B0D2; border-width: 3px; border-color: #9C9C9C; border-style: outset;')
        ##      Can be on / off with setChecked(bool)   ##

