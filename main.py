# import core.gui as gui
import core.datastore
import plugins.dnd5 as system
import yaml
# gui.launch()

# f = open('plugins/dnd5/dnd5.yml')
# doc = core.datastore.load(f)
# print(doc)
f = open('plugins/dnd5/dnd5.yml')
# doc = core.datastore.RPGLoader(f).get_single_node()
# doc = yaml.load(f, core.datastore.RPGLoader)
doc = core.datastore.load(f)
print(doc)
print(core.datastore.GameDataMeta.dataclasses)
# print(doc['Item']['Armor']['LightArmor']['Padded'].__class__)
# for cls in core.datastore.GameDataMeta.dataclasses.values():
#     print("%s: %s" % (str(cls.__name__), str([b.__name__ for b in cls.__bases__])))

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
