from StationWindow import StationWindow
from DIO import DI, DO

class Station10(StationWindow):
    def __init__(self):
        super().__init__()

        ##      Inputs      ##
        self.step_button = DI('Step Button', self.box)
        self.cycle_button = DI('Cycle Button', self.box)
        self.cover_up = DI('Cover Up', self.box)
        self.cover_down = DI('Cover Down', self.box)

        self.input_collection = (
            self.step_button,
            self.cycle_button,
            self.cover_up,
            self.cover_down
        )

        ##      Outputs     ##
        self.lower_cover = DO('Lower Cover', self.box)
        self.exhaust = DO('Exhaust', self.box)

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
        self.lower_cover.resize(dio_width, dio_height)
        self.lower_cover.move(x_pos, y_pos)
        '''for item in self.output_collection:
            item.resize(dio_width, dio_height)
            item.move(x_pos, y_pos)
            y_pos += dio_height
        '''

