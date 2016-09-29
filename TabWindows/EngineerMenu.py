from EngineerScreen import EngineerScreen
from HMIButtons import *
from PyQt5 import QtCore


class EngineerMenu(EngineerScreen):
    def __init__(self):
        super().__init__()

        #       Skip Operation Setup    #
        self.skip_item_1 = CheckBox('Skip Item 1', self.skip_operation_box)
        self.skip_item_2 = CheckBox('Skip Item 2', self.skip_operation_box)
        self.skip_item_3 = CheckBox('Skip Item 3', self.skip_operation_box)
        self.skip_item_4 = CheckBox('Skip Item 4', self.skip_operation_box)
        self.skip_item_5 = CheckBox('Skip Item 5', self.skip_operation_box)
        self.skip_item_6 = CheckBox('Skip Item 6', self.skip_operation_box)
        self.skip_item_7 = CheckBox('Skip Item 7', self.skip_operation_box)
        self.skip_item_8 = CheckBox('Skip Item 8', self.skip_operation_box)
        self.skip_item_9 = CheckBox('Skip Item 9', self.skip_operation_box)
        self.skip_item_10 = CheckBox('Skip Item 10', self.skip_operation_box)
        self.skip_item_11 = CheckBox('Skip Item 11', self.skip_operation_box)
        self.skip_item_12 = CheckBox('Skip Item 12', self.skip_operation_box)
        self.skip_item_13 = CheckBox('Skip Item 13', self.skip_operation_box)
        self.skip_item_14 = CheckBox('Skip Item 14', self.skip_operation_box)
        self.skip_item_15 = CheckBox('Skip Item 15', self.skip_operation_box)

        self.skip_items_collecton = (
            self.skip_item_1,
            self.skip_item_2,
            self.skip_item_3,
            self.skip_item_4,
            self.skip_item_5,
            self.skip_item_6,
            self.skip_item_7,
            self.skip_item_8,
            self.skip_item_9,
            self.skip_item_10,
            self.skip_item_11,
            self.skip_item_12,
            self.skip_item_13,
            self.skip_item_14,
            self.skip_item_15
        )

        #       Special Settings Setup      #

        self.special_settings_1 = CheckBox('Setting 1', self.special_settings_box)
        self.special_settings_2 = CheckBox('Setting 2', self.special_settings_box)
        self.special_settings_3 = CheckBox('Setting 3', self.special_settings_box)
        self.special_settings_4 = CheckBox('Setting 4', self.special_settings_box)
        self.special_settings_5 = CheckBox('Setting 5', self.special_settings_box)

        self.special_settings_collection = (
            self.special_settings_1,
            self.special_settings_2,
            self.special_settings_3,
            self.special_settings_4,
            self.special_settings_5
        )

        #       Skip Station Setup      #

        self.skip_station_2 = CheckBox('Skip Station 2', self.skip_station_box)
        self.skip_station_3 = CheckBox('Skip Station 3', self.skip_station_box)
        self.skip_station_4 = CheckBox('Skip Station 4', self.skip_station_box)
        self.skip_station_5 = CheckBox('Skip Station 5', self.skip_station_box)
        self.skip_station_6 = CheckBox('Skip Station 6', self.skip_station_box)
        self.skip_station_7 = CheckBox('Skip Station 7', self.skip_station_box)
        self.skip_station_8 = CheckBox('Skip Station 8', self.skip_station_box)
        self.skip_station_9 = CheckBox('Skip Station 9', self.skip_station_box)
        self.skip_station_10 = CheckBox('Skip Station 10', self.skip_station_box)

        self.skip_station_collection = (
            self.skip_station_2,
            self.skip_station_3,
            self.skip_station_4,
            self.skip_station_5,
            self.skip_station_6,
            self.skip_station_7,
            self.skip_station_8,
            self.skip_station_9,
            self.skip_station_10
        )

    def fitToScreen(self, width, height):
        super().fitToScreen(width, height)
        _width = width * 0.15
        _height = height * 0.07
        horizontal_padding = width * 0.02
        vertical_padding = height * 0.022

        for i, item in enumerate(self.skip_items_collecton):
            item.resize(_width, _height)
            if i <= 4:
                item.move((horizontal_padding * (i + 1)) + _width * i , vertical_padding)
            elif i > 4 and i <= 9:
                item.move((horizontal_padding * (i - 4)) + _width * (i - 5), vertical_padding * 2 + _height)
            elif i > 9 and i <= 14:
                item.move((horizontal_padding * (i - 9)) + _width * (i - 10), vertical_padding * 3 + _height * 2)

        for i, item in enumerate(self.special_settings_collection):
            item.resize(_width, _height)
            item.move((horizontal_padding * (i + 1)) + _width * i, vertical_padding)

        for i, item in enumerate(self.skip_station_collection):
            item.resize(_width, _height)
            if i <= 4:
                item.move((horizontal_padding * (i + 1)) + _width * i , vertical_padding)
            elif i > 4 and i <= 9:
                item.move((horizontal_padding * (i - 4)) + _width * (i - 5), vertical_padding * 2 + _height)

        ##self.skip_item_1.resize(_width, _height)
        #self.skip_item_1.move(horizontal_padding, vertical_padding)
        #self.skip_item_6.move(horizontal_padding, vertical_padding * 2 + _height)
        #self.skip_item_11.move(horizontal_padding, vertical_padding * 3 + _height * 2)
