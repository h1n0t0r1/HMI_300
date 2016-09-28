import OpenOPC


class OPC():
    def __init__(self):
        self.opc = OpenOPC.client()
        #self.opc.connect(server)

    def _connect(self, server):
        self.opc.connect(server)

    def _addGroup(self, tags, group):
        try:
            self.opc.read(tags, group=group)
        except TypeError:
            print('Some of the variables in the list is not found on OPC Server')

    def _removeGroup(self, group):
        self.opc.close(group)

    def _readGroup(self, group):
        tag_list = [tag[1] for tag in self.opc.read(group=group)]
        return tag_list


