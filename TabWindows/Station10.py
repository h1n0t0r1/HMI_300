from StationWindow import StationWindow
from DIO import DI, DO

class Station10(StationWindow):
    def __init__(self):
        super().__init__()

        ##      Inputs      ##
        self.i_step_button = DI('Step Button', self.box)
        self.i_cycle_button = DI('Cycle Button', self.box)
        self.i_cover_up = DI('Cover Up', self.box)
        self.i_cover_down = DI('Cover Down', self.box)

        self.input_collection = (
            self.i_step_button,
            self.i_cycle_button,
            self.i_cover_up,
            self.i_cover_down
        )

        ##      Outputs     ##
        self.o_lower_cover = DO('Lower Cover', self.box)
        self.o_exhaust = DO('Exhaust', self.box)

        '''self.output_collection = (
            self.lower_cover
        )
        '''
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
        self.o_lower_cover.resize(dio_width, dio_height)
        self.o_lower_cover.move(x_pos, y_pos)
        '''for item in self.output_collection:
            item.resize(dio_width, dio_height)
            item.move(x_pos, y_pos)
            y_pos += dio_height
        '''

