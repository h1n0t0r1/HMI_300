from MainScreen import MainScreen
from Stations import  Station
from PyQt5.QtWidgets import QTextBrowser

class MainWindow(MainScreen):
    def __init__(self):
        super().__init__()

        self.station_title = Station(self.box, 200, 20, 10, 10)
        self.station_title.setAsTitle()

        self.station_1 = Station(self.box, 200, 20, 10, 10)

        self.station_2 = Station(self.box, 200, 20, 10, 10)

        self.station_3 = Station(self.box, 200, 20, 10, 10)

        self.station_4 = Station(self.box, 200, 20, 10, 10)

        self.station_5 = Station(self.box, 200, 20, 10, 10)

        self.station_6 = Station(self.box, 200, 20, 10, 10)

        self.station_7 = Station(self.box, 200, 20, 10, 10)

        self.station_8 = Station(self.box, 200, 20, 10, 10)

        self.station_9 = Station(self.box, 200, 20, 10, 10)

        self.station_10 = Station(self.box, 200, 20, 10, 10)

        self.station_11 = Station(self.box, 200, 20, 10, 10)


        self.stations = (
            self.station_title,
            self.station_1,
            self.station_2,
            self.station_3,
            self.station_4,
            self.station_5,
            self.station_6,
            self.station_7,
            self.station_8,
            self.station_9,
            self.station_10,
            self.station_11
        )


    def fitToScreen(self, width, height):
        super().fitToScreen(width, height)
        x_pos = width * 0.03
        y_pos = height * 0.05
        for station in self.stations:
            station.setResize(width * 0.6, height * 0.05)
            station.setPosition(x_pos, y_pos)
            y_pos += height * 0.05

    def setLanguage(self):
        super().setLanguage()
        if self.language.lang == 0:
            self.station_1.setName('Зареждане')
            self.station_2.setName('Проверка на Пинове')
            self.station_3.setName('Сглобяване')
            self.station_4.setName('Пресоване')
            self.station_5.setName('Сканиране на Пинове')
            self.station_6.setName('Разтоварване за Лак')
            self.station_7.setName('Зареждане от Лак')
            self.station_8.setName('Сканиране на Лак')
            self.station_9.setName('Функционален Тест')
            self.station_10.setName('Лазерно Маркиране')
            self.station_11.setName('Разтоварване')
        elif self.language.lang == 1:
            self.station_1.setName('Loading')
            self.station_2.setName('Pin Gauge')
            self.station_3.setName('Pick & Place')
            self.station_4.setName('Press Fit')
            self.station_5.setName('3D AOI Pins')
            self.station_6.setName('Unload for Potting')
            self.station_7.setName('Load from Potting')
            self.station_8.setName('3D AOI Potting')
            self.station_9.setName('FCT')
            self.station_10.setName('Laser Marking')
            self.station_11.setName('Unload')