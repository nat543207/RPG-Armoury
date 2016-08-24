import os
import sys
import core.rpg as rpg

class PluginMeta(type):
    pass


class PluginBase(metaclass=PluginMeta):
    data = {}
    ui_file = None
    data_file = None

    def __init__(self):
        """Prepare plugin to construct a new character"""
        self.data_file = self.resourcefile(self.data_file)
        self.ui_file = self.resourcefile(self.ui_file)
        self.load_data()

    def load_data(self):
        """Load data from a file for reference when character displayed"""
        self.data = yaml.load(self.data_file)

    def search(self, name):
        try:
            return self.data[name]
        except KeyError:
            return None

    def construct_character(self, data):
        return self.Character(**data)


    def resourcefile(self, name):
        """Open the file with the provided name from the plugin package"""
        rootdir = os.path.dirname(sys.modules[self.__class__.__module__].__file__)
        path = os.path.join(rootdir, name)
        return open(path)

    class Character(rpg.Character):
        pass
