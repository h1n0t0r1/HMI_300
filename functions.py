from PyQt5.QtWidgets import QDesktopWidget

def percentage(percent, whole):
    return (percent * whole) / 100

def getGeometry():
    size = QDesktopWidget().screenGeometry()
    geometry = [size.width(), size.height()]
    return geometry

def checkBit(num, bit):
    if num & (1 << bit):
        return True
    else:
        return False

def setBit(num, bit):
    return num | (1 << bit)

def unsetBit(num, bit):
    return num & ~(1 << bit)

def toggleBit(num, bit):
    return num ^ (1 << bit)

