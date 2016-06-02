import yaml

class GameDataMeta(yaml.YAMLObjectMetaclass):
    dataclasses = {}
    def __init__(cls, name, bases, kwds):
        super().__init__(name, bases, kwds)
        GameDataMeta.dataclasses[name] = cls
        cls.__repr__ = GameDataMeta.__repr__

    def __repr__(cls):
        return "%s(%s)" % (cls.__name__ , ', '.join("%s=%s" % (k,v)
                for k,v in cls.__dict__.items() if k[:1] != '_'))



class GameData(yaml.YAMLObject, metaclass=GameDataMeta):
    yaml_tag = '!Data'

    @classmethod
    def from_yaml(cls, loader, node):
        data = loader.construct_sequence(node, deep=True)
        val = type(data[0], (cls,), data[1])
        return val

    def __getattribute__(self, attr):
        if attr in __dict__:
            return __dict__[attr]
        else:
            return None
