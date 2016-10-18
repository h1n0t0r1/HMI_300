from StationWindow import StationWindow
from DIO import DI, DO

class Station5(StationWindow):
    def __init__(self):
        super().__init__()

        ##      Inputs       ##
        self.step_button = DI('Step Button', self.box)
        self.cycle_button = DI('Cycle Button', self.box)
        self.drive_busy = DI('Drive Busy', self.box)
        self.drive_area = DI('Drive Area', self.box)
        self.drive_seton = DI('Drive SETON', self.box)
        self.drive_inposition = DI('Drive in Position', self.box)
        self.drive_svre = DI('Drive SVRE', self.box)
        self.drive_noalarm = DI('Drive no Alarm', self.box)

        self.input_collection = (
            self.step_button,
            self.cycle_button,
            self.drive_busy,
            self.drive_area,
            self.drive_seton,
            self.drive_inposition,
            self.drive_svre,
            self.drive_noalarm
        )

        ##      Outputs     ##
        self.start_scan = DO('Start Scan', self.box)
        self.reset_scan = DO('Reset Scan', self.box)
        self.drive_in_0 = DO('Position Bit 0', self.box)
        self.drive_in_1 = DO('Position Bit 1', self.box)
        self.drive_in_5 = DO('Position Bit 5', self.box)
        self.drive_setup = DO('Drive Setup', self.box)
        self.drive_reset = DO('Drive Reset', self.box)
        self.drive_svon = DO('Drive Servo On', self.box)

        self.output_collection = (
            self.start_scan,
            self.reset_scan,
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

