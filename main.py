# import core.gui as gui
import core.datastore
import plugins.dnd5 as system
import yaml
# gui.launch()

print(core.datastore.GameDataMeta.dataclasses)
doc = yaml.load(open('plugins/dnd5/dnd5.yml'))
# print(doc)

# elf = core.datastore.GameDataMeta.dataclasses['Elf']
# ranger = core.datastore.GameDataMeta.dataclasses['Ranger']
# c = system.Character(elf, ranger, str=10, dex=10, int=10, wis=10, con=10, cha=10)
# print(elf)
# print(ranger)
# print(c.proficiencies)

# class Test:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#         self.imabool = True

# tmp = Test()
# tmp.contained = Test()

# print(yaml.dump(tmp, default_flow_style=False))
