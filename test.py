import sys

from MScreen import MScreen
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QTabWidget, QMainWindow

from TabWindows.Station1 import Station1
from Tags import tag
from functions import checkBit


class Program(QMainWindow):
    #opc = OPC()


    def __init__(self):
        super().__init__()
        #   Setup Window    #
        self.tab = QTabWidget(self)
        self.tab.showMaximized()
        self.tab.move(0, 0)

        self.main = MScreen()
        self.tab.addTab(self.main, 'Main')
        self.statusBar().showMessage('Ready')


        self.st1 = Station1()
        self.tab.addTab(self.st1, 'Station 1')

        self.main.eng_mode.setOn()
        self.main.plc_state.setState(5)
        self.main.lock_button.setLocked()
        self.main.err_msg.setText('Unable to connect to PLC')
        self.main.gs_msg.setText('Golden Sample Procedure')

        self.resizeEvent = self.onResize

        self.showMaximized()
        self.main.start_button.ReSize(self.width(), self.height())
        self.show()

    def onResize(self, event):
        self.main.fitToScreen(self.width(), self.height())
        self.st1.fitToScreen(self.width(), self.height())
        self.tab.resize(self.width(), self.height())
    ##      End of Window Setup     ##

    ##      OPC and OPC Variables SETUP ##

        # Declare variables read from OPC #
        self.s1_barcode = tag()
        self.s1_err_code = tag()
        self.s1_status = tag()

        self.s2_barcode = tag()
        self.s2_err_code = tag()
        self.s2_status = tag()

        self.s3_barcode = tag()
        self.s3_err_code = tag()
        self.s3_status = tag()

        self.s4_barcode = tag()
        self.s4_err_code = tag()
        self.s4_status = tag()

        self.s5_barcode = tag()
        self.s5_err_code = tag()
        self.s5_status = tag()

        self.s6_barcode = tag()
        self.s6_err_code = tag()
        self.s6_status = tag()

        self.station_ready = tag()
        self.table_rotate = tag()
        self.inputs = tag()
        self.outputs = tag()


        #   Create tag group    #
        self.opc_group = (
            'PLC1.Application.PLC_PRG.st1.barcode',  # 0
            'PLC1.Application.PLC_PRG.st1.errorCode',  # 1
            'PLC1.Application.PLC_PRG.st1.status',  # 2
            'PLC1.Application.PLC_PRG.st2.barcode',  # 3
            'PLC1.Application.PLC_PRG.st2.errorCode',  # 4
            'PLC1.Application.PLC_PRG.st2.status',  # 5
            'PLC1.Application.PLC_PRG.st3.barcode',  # 6
            'PLC1.Application.PLC_PRG.st3.errorCode',  # 7
            'PLC1.Application.PLC_PRG.st3.status',  # 8
            'PLC1.Application.PLC_PRG.st4.barcode',  # 9
            'PLC1.Application.PLC_PRG.st4.errorCode',  # 10
            'PLC1.Application.PLC_PRG.st4.status',  # 11
            'PLC1.Application.PLC_PRG.st5.barcode',  # 12
            'PLC1.Application.PLC_PRG.st5.errorCode',  # 13
            'PLC1.Application.PLC_PRG.st5.status',  # 14
            'PLC1.Application.PLC_PRG.st6.barcode',  # 15
            'PLC1.Application.PLC_PRG.st6.errorCode',  # 16
            'PLC1.Application.PLC_PRG.st6.status',  # 17
            'PLC1.Application.PLC_PRG.stationready',  # 18
            'PLC1.Application.PLC_PRG.tableRotate',  # 19
            'PLC1.Application.PLC_PRG.inputs',  # 20
            'PLC1.Application.PLC_PRG.outputs'  # 21
        )
        #   Create collection of all OPC variables
        #   Later can for each this collection for fast manipulation
        self.var_colection = (
            self.s1_barcode,
            self.s1_err_code,
            self.s1_status,
            self.s2_barcode,
            self.s2_err_code,
            self.s2_status,
            self.s3_barcode,
            self.s3_err_code,
            self.s3_status,
            self.s4_barcode,
            self.s4_err_code,
            self.s4_status,
            self.s5_barcode,
            self.s5_err_code,
            self.s5_status,
            self.s6_barcode,
            self.s6_err_code,
            self.s6_status,
            self.station_ready,
            self.table_rotate,
            self.inputs,
            self.outputs
        )



        ###     Set Up OPC      ###
        '''try:
            Program.opc._connect('CoDeSys.OPC.DA')
        except OpenOPC.OPCError:
            self.statusBar().showMessage('Unable to connect to OPC Server')
        Program.opc._addGroup(self.opc_group, 'tags')
        '''


        ###     Set Up QTimer   ###
        timer = QTimer(self)
        timer.timeout.connect(self.logic)
        timer.start(0.2)



    def logic(self):
        #self.setData()   # DONE
        #self.setStationReady()  #DONE
        #self.setIO()    #DONE
        #self.rotate()   #DONE
        return

    def setIO(self):
        if self.inputs.isChanged:
            if checkBit(self.inputs.getValue(), 0):
                self.st1.connector_present.setActive()
            else:
                self.st1.connector_present.setInActive()

            if checkBit(self.inputs.getValue(), 1):
                self.st1.pcb_present.setActive()
            else:
                self.st1.pcb_present.setInActive()

            if checkBit(self.inputs.getValue(), 2):
                self.st1.connector_aligned.setActive()
            else:
                self.st1.connector_aligned.setInActive()

            if checkBit(self.inputs.getValue(), 3):
                self.st1.left_btn.setActive()
            else:
                self.st1.left_btn.setInActive()

            if checkBit(self.inputs.getValue(), 4):
                self.st1.right_btn.setActive()
            else:
                self.st1.right_btn.setInActive()

            if checkBit(self.inputs.getValue(), 5):
                self.st1.sensor_btn.setActive()
            else:
                self.st1.sensor_btn.setInActive()

            if checkBit(self.inputs.getValue(), 6):
                self.st1.di_7.setActive()
            else:
                self.st1.di_7.setInActive()

            if checkBit(self.inputs.getValue(), 7):
                self.st1.di_8.setActive()
            else:
                self.st1.di_8.setInActive()

        ##

        if self.outputs.isChanged:
            if checkBit(self.outputs.getValue(), 0):
                self.st1.left_indicator.setActive()
            else:
                self.st1.left_indicator.setInActive()

            if checkBit(self.outputs.getValue(), 1):
                self.st1.right_indicator.setActive()
            else:
                self.st1.right_indicator.setInActive()

            if checkBit(self.outputs.getValue(), 2):
                self.st1.do_3.setActive()
            else:
                self.st1.do_3.setInActive()

            if checkBit(self.outputs.getValue(), 3):
                self.st1.do_4.setActive()
            else:
                self.st1.do_4.setInActive()

            if checkBit(self.outputs.getValue(), 4):
                self.st1.do_5.setActive()
            else:
                self.st1.do_5.setInActive()

            if checkBit(self.outputs.getValue(), 5):
                self.st1.do_6.setActive()
            else:
                self.st1.do_6.setInActive()

            if checkBit(self.outputs.getValue(), 6):
                self.st1.do_7.setActive()
            else:
                self.st1.do_7.setInActive()

            if checkBit(self.outputs.getValue(), 7):
                self.st1.do_8.setActive()
            else:
                self.st1.do_8.setInActive()

    def setStationReady(self):
        if self.station_ready.isChanged:
            self.main.station_1.setReady(checkBit(self.station_ready.getValue(), 1))
            self.main.station_2.setReady(checkBit(self.station_ready.getValue(), 2))
            self.main.station_3.setReady(checkBit(self.station_ready.getValue(), 3))
            self.main.station_4.setReady(checkBit(self.station_ready.getValue(), 4))
            self.main.station_5.setReady(checkBit(self.station_ready.getValue(), 5))
            self.main.station_6.setReady(checkBit(self.station_ready.getValue(), 6))


    def getData(self, group):
        tags = Program.opc._readGroup(group)    #Return list of variables, readed from OPC in order
                                                #  writen in tag group
        self.s1_barcode.setValue(tags[0])
        self.s1_err_code.setValue(tags[1])
        self.s1_status.setValue(tags[2])

        self.s2_barcode.setValue(tags[3])
        self.s2_err_code.setValue(tags[4])
        self.s2_status.setValue(tags[5])

        self.s3_barcode.setValue(tags[6])
        self.s3_err_code.setValue(tags[7])
        self.s3_status.setValue(tags[8])

        self.s4_barcode.setValue(tags[9])
        self.s4_err_code.setValue(tags[10])
        self.s4_status.setValue(tags[11])

        self.s5_barcode.setValue(tags[12])
        self.s5_err_code.setValue(tags[13])
        self.s5_status.setValue(tags[14])

        self.s6_barcode.setValue(tags[15])
        self.s6_err_code.setValue(tags[16])
        self.s6_status.setValue(tags[17])

        self.station_ready.setValue(tags[18])
        self.table_rotate.setValue(tags[19])
        self.inputs.setValue(tags[20])
        self.outputs.setValue(tags[21])

        for var in self.var_colection:
            var.refresh()       # Refresh items to check for onChange


    def setData(self):
        if self.s1_barcode.isChanged:
            self.main.station_1.setBarcode(str(self.s1_barcode.getValue()))
        if self.s2_barcode.isChanged:
            self.main.station_2.setBarcode(str(self.s2_barcode.getValue()))
        if self.s3_barcode.isChanged:
            self.main.station_3.setBarcode(str(self.s3_barcode.getValue()))
        if self.s4_barcode.isChanged:
            self.main.station_4.setBarcode(str(self.s4_barcode.getValue()))
        if self.s5_barcode.isChanged:
            self.main.station_5.setBarcode(str(self.s5_barcode.getValue()))
        if self.s6_barcode.isChanged:
            self.main.station_6.setBarcode(str(self.s6_barcode.getValue()))

        if self.s1_status.isChanged:
            if self.s1_status.getValue() > 0:
                self.main.station_1.setItemFail()
            else:
                self.main.station_1.setItemOk()

            if self.s1_status.getValue() == 1:
                if checkBit(self.s1_err_code.getValue(), 0):
                    self.main.station_1.setError('Грешка при пинчек! Проверката на пиновете не е ОК')
                elif checkBit(self.s1_err_code.getValue(), 1):
                    self.main.station_1.setError('Грешка при пинчек! Проверката на пиновете от камерата не е ОК')
                elif checkBit(self.s1_err_code.getValue(), 2):
                    self.main.station_1.setError('Грешка при пинчек! Камерата е разпознала изделие което не съответства'
                                                 ' на произвежданите в момента.')
                elif checkBit(self.s1_err_code.getValue(), 3):
                    self.main.station_1.setError('Грешка при пинчек! Камерата не може да разпознае изделието.')
                elif checkBit(self.s1_err_code.getValue(), 4):
                    self.main.station_1.setError('Грешка при пинчек! Камерата не чете добре.')
                elif checkBit(self.s1_err_code.getValue(), 5):
                    self.main.station_1.setError('Изделието е бракувано от оператора на станция 1')
                elif checkBit(self.s1_err_code.getValue(), 6):
                    self.main.station_1.setError('Изделието е бракувано от машината на станция 1')
                elif checkBit(self.s1_err_code.getValue(), 7):
                    self.main.station_1.setError('Грешка при сглобяване! Няма сигнал от вакума на позиция Pick')
        if self.s2_status.isChanged:
            if self.s2_status.getValue() > 0:
                self.main.station_2.setItemFail()
            else:
                self.main.station_2.setItemOk()

            if self.s2_status.getValue() == 2:
                if checkBit(self.s2_err_code.getValue(), 0):
                    self.main.station_2.setError('Грешка при сглобяване! Няма сигнал от вакума на позиция Place.')
                elif checkBit(self.s2_err_code.getValue(), 1):
                    self.main.station_2.setError('Грешка при сглобяване! PCB Align Failed!')
                elif checkBit(self.s2_err_code.getValue(), 2):
                    self.main.station_2.setError('Изделието е бракувано от оператора на станция 2')
                elif checkBit(self.s2_err_code.getValue(), 3):
                    self.main.station_2.setError('Изделието е бракувано от машината на станция 3.')
                elif checkBit(self.s2_err_code.getValue(), 4):
                    self.main.station_2.setError('Грешка при пресфит! Preсsfit теста не е ОК')
                elif checkBit(self.s2_err_code.getValue(), 5):
                    self.main.station_2.setError('Грешка при пресфит! Pressfit Error.')
                elif checkBit(self.s2_err_code.getValue(), 6):
                    self.main.station_2.setError('Грешка четене на баркод станция 2! Баркодът не се чете')
                elif checkBit(self.s2_err_code.getValue(), 7):
                    self.main.station_2.setError('Грешка четене на баркод станция 2! Баркодът е с лошо качество')
        if self.s3_status.isChanged:
            if self.s3_status.getValue() > 0:
                self.main.station_3.setItemFail()
            else:
                self.main.station_3.setItemOk()

            if self.s3_status.getValue() == 3:
                if checkBit(self.s3_err_code.getValue(), 0):
                    self.main.station_3.setError(
                        'Грешка четене на баркод станция 3! Баркодът не съвпада с прочетения на станция 1.')
                elif checkBit(self.s3_err_code.getValue(), 1):
                    self.main.station_3.setError('Изделието е бракувано от оператора на станция 3')
                elif checkBit(self.s3_err_code.getValue(), 2):
                    self.main.station_3.setError('Грешка 3D сканиране! Пиновете не са ОК')
                elif checkBit(self.s3_err_code.getValue(), 3):
                    self.main.station_3.setError('Изделието е бракувано от машината на станция 3.')
                elif checkBit(self.s3_err_code.getValue(), 4):
                    self.main.station_3.setError('Грешка 3D сканиране! Лепилото не е ОК')
                elif checkBit(self.s3_err_code.getValue(), 5):
                    self.main.station_3.setError('Грешка 3D сканиране! Термо пастата не е ОК')
                elif checkBit(self.s3_err_code.getValue(), 6):
                    self.main.station_3.setError('Грешка 3D сканиране! Резултатите от скенера не се четат')
                elif checkBit(self.s3_err_code.getValue(), 7):
                    self.main.station_3.setError('Проба 1 не е ОК')
        if self.s4_status.isChanged:
            if self.s4_status.getValue() > 0:
                self.main.station_4.setItemFail()
            else:
                self.main.station_4.setItemOk()

            if self.s4_status.getValue() == 4:
                if checkBit(self.s4_err_code.getValue(), 0):
                    self.main.station_4.setError('Test Error 1 on Station 4.')
                elif checkBit(self.s4_err_code.getValue(), 1):
                    self.main.station_4.setError('Test Error 2 on Station 4')
                elif checkBit(self.s4_err_code.getValue(), 2):
                    self.main.station_4.setError('Test Error 3 on Station 4')
                elif checkBit(self.s4_err_code.getValue(), 3):
                    self.main.station_4.setError('Test Error 4 on Station 4.')
                elif checkBit(self.s4_err_code.getValue(), 4):
                    self.main.station_4.setError('Test Error 5 on Station 4')
                elif checkBit(self.s4_err_code.getValue(), 5):
                    self.main.station_4.setError('Test Error 6 on Station 4')
                elif checkBit(self.s4_err_code.getValue(), 6):
                    self.main.station_4.setError('Test Error 7 on Station 4')
                elif checkBit(self.s4_err_code.getValue(), 7):
                    self.main.station_4.setError('Test Error 8 on Station 4')
        if self.s5_status.isChanged:
            if self.s5_status.getValue() > 0:
                self.main.station_5.setItemFail()
            else:
                self.main.station_5.setItemOk()

            if self.s5_status.getValue() == 5:
                if checkBit(self.s5_err_code.getValue(), 0):
                    self.main.station_5.setError('Test Error 1 on Station 5.')
                elif checkBit(self.s5_err_code.getValue(), 1):
                    self.main.station_5.setError('Test Error 2 on Station 5')
                elif checkBit(self.s5_err_code.getValue(), 2):
                    self.main.station_5.setError('Test Error 3 on Station 5')
                elif checkBit(self.s5_err_code.getValue(), 3):
                    self.main.station_5.setError('Test Error 4 on Station 5.')
                elif checkBit(self.s5_err_code.getValue(), 4):
                    self.main.station_5.setError('Test Error 5 on Station 5')
                elif checkBit(self.s5_err_code.getValue(), 5):
                    self.main.station_5.setError('Test Error 6 on Station 5')
                elif checkBit(self.s5_err_code.getValue(), 6):
                    self.main.station_5.setError('Test Error 7 on Station 5')
                elif checkBit(self.s5_err_code.getValue(), 7):
                    self.main.station_5.setError('Test Error 8 on Station 5')
        if self.s6_status.isChanged:
            if self.s6_status.getValue() > 0:
                self.main.station_6.setItemFail()
            else:
                self.main.station_6.setItemOk()

            if self.s6_status.getValue() == 6:
                if checkBit(self.s6_err_code.getValue(), 0):
                    self.main.station_6.setError('Test Error 1 on Station 4.')
                elif checkBit(self.s6_err_code.getValue(), 1):
                    self.main.station_6.setError('Test Error 2 on Station 4')
                elif checkBit(self.s6_err_code.getValue(), 2):
                    self.main.station_6.setError('Test Error 3 on Station 4')
                elif checkBit(self.s6_err_code.getValue(), 3):
                    self.main.station_6.setError('Test Error 4 on Station 4.')
                elif checkBit(self.s6_err_code.getValue(), 4):
                    self.main.station_6.setError('Test Error 5 on Station 4')
                elif checkBit(self.s6_err_code.getValue(), 5):
                    self.main.station_6.setError('Test Error 6 on Station 4')
                elif checkBit(self.s6_err_code.getValue(), 6):
                    self.main.station_6.setError('Test Error 7 on Station 4')
                elif checkBit(self.s6_err_code.getValue(), 7):
                    self.main.station_6.setError('Test Error 8 on Station 4')


    def rotate(self):
        if self.table_rotate.isChanged:
            self.main.station_6.setError(self.main.station_5.getError())
            self.main.station_5.setError(self.main.station_4.getError())
            self.main.station_4.setError(self.main.station_3.getError())
            self.main.station_3.setError(self.main.station_2.getError())
            self.main.station_2.setError(self.main.station_1.getError())
            self.main.station_1.setError('')












if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    sys.exit(app.exec_())
