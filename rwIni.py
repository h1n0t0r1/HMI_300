import configparser

class RWIni(configparser.ConfigParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.read(self.path)

    def readIni(self, section, key):
        val = self.get(section, key)
        return val

    def writeIni(self, section, key, value):
        self.set(section, key, value)
        with open(self.path, 'w') as configfile:
            self.write(configfile)