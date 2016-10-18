from StationWindow import StationWindow
from DIO import DI, DO

class Station2(StationWindow):
    def __init__(self):
        super().__init__()

        ##      Inputs       ##
        self.i_step_button = DI('Step Button', self.box)
        self.i_cycle_button = DI('Cycle Button', self.box)
        self.i_gauge_up = DI('Gauge Up', self.box)
        self.i_gauge_down = DI('Gauge Down', self.box)
        self.i_gauge_result = DI('Gauge Result', self.box)

        self.input_collection = (
            self.i_step_button,
            self.i_cycle_button,
            self.i_gauge_up,
            self.i_gauge_down,
            self.i_gauge_result
        )

        ##       Outputs     ##
        self.o_lower_gauge = DO('Lower Gauge', self.box)


        self.output_collection = (
            self.o_lower_gauge
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
        self.o_lower_gauge.resize(dio_width, dio_height)
        self.o_lower_gauge.move(x_pos, y_pos)
        '''for item in self.output_collection:
            item.resize(dio_width, dio_height)
            item.move(x_pos, y_pos)
            y_pos += dio_height
        '''

