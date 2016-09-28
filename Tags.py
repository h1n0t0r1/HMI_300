import inspect
class tag():

    def __init__(self):
        self._val = None
        self.isChanged = None
        self._old_value = None


    def getValue(self):
        return self._val


    def setValue(self, value):
        self._val = value

    def refresh(self):
        if self._val != self._old_value:
            self.isChanged = True
            self._old_value = self._val
        else:
            self.isChanged = False

