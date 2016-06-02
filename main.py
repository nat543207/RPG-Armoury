import core.gui as gui
import core.datastore
import plugins.dnd5 as system
import yaml
# gui.launch()


doc = yaml.load(open('plugins/dnd5/dnd5.yml'))
print(doc)

print(core.datastore.GameDataMeta.dataclasses)
