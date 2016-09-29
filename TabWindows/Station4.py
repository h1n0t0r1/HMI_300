from StationWindow import StationWindow
from DIO import DI, DO

class Station4(StationWindow):
    def __init__(self):
        super().__init__()

        self.di_1 = DI('digital input 1', self.box)
        self.di_2 = DI('digital input 2', self.box)
        self.di_3 = DI('digital input 3', self.box)
        self.di_4 = DI('digital input 4', self.box)
        self.di_5 = DI('digital input 5', self.box)
        self.di_6 = DI('digital input 6', self.box)

        self.input_collection = (
            self.di_1,
            self.di_2,
            self.di_3,
            self.di_4,
            self.di_5,
            self.di_6
        )

        self.do_1 = DO('digital output 1', self.box)
        self.do_2 = DO('digital output 2', self.box)
        self.do_3 = DO('digital output 3', self.box)
        self.do_4 = DO('digital output 4', self.box)
        self.do_5 = DO('digital output 5', self.box)
        self.do_6 = DO('digital output 6', self.box)

        self.output_collection = (
            self.do_1,
            self.do_2,
            self.do_3,
            self.do_4,
            self.do_5,
            self.do_6
        )

    def fitToScreen(self, width, height):
        super().fitToScreen(width, height)
        dio_width = width * 0.1
        dio_height = height * 0.05
        x_pos = width * 0.02
        y_pos = height * 0.15
        for item in self.input_collection:
            item.resize(dio_width, dio_height)
            item.move(x_pos, y_pos)
            y_pos += dio_height

        x_pos = width * 0.382
        y_pos = height * 0.15
        for item in self.output_collection:
            item.resize(dio_width, dio_height)
            item.move(x_pos, y_pos)
            y_pos += dio_height

