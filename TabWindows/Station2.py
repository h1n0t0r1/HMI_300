from StationWindow import StationWindow
from DIO import DI, DO

class Station2(StationWindow):
    def __init__(self):
        super().__init__()

        ##      Inputs       ##
        self.step_button = DI('Step Button', self.box)
        self.cycle_button = DI('Cycle Button', self.box)
        self.gauge_up = DI('Gauge Up', self.box)
        self.gauge_down = DI('Gauge Down', self.box)
        self.gauge_result = DI('Gauge Result', self.box)

        self.input_collection = (
            self.step_button,
            self.cycle_button,
            self.gauge_up,
            self.gauge_down,
            self.gauge_result
        )

        ##       Outputs     ##
        self.lower_gauge = DO('Lower Gauge', self.box)


        self.output_collection = (
            self.lower_gauge
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

        self.lower_gauge.resize(dio_width, dio_height)
        self.lower_gauge.move(x_pos, y_pos)
        '''for item in self.output_collection:
            item.resize(dio_width, dio_height)
            item.move(x_pos, y_pos)
            y_pos += dio_height
        '''

