# import core.gui as gui
import core.datastore
import plugins.dnd5 as system
import yaml
# gui.launch()

# doc = yaml.load(open('plugins/dnd5/dnd5.yml'))
# print(doc)

# elf = core.datastore.GameDataMeta.dataclasses['Elf']
# ranger = core.datastore.GameDataMeta.dataclasses['Ranger']
# c = system.Character(elf, ranger, str=10, dex=10, int=10, wis=10, con=10, cha=10)
# print(elf)
# print(ranger)
# print(c.size)


# out = yaml.Dumper(open('test.yml'))
# node = yaml.MappingNode(tag='tag:yaml.org,2002:map', value=[(yaml.ScalarNode(tag='tag:yaml.org,2002:str', value='Item')), (yaml.ScalarNode(tag='tag:yaml.org,2002:str', value='Test'))])
# print(node)


# No accidental type masking:
# a = type('Test', (object,), {})
# b = type('Test', (object,), {'attr' : 1})
# t1 = a()
# t2 = b()
# print(t1.__class__)
# print(t2.__class__)
# print(t1.__class__ is t2.__class__)
