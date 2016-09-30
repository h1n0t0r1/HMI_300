from SimpleWindow import SimpleWindow, QGroupBox
from PyQt5.QtWidgets import QComboBox, QLabel
from PyQt5 import QtCore
from HMIButtons import BlueButton

class GoldenSample(SimpleWindow):
    def __init__(self):
        super().__init__()
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
        self.sample_number.currentIndexChanged.connect(self.setSampleLabel)
        ##      Sample Number Label     ##

        self.sample_label = QLabel('', self.box)
        self.sample_label.setStyleSheet('background-color: transparent; border-style: none; font-size: 32px;')

        ##      Setup Side Buttons      ##

        self.save_label = QLabel('Save Template', self)
        self.save_label.setStyleSheet('font-size: 32px')

        self.save_tmp1_btn = BlueButton('empty', self)
        self.save_tmp2_btn = BlueButton('empty', self)
        self.save_tmp3_btn = BlueButton('empty', self)
        self.save_tmp4_btn = BlueButton('empty', self)
        self.save_tmp5_btn = BlueButton('empty', self)
        self.save_tmp6_btn = BlueButton('empty', self)
        self.save_tmp7_btn = BlueButton('empty', self)
        self.save_tmp8_btn = BlueButton('empty', self)
        self.save_tmp9_btn = BlueButton('empty', self)
        self.save_tmp10_btn = BlueButton('empty', self)

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
        self.load_tmp2_btn = BlueButton('empty', self)
        self.load_tmp3_btn = BlueButton('empty', self)
        self.load_tmp4_btn = BlueButton('empty', self)
        self.load_tmp5_btn = BlueButton('empty', self)
        self.load_tmp6_btn = BlueButton('empty', self)
        self.load_tmp7_btn = BlueButton('empty', self)
        self.load_tmp8_btn = BlueButton('empty', self)
        self.load_tmp9_btn = BlueButton('empty', self)
        self.load_tmp10_btn = BlueButton('empty', self)

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

    def fitToScreen(self, width, height):
        super().fitToScreen(width, height)
        self.gs_count_box.resize(width * 0.1, height * 0.1)
        self.gs_count_box.move(width * 0.02, height * 0.12)
        self.gs_count_label.move(width * 0.025, height * 0.01)
        self.gs_count.resize(width * 0.06, height * 0.04)
        self.gs_count.move(width * 0.02, height * 0.05)

        self.sample_number_box.resize(width * 0.1, height * 0.1)
        self.sample_number_box.move(width * 0.15, height * 0.12)
        self.sample_number_label.move(width * 0.025, height * 0.01)
        self.sample_number.resize(width * 0.06, height * 0.04)
        self.sample_number.move(width * 0.02, height * 0.05)

        self.sample_label.move(width * 0.3, height * 0.25)

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