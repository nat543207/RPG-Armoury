from plugins import PluginBase
from . import gamedata
import yaml

from . import gui




class dnd5(PluginBase):
    data_file = 'dnd5.yml'
    ui_file = 'dnd5.kv'
    Character = gamedata.DND5_Character

    def load_data(self):
        raw_data = yaml.load(self.data_file)
        self.parse(raw_data)

    def parse(self, dct, parents=(object,)):
        for k in dct:
            cls = self.search(k)
            if '__class' in dct[k]:
                if cls is None:
                    cls = type(k, parents, dct)
                self.data[k] = cls
            else:
                if cls is None:
                    cls = type(k, parents, {})
                self.data[k] = cls
                self.parse(dct[k], (cls,))




import sys
sys.modules[__name__] = dnd5()
