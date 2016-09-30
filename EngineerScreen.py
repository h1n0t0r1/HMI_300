from PyQt5.QtWidgets import QMainWindow, QGroupBox

class EngineerScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet('background-color: #C8DBFE;')

        self.skip_operation_box = QGroupBox(self)
        self.special_settings_box = QGroupBox(self)
        self.skip_station_box = QGroupBox(self)

        collection = (
            self.skip_operation_box,
            self.special_settings_box,
            self.skip_station_box
        )

        for box in collection:
            box.setStyleSheet('background-color: #C0C0C0')

    def fitToScreen(self, width, height):
        _width = width * 0.95
        box_x_pos = width * 0.02
        self.skip_operation_box.resize(_width, height * 0.3)
        self.skip_operation_box.move(box_x_pos, height * 0.05)

        self.special_settings_box.resize(_width, height * 0.2)
        self.special_settings_box.move(box_x_pos, height * 0.4)

        self.skip_station_box.resize(_width, height * 0.25)
        self.skip_station_box.move(box_x_pos, height * 0.65)

