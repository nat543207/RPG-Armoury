from datastore import GameData

class RPGSystem(GameData):
    """Top-level abstractions of RPG game data"""

    class Creature(GameData):
        """A single living creature, or small group thereof as in the case
        of a school of fish, a swarm of locusts, or a flock of birds."""
        yaml_tag = '!Creature'


    class Group(GameData):
        """A class, party, national affiliation, or other designation that
        provides an individual with some benefits, detriments, powers, or
        the like"""
        yaml_tag = '!Group'


    class Object(GameData):
        """A single nonliving entity such as a door, weapon, potion, or
        vehicle"""
        yaml_tag = '!Object'


    class Attribute:
        """A quality or property of a thing, such as an ability score, an
        enchantment, a status effect, or the like."""
        yaml_tag = '!Attribute'


    class Power:
        """An activated skill, ability, attack, etc. that a creature has
        access to."""
        yaml_tag = '!Power'
