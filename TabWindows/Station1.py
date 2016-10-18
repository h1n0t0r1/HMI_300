from StationWindow import StationWindow
from DIO import DI, DO

class Station1(StationWindow):
    def __init__(self):
        super().__init__()

        ##      Inputs      ##
        self.i_connector_present = DI('Connector Present', self.box)
        self.i_pcb_present = DI('PCB Present', self.box)
        self.i_connector_aligned = DI('Connector Aligned', self.box)
        self.i_pcb_alligned = DI('PCB Aligned', self.box)
        self.i_left_btn = DI('Left Button', self.box)
        self.i_right_btn = DI('Right Button', self.box)
        self.i_sensor_btn = DI('Sensor Button', self.box)

        self.input_collection = (
            self.i_connector_present,
            self.i_pcb_present,
            self.i_connector_aligned,
            self.i_pcb_alligned,
            self.i_left_btn,
            self.i_right_btn,
            self.i_sensor_btn
        )
        ##      Outputs     ##
        self.o_left_indicator = DO('Left Button Lamp', self.box)
        self.o_right_indicator = DO('Right Button Lamp', self.box)

        self.output_collection = (
            self.o_left_indicator,
            self.o_right_indicator
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



