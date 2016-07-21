# import core.gui as gui
import core.datastore
# import plugins.dnd5 as system
import yaml
# gui.launch()

# f = open('plugins/dnd5/dnd5.yml')
# doc = core.datastore.load(f)
# print(doc)
f = open('plugins/dnd5/dnd5.yml')
doc = core.datastore.load(f)
print(doc)
print(core.datastore.GameDataMeta.dataclasses)
