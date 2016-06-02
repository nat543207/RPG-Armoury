class Meta(type):
    def __init__(self, *args, **kwargs):
        self.__contains__ = Meta.__contains__
        self.__getattr__ = Meta.__getattr__
        self.__getitem__ = Meta.__getitem__

    def __contains__(self, val):
        if val in self.__dict__:
            return True
        return False

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        if key in self.stats:
            val = sum([v[key] for v in self.__dict__.values() if key in v])
            return val
        raise IndexError

    def __getattr__(self, attr):
        try:
            return self.__getitem__(self, attr)
        except IndexError:
            raise AttributeError


class Character():
    def __init__(self, race=None, cls=None, **kwargs):
        self.stats = {}
        self.race = race
        self.cls = cls
        for k,v in kwargs.items():
            self.stats[k] = v

    def __repr__(self):
        return str(self.stats)

    def __contains__(self, val):
        if val in self.__dict__:
            return True
        return False

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        if key in self.stats:
            val = sum([v[key] for v in self.__dict__.values() if key in v])
            return val
        raise IndexError

    def __getattr__(self, attr):
        try:
            return self.__getitem__(attr)
        except IndexError:
            raise AttributeError


class Race(metaclass=Meta):
    stats = {'dex' : '2'}
    str = 2

class Class(metaclass=Meta):
    str = 1





c = Character(Race, Class, dex=12, str=15, int=19)
print(c)
print(c.str)
