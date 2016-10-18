from StationWindow import StationWindow
from DIO import DI, DO

class Station6(StationWindow):
    def __init__(self):
        super().__init__()

        ##      Inputs      ##
        self.position_empty = DI('Position Empty', self.box)
        self.transfered = DI('Transfered', self.box)

        self.input_collection = (
            self.position_empty,
            self.transfered
        )

        ##      Outputs     ##
        self.part_available = DO('Part Available', self.box)
        self.at_position_A0 = DO('At A0 Position', self.box)
        self.at_position_A1 = DO('At A1 Position', self.box)
        self.at_position_A2 = DO('At A2 Position', self.box)
        self.at_position_A3 = DO('At A3 Position', self.box)
        self.transfer = DO('Transfer', self.box)

        self.output_collection = (
            self.part_available,
            self.at_position_A0,
            self.at_position_A1,
            self.at_position_A2,
            self.at_position_A3,
            self.transfer
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

