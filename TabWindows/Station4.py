from StationWindow import StationWindow
from DIO import DI, DO

class Station4(StationWindow):
    def __init__(self):
        super().__init__()

        ##      Inputs      ##
        self.step_button = DI('Step Button', self.box)
        self.cycle_button = DI('Cycle Button', self.box)
        self.pf_ok = DI('Press Fit OK', self.box)
        self.pf_nok = DI('Press Fit NOK', self.box)
        self.pf_ack = DI('Press Fit Acknowledge', self.box)
        self.pf_not_homed = DI('Press Fit Not Homed', self.box)
        self.pf_up = DI('Pres Fit Up', self.box)
        self.vacuum_ok = DI('Vacuum OK', self.box)
        self.pick_up = DI('Pick Up', self.box)
        self.pick_down = DI('Pick Down', self.box)
        self.drive_busy = DI('Drive Busy', self.box)
        self.drive_area = DI('Drive Area', self.box)
        self.drive_seton = DI('Drive SETON', self.box)
        self.drive_inposition = DI('Drive in Position', self.box)
        self.drive_svre = DI('Drive SVRE', self.box)
        self.drive_noalarm = DI('Drive no Alarm', self.box)

        self.input_collection = (
            self.step_button,
            self.cycle_button,
            self.pf_ok,
            self.pf_nok,
            self.pf_ack,
            self.pf_not_homed,
            self.pf_up,
            self.pick_up,
            self.pick_down,
            self.vacuum_ok,
            self.drive_busy,
            self.drive_area,
            self.drive_seton,
            self.drive_inposition,
            self.drive_svre,
            self.drive_noalarm
        )

        ##      Outputs     ##

        self.ps_start_ref = DO('Press Fit Start Ref', self.box)
        self.pf_start_cycle = DO('Press Fit Start Cycle', self.box)
        self.pick = DO('Pick', self.box)
        self.vacuum_on = DO('Vacuum ON', self.box)
        self.blow = DO('Blow', self.box)
        self.drive_in_0 = DO('Position Bit 0', self.box)
        self.drive_in_1 = DO('Position Bit 1', self.box)
        self.drive_in_5 = DO('Position Bit 5', self.box)
        self.drive_setup = DO('Drive Setup', self.box)
        self.drive_reset = DO('Drive Reset', self.box)
        self.drive_svon = DO('Drive Servo On', self.box)

        self.output_collection = (
            self.ps_start_ref,
            self.pf_start_cycle,
            self.pick,
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
            if i == 7:
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

