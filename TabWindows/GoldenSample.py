from SimpleWindow import SimpleWindow, QGroupBox
from PyQt5.QtWidgets import QComboBox, QLabel, QInputDialog
from PyQt5 import QtCore
from HMIButtons import BlueButton, CheckBox
from rwIni import RWIni
import functions

class GoldenSample(SimpleWindow):
    def __init__(self):
        super().__init__()

        self.ini = RWIni('C:\\Users\\Cvetan\\test.ini')

        self.gs_check_1 = 2
        self.gs_check_2 = 4
        self.gs_check_3 = 6
        self.gs_check_4 = 8
        self.gs_check_5 = 10
        self.gs_check_6 = 12
        self.gs_check_7 = 14
        self.gs_check_8 = 16

        self.gs_pass_1 = 2
        self.gs_pass_2 = 4
        self.gs_pass_3 = 8
        self.gs_pass_4 = 16
        self.gs_pass_5 = 32
        self.gs_pass_6 = 64
        self.gs_pass_7 = 128
        self.gs_pass_8 = 255

        ##      Samples Count       ##

        self.gs_count_box = QGroupBox(self.box)

        self.gs_count_box.setStyleSheet('background-color: #96B0D2; border-width: 3px; border-color: #9C9C9C;\
                                         border-style: outset;')

        self.gs_count_label = QLabel('Samples', self.gs_count_box)
        self.gs_count_label.setStyleSheet('background-color: transparent; border-style: none; font-size: 24px;')

        self.gs_count = QComboBox(self.gs_count_box)
        self.gs_count.setStyleSheet('background-color: #C8DBFE; border-width: 3px; border-color: #9C9C9C;\
                                     border-style: inset;')
        self.gs_count.setEditable(True)
        self.gs_count.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.gs_count.addItems(['1', '2', '3', '4', '5', '6', '7', '8'])
        self.gs_count.setCurrentIndex(3)
        self.gs_count.currentIndexChanged.connect(self.setSampleCount)

        ##      Sample Number       ##

        self.sample_number_box = QGroupBox(self.box)
        self.sample_number_box.setStyleSheet('background-color: #96B0D2; border-width: 3px; border-color: #9C9C9C;\
                                         border-style: outset;')

        self.sample_number_label = QLabel('Sample', self.sample_number_box)
        self.sample_number_label.setStyleSheet('background-color: transparent; border-style: none; font-size: 24px;')

        self.sample_number = QComboBox(self.sample_number_box)
        self.sample_number.setStyleSheet('background-color: #C8DBFE; border-width: 3px; border-color: #9C9C9C;\
                                          border-style: inset;')
        self.sample_number.setEditable(True)
        self.sample_number.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.sample_number.currentIndexChanged.connect(self.setSampleLabel)
        self.sample_number.currentIndexChanged.connect(lambda: self.updateBox(self.sample_number.currentIndex() + 1))
        ##      Sample Number Label     ##

        self.sample_label = QLabel('', self.box)
        self.sample_label.setStyleSheet('background-color: transparent; border-style: none; font-size: 32px;')

        ##      Setup Check & Pass Buttons

        self.pass_1 = CheckBox('Pass 1', self.box)
        self.pass_2 = CheckBox('Pass 2', self.box)
        self.pass_3 = CheckBox('Pass 3', self.box)
        self.pass_4 = CheckBox('Pass 4', self.box)
        self.pass_5 = CheckBox('Pass 5', self.box)
        self.pass_6 = CheckBox('Pass 6', self.box)
        self.pass_7 = CheckBox('Pass 7', self.box)
        self.pass_8 = CheckBox('Pass 8', self.box)

        self.pass_collection = (
            self.pass_1,
            self.pass_2,
            self.pass_3,
            self.pass_4,
            self.pass_5,
            self.pass_6,
            self.pass_7,
            self.pass_8
        )

        self.check_1 = CheckBox('Check 1', self.box)
        self.check_2 = CheckBox('Check 2', self.box)
        self.check_3 = CheckBox('Check 3', self.box)
        self.check_4 = CheckBox('Check 4', self.box)
        self.check_5 = CheckBox('Check 5', self.box)
        self.check_6 = CheckBox('Check 6', self.box)
        self.check_7 = CheckBox('Check 7', self.box)
        self.check_8 = CheckBox('Check 8', self.box)

        self.check_collection = (
            self.check_1,
            self.check_2,
            self.check_3,
            self.check_4,
            self.check_5,
            self.check_6,
            self.check_7,
            self.check_8
        )

        ##      Setup Side Buttons      ##

        self.save_label = QLabel('Save Template', self)
        self.save_label.setStyleSheet('font-size: 32px')

        self.save_tmp1_btn = BlueButton('empty', self)
        self.save_tmp1_btn.clicked.connect(lambda: self.savePressed(1))

        self.save_tmp2_btn = BlueButton('empty', self)
        self.save_tmp2_btn.clicked.connect(lambda: self.savePressed(2))

        self.save_tmp3_btn = BlueButton('empty', self)
        self.save_tmp3_btn.clicked.connect(lambda: self.savePressed(3))

        self.save_tmp4_btn = BlueButton('empty', self)
        self.save_tmp4_btn.clicked.connect(lambda: self.savePressed(4))

        self.save_tmp5_btn = BlueButton('empty', self)
        self.save_tmp5_btn.clicked.connect(lambda: self.savePressed(5))

        self.save_tmp6_btn = BlueButton('empty', self)
        self.save_tmp6_btn.clicked.connect(lambda: self.savePressed(6))

        self.save_tmp7_btn = BlueButton('empty', self)
        self.save_tmp7_btn.clicked.connect(lambda: self.savePressed(7))

        self.save_tmp8_btn = BlueButton('empty', self)
        self.save_tmp8_btn.clicked.connect(lambda: self.savePressed(8))

        self.save_tmp9_btn = BlueButton('empty', self)
        self.save_tmp9_btn.clicked.connect(lambda: self.savePressed(9))

        self.save_tmp10_btn = BlueButton('empty', self)
        self.save_tmp10_btn.clicked.connect(lambda: self.savePressed(10))

        self.save_btn_collection =(
            self.save_tmp1_btn,
            self.save_tmp2_btn,
            self.save_tmp3_btn,
            self.save_tmp4_btn,
            self.save_tmp5_btn,
            self.save_tmp6_btn,
            self.save_tmp7_btn,
            self.save_tmp8_btn,
            self.save_tmp9_btn,
            self.save_tmp10_btn
        )

        self.load_label = QLabel('Load Template', self)
        self.load_label.setStyleSheet('font-size: 32px')

        self.load_tmp1_btn = BlueButton('empty', self)
        self.load_tmp1_btn.clicked.connect(lambda: self.loadPressed(1))

        self.load_tmp2_btn = BlueButton('empty', self)
        self.load_tmp2_btn.clicked.connect(lambda: self.loadPressed(2))

        self.load_tmp3_btn = BlueButton('empty', self)
        self.load_tmp3_btn.clicked.connect(lambda: self.loadPressed(3))

        self.load_tmp4_btn = BlueButton('empty', self)
        self.load_tmp4_btn.clicked.connect(lambda: self.loadPressed(4))

        self.load_tmp5_btn = BlueButton('empty', self)
        self.load_tmp5_btn.clicked.connect(lambda: self.loadPressed(5))

        self.load_tmp6_btn = BlueButton('empty', self)
        self.load_tmp6_btn.clicked.connect(lambda: self.loadPressed(6))

        self.load_tmp7_btn = BlueButton('empty', self)
        self.load_tmp7_btn.clicked.connect(lambda: self.loadPressed(7))

        self.load_tmp8_btn = BlueButton('empty', self)
        self.load_tmp8_btn.clicked.connect(lambda: self.loadPressed(8))

        self.load_tmp9_btn = BlueButton('empty', self)
        self.load_tmp9_btn.clicked.connect(lambda: self.loadPressed(9))

        self.load_tmp10_btn = BlueButton('empty', self)
        self.load_tmp10_btn.clicked.connect(lambda: self.loadPressed(10))

        self.load_btn_collection = (
            self.load_tmp1_btn,
            self.load_tmp2_btn,
            self.load_tmp3_btn,
            self.load_tmp4_btn,
            self.load_tmp5_btn,
            self.load_tmp6_btn,
            self.load_tmp7_btn,
            self.load_tmp8_btn,
            self.load_tmp9_btn,
            self.load_tmp10_btn
        )

        self.setSampleCount()
        self.readIni()

        ##      Functions       ##

    def fitToScreen(self, width, height):
        super().fitToScreen(width, height)
        self.gs_count_box.resize(width * 0.1, height * 0.1)
        self.gs_count_box.move(width * 0.2, height * 0.08)
        self.gs_count_label.move(width * 0.028, height * 0.01)
        self.gs_count.resize(width * 0.06, height * 0.04)
        self.gs_count.move(width * 0.02, height * 0.05)

        self.sample_number_box.resize(width * 0.1, height * 0.1)
        self.sample_number_box.move(width * 0.45, height * 0.08)
        self.sample_number_label.move(width * 0.025, height * 0.01)
        self.sample_number.resize(width * 0.06, height * 0.04)
        self.sample_number.move(width * 0.02, height * 0.05)

        self.sample_label.move(width * 0.3, height * 0.21)

        pos_x = width * 0.15
        pos_y = height * 0.29
        box_width = width * 0.1
        box_height = height * 0.07
        for i, box in enumerate(self.pass_collection):
            box.resize(box_width, box_height)
            box.move(pos_x, pos_y)
            pos_x += width * 0.12
            if i == 3:
                pos_x = width * 0.15
                pos_y = height * 0.51
        pos_x = width * 0.15
        pos_y = height * 0.4
        for i , box in enumerate(self.check_collection):
            box.resize(box_width, box_height)
            box.move(pos_x, pos_y)
            pos_x += width * 0.12
            if i == 3:
                pos_x = width * 0.15
                pos_y = height * 0.62

        self.save_label.resize(width * 0.12, height * 0.05)
        self.save_label.move(width * 0.8, height * 0.15)

        pos_x = width * 0.725
        pos_y = height * 0.21
        for i, button in enumerate(self.save_btn_collection):
            button.resize(width * 0.12, height * 0.05)
            button.move(pos_x, pos_y)
            if (i + 1) % 2 == 0:
                pos_x = width * 0.725
                pos_y += height * 0.06
            else:
                pos_x = width * 0.86

        self.load_label.resize(width * 0.12, height * 0.05)
        self.load_label.move(width * 0.8, height * 0.52)

        pos_x = width * 0.725
        pos_y = height * 0.59
        for i, button in enumerate(self.load_btn_collection):
            button.resize(width * 0.12, height * 0.05)
            button.move(pos_x, pos_y)
            if (i + 1) % 2 == 0:
                pos_x = width * 0.725
                pos_y += height * 0.06
            else:
                pos_x = width * 0.86

    def setSampleCount(self):
        gs_count = int(self.gs_count.currentText())
        self.sample_number.clear()
        for i in range(1, gs_count + 1):
            self.sample_number.addItem(str(i))

    def setSampleLabel(self):
        self.sample_label.setText('Golden Sample {}'.format(self.sample_number.currentText()))

    def readIni(self):
        for i, (save_btn, load_btn) in enumerate(zip(self.save_btn_collection, self.load_btn_collection)):
            label = self.ini.readIni('Golden Sample', 'Template ' + str(i + 1))
            save_btn.setText(label)
            load_btn.setText(label)

    def savePressed(self, idx):
        text, ok = QInputDialog.getText(self, 'Save Template', 'Enter template name')
        if ok:
            key = 'Template ' + str(idx)
            self.ini.writeIni('Golden Sample', key, text)
            # TODO
            # Write golden sample settings in ini file

            self.save_btn_collection[idx - 1].setText(text)
            self.load_btn_collection[idx - 1].setText(text)

    def loadPressed(self, idx):
        section = 'Golden Sample Template {}'.format(str(idx))
        self.gs_check_1 = int(self.ini.readIni(section, 'GS1_Check'))
        self.gs_check_2 = int(self.ini.readIni(section, 'GS2_Check'))
        self.gs_check_3 = int(self.ini.readIni(section, 'GS3_Check'))
        self.gs_check_4 = int(self.ini.readIni(section, 'GS4_Check'))
        self.gs_check_5 = int(self.ini.readIni(section, 'GS5_Check'))
        self.gs_check_6 = int(self.ini.readIni(section, 'GS6_Check'))
        self.gs_check_7 = int(self.ini.readIni(section, 'GS7_Check'))
        self.gs_check_8 = int(self.ini.readIni(section, 'GS8_Check'))

        self.gs_pass_1 = int(self.ini.readIni(section, 'GS1_Pass'))
        self.gs_pass_2 = int(self.ini.readIni(section, 'GS2_Pass'))
        self.gs_pass_3 = int(self.ini.readIni(section, 'GS3_Pass'))
        self.gs_pass_4 = int(self.ini.readIni(section, 'GS4_Pass'))
        self.gs_pass_5 = int(self.ini.readIni(section, 'GS5_Pass'))
        self.gs_pass_6 = int(self.ini.readIni(section, 'GS6_Pass'))
        self.gs_pass_7 = int(self.ini.readIni(section, 'GS7_Pass'))
        self.gs_pass_8 = int(self.ini.readIni(section, 'GS8_Pass'))

        self.updateBox(self.sample_number.currentIndex() + 1)

    def updateBox(self, idx):
        if idx >= 1:
            gs_check = None
            gs_pass = None
            if idx == 1:
                gs_check = self.gs_check_1
                gs_pass = self.gs_pass_1
            elif idx == 2:
                gs_check = self.gs_check_2
                gs_pass = self.gs_pass_2
            elif idx == 3:
                gs_check = self.gs_check_3
                gs_pass = self.gs_pass_3
            elif idx == 4:
                gs_check = self.gs_check_4
                gs_pass = self.gs_pass_4
            elif idx == 5:
                gs_check = self.gs_check_5
                gs_pass = self.gs_pass_5
            elif idx == 6:
                gs_check = self.gs_check_6
                gs_pass = self.gs_pass_6
            elif idx == 7:
                gs_check = self.gs_check_7
                gs_pass = self.gs_pass_7
            elif idx == 8:
                gs_check = self.gs_check_8
                gs_pass = self.gs_pass_8

            self.check_1.setChecked(functions.checkBit(gs_check, 1))
            self.check_2.setChecked(functions.checkBit(gs_check, 2))
            self.check_3.setChecked(functions.checkBit(gs_check, 3))
            self.check_4.setChecked(functions.checkBit(gs_check, 4))
            self.check_5.setChecked(functions.checkBit(gs_check, 5))
            self.check_6.setChecked(functions.checkBit(gs_check, 6))
            self.check_7.setChecked(functions.checkBit(gs_check, 7))
            self.check_8.setChecked(functions.checkBit(gs_check, 8))

            self.pass_1.setChecked(functions.checkBit(gs_pass, 1))
            self.pass_2.setChecked(functions.checkBit(gs_pass, 2))
            self.pass_3.setChecked(functions.checkBit(gs_pass, 3))
            self.pass_4.setChecked(functions.checkBit(gs_pass, 4))
            self.pass_5.setChecked(functions.checkBit(gs_pass, 5))
            self.pass_6.setChecked(functions.checkBit(gs_pass, 6))
            self.pass_7.setChecked(functions.checkBit(gs_pass, 7))
            self.pass_8.setChecked(functions.checkBit(gs_pass, 8))
