# A single living thing, or group thereof
class Creature:
    pass

# A single inanimate object: a weapon, a potion, a statue, etc.
class Object:
    pass

# A quality of a creature or object:  an ability score, a skill check,
# an enchantment or weapon property, etc.
class Attribute:
    # Return the value of the Attribute
    def value(self):
        pass
    pass

# An action that a creature can take, a passive skill, etc.
class Power:
    pass

# A set of duties or qualifications that a creature might meet:  a class,
# a background, a title, etc.
class Role:
    pass

# A description of when creatures "level up" or receive similar bonuses
class Progression:
    pass
