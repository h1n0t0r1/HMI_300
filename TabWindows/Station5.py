from StationWindow import StationWindow
from DIO import DI, DO

class Station5(StationWindow):
    def __init__(self):
        super().__init__()

        ##      Inputs       ##
        self.i_step_button = DI('Step Button', self.box)
        self.i_cycle_button = DI('Cycle Button', self.box)
        self.i_drive_busy = DI('Drive Busy', self.box)
        self.i_drive_area = DI('Drive Area', self.box)
        self.i_drive_seton = DI('Drive SETON', self.box)
        self.i_drive_inposition = DI('Drive in Position', self.box)
        self.i_drive_svre = DI('Drive SVRE', self.box)
        self.i_drive_noalarm = DI('Drive no Alarm', self.box)

        self.input_collection = (
            self.i_step_button,
            self.i_cycle_button,
            self.i_drive_busy,
            self.i_drive_area,
            self.i_drive_seton,
            self.i_drive_inposition,
            self.i_drive_svre,
            self.i_drive_noalarm
        )

        ##      Outputs     ##
        self.o_start_scan = DO('Start Scan', self.box)
        self.o_reset_scan = DO('Reset Scan', self.box)
        self.o_drive_in_0 = DO('Position Bit 0', self.box)
        self.o_drive_in_1 = DO('Position Bit 1', self.box)
        self.o_drive_in_5 = DO('Position Bit 5', self.box)
        self.o_drive_setup = DO('Drive Setup', self.box)
        self.o_drive_reset = DO('Drive Reset', self.box)
        self.o_drive_svon = DO('Drive Servo On', self.box)

        self.output_collection = (
            self.o_start_scan,
            self.o_reset_scan,
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

        for item in self.input_collection:
            item.resize(dio_width, dio_height)
            item.move(x_pos, y_pos)
            y_pos += dio_height

        x_pos = width * StationWindow.output_col_1_x_pos
        y_pos = height * StationWindow.i_o_y_pos

        for item in self.output_collection:
            item.resize(dio_width, dio_height)
            item.move(x_pos, y_pos)
            y_pos += dio_height

