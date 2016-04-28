# A roleplaying system, which defines the rules and applicable data
# members of that system
class System:
    def __init__(self):
        self.presentation_name = 'Generic Roleplaying System'
        self.id = 'base_system'

    # A single living thing, or group thereof
    class Creature:
        def __init__(self):
            self.hp = 0
            self.name = 'Creature Name'


    # A single inanimate object: a weapon, a potion, a statue, etc.
    class Object:
        def __init__(self):
            self.name = 'Object Name'
            self.properties = []
            self.description = ''


    class Item:
        def __init__(self):
            self.weight = 0
            self.quantity = 0


    # A quality of a creature or object:  an ability score, a skill check,
    # an enchantment or weapon property, etc.
    class Attribute:
        def __init__(self):
            self.dependencies = []
            self.name = 'Attribute Name'

        # Return the value of the Attribute
        def value(self):
            pass
        pass

        def __repr__(self):
            return self.name


    # An action that a creature can take, a passive skill, etc.
    class Power:
        def __init__(self):
            self.name = 'Power Name'

        def __repr__(self):
            return self.name


    # A group to which a creature belongs that affords them certain attributes;
    # a class, a race, a backgrond, a kingdom, etc.
    class Group:
        def __init__(self):
            self.name = 'Group Name'


    # A description of when creatures "level up" or receive similar bonuses
    class Progression:
        def __init__(self):
            self.group = None


    class Character(Creature):
        pass
