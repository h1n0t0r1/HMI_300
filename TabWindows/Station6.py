from StationWindow import StationWindow
from DIO import DI, DO

class Station6(StationWindow):
    def __init__(self):
        super().__init__()

        ##      Inputs      ##
        self.i_position_empty = DI('Position Empty', self.box)
        self.i_transferred = DI('Transfered', self.box)

        self.input_collection = (
            self.i_position_empty,
            self.i_transferred
        )

        ##      Outputs     ##
        self.o_part_available = DO('Part Available', self.box)
        self.o_at_position_A0 = DO('At A0 Position', self.box)
        self.o_at_position_A1 = DO('At A1 Position', self.box)
        self.o_at_position_A2 = DO('At A2 Position', self.box)
        self.o_at_position_A3 = DO('At A3 Position', self.box)
        self.o_transfer = DO('Transfer', self.box)

        self.output_collection = (
            self.o_part_available,
            self.o_at_position_A0,
            self.o_at_position_A1,
            self.o_at_position_A2,
            self.o_at_position_A3,
            self.o_transfer
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

