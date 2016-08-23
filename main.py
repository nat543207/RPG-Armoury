import core.gui as gui
import core.datastore


gui.RPGArmoury().run()


# import yaml
# import importlib
# name = 'dnd5'
# char = yaml.load(open('characters.yml'))['Fingon Anwamane']
# plugin = importlib.import_module('plugins.%s' % name)
# char = plugin.Character(**char)
# print(char.dex)
