import yaml
import collections

# class GameDataMeta(yaml.YAMLObjectMetaclass):
#     dataclasses = {}
#     reserved_tags = set()
#     def __init__(cls, name, bases, kwds):
#         super().__init__(name, bases, kwds)
#         GameDataMeta.dataclasses[name] = cls
#         GameDataMeta.reserved_tags |= {cls.yaml_tag}
#
#     def __repr__(cls):
#         """Print format:  ClassName(arg1=val1, arg2=val2, ... argn=valn)"""
#         return "%s(%s)" % (cls.__name__ , ', '.join("%s=%s" % (k,v)
#                 for k,v in cls.__dict__.items() if k[:1] != '_'))






class Data(yaml.YAMLObject):
    yaml_tag = '!Data'
    @classmethod
    def from_yaml(cls, loader, node):
        data = loader.construct_mapping(node)
        data['__class'] = True
        return data



yaml.add_constructor('tag:yaml.org,2002:map', lambda l, n: collections.OrderedDict(l.construct_pairs(n)))
# class RPGLoader(yaml.Loader):
#     typelist = []
#     def __init__(self, stream):
#         super().__init__(stream)
#         self.inheritance_helper = RPGLoader.Stack([object])

#     class Stack(list):
#         def push(self, obj):
#             self.append(obj)
#         @property
#         def top(self):
#             return self[-1]

#     def construct_mapping(self, node):
#         parents = self.inheritance_helper
#         dct = {}
#         for k, v in node.value:
#             try:
#                 k = self.construct_object(k)
#                 t = type(k, (parents.top,), {})
#                 self.typelist.append(t)
#                 parents.push(t)
#                 v = self.construct_object(v)
#                 dct[k] = v
#             except TypeError:
#                 print(k)
#                 raise
#         return dct
