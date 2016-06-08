# import core.gui as gui
import core.datastore
import plugins.dnd5 as system
import yaml
# gui.launch()

doc = yaml.load(open('plugins/dnd5/dnd5.yml'))
# print(doc)

elf = core.datastore.GameDataMeta.dataclasses['Elf']
ranger = core.datastore.GameDataMeta.dataclasses['Ranger']
c = system.Character(elf, ranger, str=10, dex=10, int=10, wis=10, con=10, cha=10)
print(elf)
print(ranger)
print(c.size)
