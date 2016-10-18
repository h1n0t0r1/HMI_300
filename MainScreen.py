from SimpleWindow import SimpleWindow
from HMIButtons import *
from Miscs import EngMode, PLCState, MachineError, GoldenSample

class MainScreen(SimpleWindow):
    def __init__(self):
        super().__init__()

        ##      Engineering Mode Alert  ###
        self.eng_mode = EngMode(self)
        self.eng_mode.setOn()

        ###     Init Button     ###
        self.init_button = InitButton(self)
        ###     Start Button    ###
        self.start_button = StartButton(self)

        ###     Pause Button    ###
        self.pause_button = PauseButton(self)

        ###     Test Mode Button    ###
        self.test_mode_button = TestModeButton(self)

        ###     Reset Button    ###
        self.reset_button = ResetButton(self)

        ###     Unload Button   ###
        self.unload_button = UnloadButton(self)

        ###     PLC State   ###
        self.plc_state = PLCState(self)

        ###     Lock Button     ###
        self.lock_button = LockButton(self)

        ###     Machine Errors  ###
        self.err_msg = MachineError(self)

        ###     Golden Sample Bar   ###
        self.gs_msg = GoldenSample(self)

    def fitToScreen(self, width, height):
        super().fitToScreen(width, height)

        _width = width * 0.11
        _height = height * 0.064
        left_col_x = width * 0.74   # X position of the left column of buttons
        right_col_x = width * 0.859 # X position of the right column of the buttons

        self.eng_mode.resize(width * 0.229, height * 0.08)
        self.eng_mode.move(left_col_x, height * 0.05)

        self.init_button.resize(_width, _height)
        self.init_button.move(left_col_x, height * 0.142)

        self.start_button.resize(_width, _height)
        self.start_button.move(right_col_x, height * 0.142)

        self.pause_button.resize(_width, _height)
        self.pause_button.move(left_col_x, height * 0.22)

        self.test_mode_button.resize(_width, _height)
        self.test_mode_button.move(right_col_x, height * 0.22)

        self.reset_button.resize(_width, _height)
        self.reset_button.move(left_col_x, height * 0.298)

        self.unload_button.resize(_width, _height)
        self.unload_button.move(right_col_x, height * 0.298)

        self.plc_state.resize(width * 0.229, height * 0.092)
        self.plc_state.move(left_col_x, height * 0.376)

        self.lock_button.resize(width * 0.22, height * 0.079)
        self.lock_button.move(left_col_x, height * 0.48)

        self.err_msg.resize(width * 0.229, height * 0.196)
        self.err_msg.move(left_col_x, height * 0.575)

        self.gs_msg.resize(width * 0.229, height * 0.118)
        self.gs_msg.move(left_col_x, height * 0.785)

    def setLanguage(self):
        self.language.change()
        self.eng_mode.setLanguage(self.language.lang)
        self.init_button.setLanguage(self.language.lang)
        self.start_button.setLanguage(self.language.lang)
        self.pause_button.setLanguage(self.language.lang)
        self.test_mode_button.setLanguage(self.language.lang)
        self.unload_button.setLanguage(self.language.lang)
        self.lock_button.setLanguage(self.language.lang)