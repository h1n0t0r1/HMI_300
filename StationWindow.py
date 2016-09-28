from PyQt5.QtWidgets import QLabel
from SimpleWindow import SimpleWindow
from PyQt5.QtWidgets import QFrame
from HMIButtons import *

class StationWindow(SimpleWindow):
    def __init__(self):
        super().__init__()

        self.input_label = QLabel('Inputs', self.box)
        self.input_label.setStyleSheet('background-color: #C8DBFE; font-size: 30px; color: #696969')

        self.output_label = QLabel('Outputs', self.box)
        self.output_label.setStyleSheet('background-color: #C8DBFE; font-size: 30px; color: #696969')

        self.line = QFrame(self.box)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setStyleSheet('background-color: #C8DBFE')

        ###     Test Mode Button    ###
        self.test_btn = TestModeButton(self)
        self.test_btn.setStyleSheet('background-color: #85CD9A; font-size: 20px;')

        ###     Step Mode Button    ###
        self.step_btn = StepModeButton(self)

        ###     Init Station Button ###
        self.init_station_btn = InitStationButton(self)

        ###     Scrap Button    ###
        self.scrap_btn = ScrapItemButton(self)

        ###     Unscrap Button  ###
        self.unscrap_btn = UnscrapItemButton(self)

        ###     Indexer CW Button   ###
        self.indexercw_btn = IndexerCWButton(self)

        ###     Indexer CCW Button  ###
        self.indexerccw_btn = IndexerCCWButton(self)

    def fitToScreen(self, width, height):
        super().fitToScreen(width, height)

        _width = width * 0.11
        _height = height * 0.064
        left_col_x = width * 0.74   # X position of the left column of buttons
        right_col_x = width * 0.859 # X position of the right column of the buttons

        self.input_label.resize(width * 0.1, height * 0.1)
        self.input_label.move(width * 0.15, height * 0.005)

        self.output_label.resize(width * 0.1, height * 0.1)
        self.output_label.move(width * 0.51, height * 0.005)

        self.line.resize(width * 0.01, height * 0.65)
        self.line.move(width * 0.355, height * 0.05)

        self.test_btn.resize(_width, _height)
        self.test_btn.move(left_col_x, height * 0.142)

        self.step_btn.resize(_width, _height)
        self.step_btn.move(right_col_x, height * 0.142)

        self.init_station_btn.resize(_width, _height)
        self.init_station_btn.move(left_col_x, height * 0.22)

        self.scrap_btn.resize(_width, _height)
        self.scrap_btn.move(left_col_x, height * 0.298)

        self.unscrap_btn.resize(_width, _height)
        self.unscrap_btn.move(right_col_x, height * 0.298)

        self.indexercw_btn.resize(_width, _height)
        self.indexercw_btn.move(left_col_x, height * 0.376)

        self.indexerccw_btn.resize(_width, _height)
        self.indexerccw_btn.move(right_col_x, height * 0.376)