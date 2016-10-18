import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTabWidget, QMainWindow
import Settings
import StationsScreen

from TabWindows import MainWindow, Station1, Station2, Station3, Station4, Station5,Station6,\
                       Station7, Station8, Station9, Station10, Station11, EngineerMenu, GoldenSample

class Program(QMainWindow):
    def __init__(self):
        super().__init__()

        #   Setup Window    #
        self.tab = QTabWidget(self)
        self.tab.showMaximized()
        self.tab.move(0, 0)
        self.tab.tabBar().setStyleSheet('font-size: 10px')
        self.tab.currentChanged.connect(self.changeTabColor)

        self.main = MainWindow.MainWindow()
        self.tab.addTab(self.main, '   Main   ')

        self.stations_tab = StationsScreen.StationsScreen()


        self.station_1 = Station1.Station1()
        self.stations_tab.tab.addTab(self.station_1, '1. Loading')

        self.station_2 = Station2.Station2()
        self.stations_tab.tab.addTab(self.station_2, '2. Pin Gauge')

        self.station_3 = Station3.Station3()
        self.stations_tab.tab.addTab(self.station_3, '3. Pick & Place')

        self.station_4 = Station4.Station4()
        self.stations_tab.tab.addTab(self.station_4, '4. Press Fit')

        self.station_5 = Station5.Station5()
        self.stations_tab.tab.addTab(self.station_5, '5. 3D AOI Pins')

        self.station_6 = Station6.Station6()
        self.stations_tab.tab.addTab(self.station_6, '6. Dispenser Unloading')

        self.station_7 = Station7.Station7()
        self.stations_tab.tab.addTab(self.station_7, '7. Dispenser Loading')

        self.station_8 = Station8.Station8()
        self.stations_tab.tab.addTab(self.station_8, '8. 3D AOI Potting')

        self.station_9 = Station9.Station9()
        self.stations_tab.tab.addTab(self.station_9, '   9. FCT   ')

        self.station_10 = Station10.Station10()
        self.stations_tab.tab.addTab(self.station_10, '10. Laser Marking')

        self.station_11 = Station11.Station11()
        self.stations_tab.tab.addTab(self.station_11, '11. Unloading')
        ##

        self.tab.addTab(self.stations_tab, 'Stations')

        self.settings = Settings.Settings()
        self.tab.addTab(self.settings, 'Settings')

        self.eng_menu = EngineerMenu.EngineerMenu()
        self.settings.settings_tab.addTab(self.eng_menu, 'Engineering Menu')

        #self.golden_sample = GoldenSample.GoldenSample()
        #self.settings.settings_tab.addTab(self.golden_sample, 'Golden Sample')

        #       Change Language Button Setup
        self.main.language.clicked.connect(lambda: self.changeLanguage())
        self.station_1.language.clicked.connect(lambda: self.changeLanguage())
        self.station_2.language.clicked.connect(lambda: self.changeLanguage())
        self.station_3.language.clicked.connect(lambda: self.changeLanguage())
        self.station_4.language.clicked.connect(lambda: self.changeLanguage())
        self.station_5.language.clicked.connect(lambda: self.changeLanguage())
        self.station_6.language.clicked.connect(lambda: self.changeLanguage())
        self.station_7.language.clicked.connect(lambda: self.changeLanguage())
        self.station_8.language.clicked.connect(lambda: self.changeLanguage())
        self.station_9.language.clicked.connect(lambda: self.changeLanguage())
        self.station_10.language.clicked.connect(lambda: self.changeLanguage())
        self.station_11.language.clicked.connect(lambda: self.changeLanguage())
        ##          Tests Only
        self.main.start_button.clicked.connect(lambda: self.tab.setCurrentIndex(2))
        ##
        self.changeLanguage()
        self.resizeEvent = self.onResize
        self.showMaximized()
        self.show()

    def changeLanguage(self):
        self.main.setLanguage()
        self.changeTabLabel()
        self.station_1.setLanguage()
        self.station_2.setLanguage()
        self.station_3.setLanguage()
        self.station_4.setLanguage()
        self.station_5.setLanguage()
        self.station_6.setLanguage()
        self.station_7.setLanguage()
        self.station_8.setLanguage()
        self.station_9.setLanguage()
        self.station_10.setLanguage()
        self.station_11.setLanguage()

    def changeTabColor(self, index):
        for i in range(0, self.tab.count()):
            self.tab.tabBar().setTabTextColor(i, Qt.black)
        self.tab.tabBar().setTabTextColor(index, Qt.darkGreen)

    def changeTabLabel(self):
        if self.main.language.lang == 0:
            self.tab.setTabText(0, 'Главно')
            self.tab.setTabText(1, 'Станции')
            self.tab.setTabText(2, 'Настройки')
            self.stations_tab.tab.setTabText(0, '1. Зареждане')
            self.stations_tab.tab.setTabText(1, '2. Проверка на Пиновете')
            self.stations_tab.tab.setTabText(2, '3. Сглобяване')
            self.stations_tab.tab.setTabText(3, '4. Пресоване')
            self.stations_tab.tab.setTabText(4, '5. Сканиране на Пинове')
            self.stations_tab.tab.setTabText(5, '6. Разтоварване Лак')
            self.stations_tab.tab.setTabText(6, '7. Зареждане Лак')
            self.stations_tab.tab.setTabText(7, '8. Сканиране Лак')
            self.stations_tab.tab.setTabText(8, '9. Функционален Тест')
            self.stations_tab.tab.setTabText(9, '10. Лазерно Маркиране')
            self.stations_tab.tab.setTabText(10, '11. Разтоварване')
            self.stations_tab.tab.setTabText(11, 'Настройки')
        elif self.main.language.lang == 1:
            self.tab.setTabText(0, 'Main')
            self.tab.setTabText(1, 'Stations')
            self.tab.setTabText(2, 'Settings')
            self.stations_tab.tab.setTabText(0, '1. Loading')
            self.stations_tab.tab.setTabText(1, '2. Pin Gauge')
            self.stations_tab.tab.setTabText(2, '3. Pick & Place')
            self.stations_tab.tab.setTabText(3, '4. Press Fit')
            self.stations_tab.tab.setTabText(4, '5. 3D AOI Pins')
            self.stations_tab.tab.setTabText(5, '6. Dispenser Unloading')
            self.stations_tab.tab.setTabText(6, '7. Dispenser Loading')
            self.stations_tab.tab.setTabText(7, '8. 3D AOI Potting')
            self.stations_tab.tab.setTabText(8, '9. FCT')
            self.stations_tab.tab.setTabText(9, '10. Laser Marking')
            self.stations_tab.tab.setTabText(10, '11. Unloading')
            self.stations_tab.tab.setTabText(11, '12. Settings')

    def onResize(self, event):
        self.tab.resize(self.width(), self.height())
        self.main.fitToScreen(self.width(), self.height())
        self.station_1.fitToScreen(self.width(), self.height())
        self.station_2.fitToScreen(self.width(), self.height())
        self.station_3.fitToScreen(self.width(), self.height())
        self.station_4.fitToScreen(self.width(), self.height())
        self.station_5.fitToScreen(self.width(), self.height())
        self.station_6.fitToScreen(self.width(), self.height())
        self.station_7.fitToScreen(self.width(), self.height())
        self.station_8.fitToScreen(self.width(), self.height())
        self.station_9.fitToScreen(self.width(), self.height())
        self.station_10.fitToScreen(self.width(), self.height())
        self.station_11.fitToScreen(self.width(), self.height())
        self.stations_tab.fitToScreen(self.width(), self.height())
        self.settings.fitToScreen(self.width(), self.height())
        self.eng_menu.fitToScreen(self.width(), self.height())
        #self.golden_sample.fitToScreen(self.width(), self.height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    sys.exit(app.exec_())
