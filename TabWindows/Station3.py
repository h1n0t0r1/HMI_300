from StationWindow import StationWindow
from DIO import DI, DO

class Station3(StationWindow):
    def __init__(self):
        super().__init__()

        ##      Inputs      ##
        self.step_button = DI('Step Button', self.box)
        self.cycle_button = DI('Cycle Button', self.box)
        self.position_up = DI('Upper Position', self.box)
        self.position_down = DI('Down Position', self.box)
        self.pick_up = DI('Pick Up', self.box)
        self.pick_down = DI('Pick Down', self.box)
        self.center_up = DI('Center Up', self.box)
        self.center_down = DI('Center Down', self.box)
        self.align_open = DI('Aligner Opened', self.box)
        self.align_close = DI('Aligner Closed', self.box)
        self.vacuum_ok = DI('Vacuum OK', self.box)
        self.drive_busy = DI('Drive Busy', self.box)
        self.drive_area = DI('Drive Area', self.box)
        self.drive_seton = DI('Drive SETON', self.box)
        self.drive_inposition = DI('Drive in Position', self.box)
        self.drive_svre = DI('Drive SVRE', self.box)
        self.drive_noalarm = DI('Drive no Alarm', self.box)

        self.input_collection = (
            self.step_button,
            self.cycle_button,
            self.position_up,
            self.position_down,
            self.pick_up,
            self.pick_down,
            self.center_up,
            self.center_down,
            self.align_open,
            self.align_close,
            self.vacuum_ok,
            self.drive_busy,
            self.drive_area,
            self.drive_seton,
            self.drive_inposition,
            self.drive_svre,
            self.drive_noalarm
        )
        ##      Outputs     ##
        self.pick = DO('Pick', self.box)
        self.center = DO('Center', self.box)
        self.align = DO('Align', self.box)
        self.vacuum_on = DO('Vacuum ON', self.box)
        self.blow = DO('Blow', self.box)
        self.drive_in_0 = DO('Position Bit 0', self.box)
        self.drive_in_1 = DO('Position Bit 1', self.box)
        self.drive_in_5 = DO('Position Bit 5', self.box)
        self.drive_setup = DO('Drive Setup', self.box)
        self.drive_reset = DO('Drive Reset', self.box)
        self.drive_svon = DO('Drive Servo On', self.box)

        self.output_collection = (
            self.pick,
            self.center,
            self.align,
            self.vacuum_on,
            self.blow,
            self.drive_in_0,
            self.drive_in_1,
            self.drive_in_5,
            self.drive_setup,
            self.drive_reset,
            self.drive_svon
        )

    def fitToScreen(self, width, height):
        super().fitToScreen(width, height)
        dio_width = width * 0.1
        dio_height = height * 0.05
        x_pos = width * StationWindow.input_col_1_x_pos
        y_pos = height * StationWindow.i_o_y_pos

        for i, item in enumerate(self.input_collection):
            item.resize(dio_width, dio_height)
            item.move(x_pos, y_pos)
            y_pos += dio_height
            if i == 8:
                x_pos = width * StationWindow.input_col_2_x_pos
                y_pos = height * StationWindow.i_o_y_pos

        x_pos = width * StationWindow.output_col_1_x_pos
        y_pos = height * StationWindow.i_o_y_pos

        for i, item in enumerate(self.output_collection):
            item.resize(dio_width, dio_height)
            item.move(x_pos, y_pos)
            y_pos += dio_height
            if i == 5:
                x_pos = width * StationWindow.output_col_2_x_pos
                y_pos = height * StationWindow.i_o_y_pos

