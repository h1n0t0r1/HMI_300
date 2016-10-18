from StationWindow import StationWindow
from DIO import DI, DO

class Station3(StationWindow):
    def __init__(self):
        super().__init__()

        ##      Inputs      ##
        self.i_step_button = DI('Step Button', self.box)
        self.i_cycle_button = DI('Cycle Button', self.box)
        self.i_position_up = DI('Upper Position', self.box)
        self.i_position_down = DI('Down Position', self.box)
        self.i_pick_up = DI('Pick Up', self.box)
        self.i_pick_down = DI('Pick Down', self.box)
        self.i_center_up = DI('Center Up', self.box)
        self.i_center_down = DI('Center Down', self.box)
        self.i_align_open = DI('Aligner Opened', self.box)
        self.i_align_close = DI('Aligner Closed', self.box)
        self.i_vacuum_ok = DI('Vacuum OK', self.box)
        self.i_drive_busy = DI('Drive Busy', self.box)
        self.i_drive_area = DI('Drive Area', self.box)
        self.i_drive_seton = DI('Drive SETON', self.box)
        self.i_drive_inposition = DI('Drive in Position', self.box)
        self.i_drive_svre = DI('Drive SVRE', self.box)
        self.i_drive_noalarm = DI('Drive no Alarm', self.box)

        self.input_collection = (
            self.i_step_button,
            self.i_cycle_button,
            self.i_position_up,
            self.i_position_down,
            self.i_pick_up,
            self.i_pick_down,
            self.i_center_up,
            self.i_center_down,
            self.i_align_open,
            self.i_align_close,
            self.i_vacuum_ok,
            self.i_drive_busy,
            self.i_drive_area,
            self.i_drive_seton,
            self.i_drive_inposition,
            self.i_drive_svre,
            self.i_drive_noalarm
        )
        ##      Outputs     ##
        self.o_pick = DO('Pick', self.box)
        self.o_center = DO('Center', self.box)
        self.o_align = DO('Align', self.box)
        self.o_vacuum_on = DO('Vacuum ON', self.box)
        self.o_blow = DO('Blow', self.box)
        self.o_drive_in_0 = DO('Position Bit 0', self.box)
        self.o_drive_in_1 = DO('Position Bit 1', self.box)
        self.o_drive_in_5 = DO('Position Bit 5', self.box)
        self.o_drive_setup = DO('Drive Setup', self.box)
        self.o_drive_reset = DO('Drive Reset', self.box)
        self.o_drive_svon = DO('Drive Servo On', self.box)

        self.output_collection = (
            self.o_pick,
            self.o_center,
            self.o_align,
            self.o_vacuum_on,
            self.o_blow,
            self.o_drive_in_0,
            self.o_drive_in_1,
            self.o_drive_in_5,
            self.o_drive_setup,
            self.o_drive_reset,
            self.o_drive_svon
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

