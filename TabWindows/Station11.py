from StationWindow import StationWindow
from DIO import DI, DO

class Station11(StationWindow):
    def __init__(self):
        super().__init__()

        ##      Inputs      #
        self.i_step_button = DI('Step Button', self.box)
        self.i_cycle_button = DI('Cycle Button', self.box)
        self.i_pick_up = DI('Pick Up', self.box)
        self.i_pick_down = DI('Pick Down', self.box)
        self.i_gripper_open = DI('Gripper Open', self.box)
        self.i_gripper_closed = DI('Gripper Closed', self.box)
        self.i_ok_part_placed = DI('OK Part Placed', self.box)
        self.i_ok_part_at_output = DI('OK Part at Output', self.box)
        self.i_ok_part_unload_button = DI('OK Part Unload Button', self.box)
        self.i_nok_part_placed = DI('NOK Part Placed', self.box)
        self.i_nok_part_at_output = DI('NOK Part at Output', self.box)
        self.i_nok_part_button = DI('NOK Part Unload Button', self.box)
        self.i_drive_busy = DI('Drive Busy', self.box)
        self.i_drive_area = DI('Drive Area', self.box)
        self.i_drive_seton = DI('Drive SETON', self.box)
        self.i_drive_inposition = DI('Drive in Position', self.box)
        self.i_drive_svre = DI('Drive SVRE', self.box)
        self.i_drive_noalarm = DI('Drive no Alarm', self.box)

        self.input_collection = (
            self.i_step_button,
            self.i_cycle_button,
            self.i_pick_up,
            self.i_pick_down,
            self.i_gripper_open,
            self.i_gripper_closed,
            self.i_ok_part_placed,
            self.i_ok_part_at_output,
            self.i_ok_part_unload_button,
            self.i_nok_part_placed,
            self.i_nok_part_at_output,
            self.i_nok_part_button,
            self.i_drive_busy,
            self.i_drive_area,
            self.i_drive_seton,
            self.i_drive_inposition,
            self.i_drive_svre,
            self.i_drive_noalarm
        )

        self.o_pick_up_down = DO('Pick Up/Down', self.box)
        self.o_open_gripper = DO('Open Gripper', self.box)
        self.o_close_gripper = DO('Close Gripper', self.box)
        self.o_drive_in_0 = DO('Position Bit 0', self.box)
        self.o_drive_in_1 = DO('Position Bit 1', self.box)
        self.o_drive_in_5 = DO('Position Bit 5', self.box)
        self.o_drive_setup = DO('Drive Setup', self.box)
        self.o_drive_reset = DO('Drive Reset', self.box)
        self.o_drive_svon = DO('Drive Servo On', self.box)

        self.output_collection = (
            self.o_pick_up_down,
            self.o_open_gripper,
            self.o_close_gripper,
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

        for item in self.output_collection:
            item.resize(dio_width, dio_height)
            item.move(x_pos, y_pos)
            y_pos += dio_height

