import yaml

class GameDataMeta(yaml.YAMLObjectMetaclass):
    dataclasses = {}
    def __init__(cls, name, bases, kwds):
        super().__init__(name, bases, kwds)
        GameDataMeta.dataclasses[name] = cls

    def __repr__(cls):
        return "%s(%s)" % (cls.__name__ , ', '.join("%s=%s" % (k,v)
                for k,v in cls.__dict__.items() if k[:1] != '_'))

    def __contains__(cls, val):
        for i in cls.__dict__.values():
            if i is None:
                continue
            if val in i:
                return True
        return False

    def __getitem__(cls, key):
        if key in cls.__dict__:
            return cls.__dict__[key]
        for v in cls.__dict__.values():
            # try:
            if v is None:
                continue
            if key in v:
                return v[key]
            # except:



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
