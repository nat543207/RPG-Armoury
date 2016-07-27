"""Top-level abstractions of RPG game data"""



class Character:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        """Print format:  ClassName(arg1=val1, arg2=val2, ... argn=valn)"""
        return "%s(%s)" % (cls.__class__.__name__ , ', '.join("%s=%s" % (k,v)
                for k,v in cls.__dict__.items() if k[:1] != '_'))

    def __str__(self):
        return """%s:
        Race:    %s
        Class:   %s
        HP:      %d/%d
        XP:      %d
        AC:      %d""" % (self.name, self.race, self.classes, self.hp, self.hpmax, self.xp, self.ac)

class System():
    """A game system that defines the items, creatures, powers, and other
    rules of an RPG.  Mostly, this will operate as a container for game-
    specific data types."""
    pass

class Creature():
    """A single living creature, or small group thereof as in the case
    of a school of fish, a swarm of locusts, or a flock of birds."""
    pass

class Group():
    """A class, party, national affiliation, or other designation that
    provides an individual with some benefits, detriments, powers, or
    the like"""
    pass

class Object():
    """A single nonliving entity such as a door, weapon, potion, or
    vehicle"""
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def __str__(self):
        return str(self.name)

class Attribute():
    """A quality or property of a thing, such as an ability score, an
    enchantment, a status effect, or the like."""
    pass

class Power():
    """An activated skill, ability, attack, etc. that a creature has
    access to."""
    pass
