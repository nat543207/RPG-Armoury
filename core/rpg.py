"""Top-level abstractions of RPG game data"""


class Data:
    name = 'Unnamed Game Datum'
    def __init__(self, **kwargs):
        # for key in self.defaults:
        #     setattr(self, key, kwargs.pop(key, self.defaults[key]))
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.__dict__)




class Character(Data):
    def __repr__(self):
        """Print format:  ClassName(arg1=val1, arg2=val2, ... argn=valn)"""
        # return "%s(%s)" % (cls.__class__.__name__ , ', '.join("%s=%s" % (k,v)
        #         for k,v in cls.__dict__.items() if k[:1] != '_'))
        return str(self.__dict__)



class Creature(Data):
    """A single living creature, or small group thereof as in the case
    of a school of fish, a swarm of locusts, or a flock of birds."""
    pass



class Group(Data):
    """A class, party, national affiliation, or other designation that
    provides an individual with some benefits, detriments, powers, or
    the like"""
    def __repr__(self):
        return self.__name__



class Object(Data):
    """A single nonliving entity such as a door, weapon, potion, or
    vehicle"""
    # def __str__(self):
    #     return """Name: %s
    #     Data: %s""" % (self.name, self.__dict__)
    pass


class Attribute(Data):
    """A quality or property of a thing, such as an ability score, an
    enchantment, a status effect, or the like."""
    pass



class Power(Data):
    """An activated skill, ability, attack, etc. that a creature has
    access to."""
    pass












class System(Data):
    """A game system that defines the items, creatures, powers, and other
    rules of an RPG.  Mostly, this will operate as a container for game-
    specific data types."""
    pass
