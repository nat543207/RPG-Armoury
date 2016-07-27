import yaml
import core.rpg

# class GameDataMeta(yaml.YAMLObjectMetaclass):
#     dataclasses = {}
#     reserved_tags = set()
#     def __init__(cls, name, bases, kwds):
#         super().__init__(name, bases, kwds)
#         GameDataMeta.dataclasses[name] = cls
#         GameDataMeta.reserved_tags |= {cls.yaml_tag}

#     def __repr__(cls):
#         """Print format:  ClassName(arg1=val1, arg2=val2, ... argn=valn)"""
#         return "%s(%s)" % (cls.__name__ , ', '.join("%s=%s" % (k,v)
#                 for k,v in cls.__dict__.items() if k[:1] != '_'))



# class GameDataType(yaml.YAMLObject, metaclass=GameDataMeta):
#     yaml_tag = '!Data'

#     @classmethod
#     def from_yaml(cls, loader, node):
#         parent = loader.inheritance_helper.top
#         types = {}
#         for name, data in node.value:
#             name = loader.construct_object(name)
#             data = loader.construct_object(data, deep=True)
#             types[name] = type(name, (parent,), data)
#         return types


# class CharacterData(yaml.YAMLObject):
#     yaml_tag = '!CharacterList'

#     @classmethod
#     def from_yaml(cls, loader, node):
#         if not isinstance(node, yaml.MappingNode):
#             raise TypeError("Can only construct characters from mappings, not scalars or sequences")
#         characters = {}
#         for n, d in node.value:
#             name = loader.construct_object(n)
#             data = loader.construct_object(d, deep=True)
#             data.update({'name':name})
#             characters[name] = core.rpg.Character(**data)
#         return characters

# class ItemList(yaml.YAMLObject):
#     yaml_tag = '!ItemList'

#     @classmethod
#     def from_yaml(cls, loader, node):
#         pass

# class AggregateProperty(yaml.YAMLObject):
#     yaml_tag = '!Aggregate'

















# class YAMLType(yaml.YAMLObject):
#     yaml_tag = '!Type'
#     @classmethod
#     def from_yaml(cls, loader, node):
#         pass






class RPGLoader(yaml.Loader):
    typelist = []
    def __init__(self, stream):
        super().__init__(stream)
        self.inheritance_helper = RPGLoader.Stack([object])

    class Stack(list):
        def push(self, obj):
            self.append(obj)
        @property
        def top(self):
            return self[-1]

    def construct_mapping(self, node):
        parents = self.inheritance_helper
        dct = {}
        for k, v in node.value:
            try:
                k = self.construct_object(k)
                t = type(k, (parents.top,), {})
                self.typelist.append(t)
                parents.push(t)
                v = self.construct_object(v)
                dct[k] = v
            except TypeError:
                print(k)
                raise
        return dct

class CharacterLoader(yaml.Loader):
    class CharacterList(yaml.YAMLObject):
        yaml_tag = '!CharacterList'
        @classmethod
        def from_yaml(cls, loader, node):
            characters = []
            for char in node.value:
                # characters.append()
                pass
