from yaml import YAMLObject


class GameData(YAMLObject):
    pass


# Top-level abstractions of RPG game data
class RPGSystem(GameData):
    class Creature(GameData):
        def __init__(self):
            self.stats = {}
            self.powers = {}
            self.abilities = {}
            # self.inventory = []   #Item drops for monsters?  Not sure if necessary.

    class Group(GameData):
        def __getattr__(self, name):
            return {}   #Guarantee return value upon accessing nonexistent fields.  Remove?

    class Object(GameData):
        pass

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
