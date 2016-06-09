import yaml

class DeepDataStructure():
    def __contains__(cls, val):
        if val in cls.__dict__:
            return True
        for i in cls.__dict__.values():
            try:
                if i is None:
                    continue
                if val in i:
                    return True
            except TypeError:
                pass
        return False

    def __getitem__(cls, key):
        if key in cls.__dict__:
            return cls.__dict__[key] #Return, or prepare to cobine?
        for v in cls.__dict__.values():
            try:
                if v is None:
                    continue
                if key in v:
                    return v[key]
            except TypeError:
                pass


class GameDataMeta(yaml.YAMLObjectMetaclass):
    dataclasses = {}
    def __init__(cls, name, bases, kwds):
        super().__init__(name, bases, kwds)
        GameDataMeta.dataclasses[name] = cls

    def __repr__(cls):
        return "%s(%s)" % (cls.__name__ , ', '.join("%s=%s" % (k,v)
                for k,v in cls.__dict__.items() if k[:1] != '_'))



class GameType(yaml.YAMLObject, metaclass=GameDataMeta):
    yaml_tag = yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG

    @classmethod
    def from_yaml(cls, loader, node):
        # print(cls)
        # print(node)
        key, val = node.value[0]
        print(key)
        print(val)

    def __getattribute__(self, attr):
        if attr in __dict__:
            return __dict__[attr]
        else:
            return None


class GameDataType(GameType):
    yaml_tag = '!Data'

    @classmethod
    def from_yaml(cls, loader, node):
        data = loader.construct_sequence(node, deep=True)
        val = type(data[0], (cls,), data[1])
        return val

