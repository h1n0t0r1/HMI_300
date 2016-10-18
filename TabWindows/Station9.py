from StationWindow import StationWindow
from DIO import DI, DO

class Station9(StationWindow):
    def __init__(self):
        super().__init__()

        self.step_button = DI('Step Button', self.box)
        self.cycle_button = DI('Cycle Button', self.box)
        self.top_cylinder_up = DI('Top Cylinder Up', self.box)
        self.top_cylinder_down = DI('Top Cylinder Down', self.box)
        self.contacts_out = DI('Contacts Out', self.box)
        self.contacts_in = DI('Contacts In', self.box)

        ##      Inputs      ##
        self.input_collection = (
            self.step_button,
            self.cycle_button,
            self.top_cylinder_up,
            self.top_cylinder_down,
            self.contacts_out,
            self.contacts_in
        )

        ##      Outputs     ##
        self.go_up = DO('Go Up', self.box)
        self.go_down = DO('Go Down', self.box)
        self.go_in = DO('Go In', self.box)

        self.output_collection = (
            self.go_up,
            self.go_down,
            self.go_in
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

