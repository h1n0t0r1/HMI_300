from StationWindow import StationWindow
from DIO import DI, DO

class Station7(StationWindow):
    def __init__(self):
        super().__init__()

        ##       Inputs     ##
        self.i_part_present = DI('Part Present', self.box)
        self.i_part_aligned = DI('Part Aligned', self.box)
        self.i_at_pos_A0 = DI('At A0 Position', self.box)
        self.i_at_pos_A1 = DI('At A1 Position', self.box)
        self.i_at_pos_A2 = DI('At A2 Position', self.box)
        self.i_at_pos_A3 = DI('At A3 Position', self.box)
        self.i_robot_part_present = DI('Robot Part Present', self.box)
        self.i_robot_picked = DI('Robot Part Picked', self.box)

        self.input_collection = (
            self.i_part_present,
            self.i_part_aligned,
            self.i_at_pos_A0,
            self.i_at_pos_A1,
            self.i_at_pos_A2,
            self.i_at_pos_A3,
            self.i_robot_part_present,
            self.i_robot_picked
        )

        ##      Outputs     ##
        self.o_robot_pick = DO('Robot Pick Part', self.box)
        self.o_robot_spare = DO('Robot Spare Part', self.box)

        self.output_collection = (
            self.o_robot_pick,
            self.o_robot_spare
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

