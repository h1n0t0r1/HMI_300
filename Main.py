import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTabWidget, QMainWindow
import Settings
from TabWindows import MainWindow, Station1, Station2, Station3, Station4, Station5,Station6,\
                       Station7, Station8, Station9, Station10, Station11, EngineerMenu, GoldenSample

class Program(QMainWindow):
    def __init__(self):
        super().__init__()

        #   Setup Window    #
        self.tab = QTabWidget(self)
        self.tab.showMaximized()
        self.tab.move(0, 0)
        self.tab.currentChanged.connect(self.changeTabColor)

        self.main = MainWindow.MainWindow()
        self.tab.addTab(self.main, '   Main   ')

        self.station_1 = Station1.Station1()
        self.tab.addTab(self.station_1, '1. Loading')

        self.station_2 = Station2.Station2()
        self.tab.addTab(self.station_2, '2. Pin Gauge')

        self.station_3 = Station3.Station3()
        self.tab.addTab(self.station_3, '3. Pick & Place')

        self.station_4 = Station4.Station4()
        self.tab.addTab(self.station_4, '4. Press Fit')

        self.station_5 = Station5.Station5()
        self.tab.addTab(self.station_5, '5. 3D AOI Pins')

        self.station_6 = Station6.Station6()
        self.tab.addTab(self.station_6, '6. Dispenser Unloading')

        self.station_7 = Station7.Station7()
        self.tab.addTab(self.station_7, '7. Dispenser Loading')

        self.station_8 = Station8.Station8()
        self.tab.addTab(self.station_8, '8. 3D AOI Potting')

        self.station_9 = Station9.Station9()
        self.tab.addTab(self.station_9, '   9. FCT   ')

        self.station_10 = Station10.Station10()
        self.tab.addTab(self.station_10, '10. Laser Marking')

        self.station_11 = Station11.Station11()
        self.tab.addTab(self.station_11, '11. Unloading')

        ##
        self.settings = Settings.Settings()
        self.tab.addTab(self.settings, 'Settings')

        self.eng_menu = EngineerMenu.EngineerMenu()
        self.settings.settings_tab.addTab(self.eng_menu, 'Engineering Menu')

        #self.golden_sample = GoldenSample.GoldenSample()
        #self.settings.settings_tab.addTab(self.golden_sample, 'Golden Sample')
        ##

        self.resizeEvent = self.onResize
        self.showMaximized()
        self.show()

    def changeTabColor(self, index):
        for i in range(0, self.tab.count()):
            self.tab.tabBar().setTabTextColor(i, Qt.black)
        self.tab.tabBar().setTabTextColor(index, Qt.darkGreen)


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
        self.settings.fitToScreen(self.width(), self.height())
        self.eng_menu.fitToScreen(self.width(), self.height())
        self.golden_sample.fitToScreen(self.width(), self.height())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    sys.exit(app.exec_())
