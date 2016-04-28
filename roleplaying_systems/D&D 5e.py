from base_rpg import System

class DnD_5e(System):
    def __init__(self):
        pass

    def newCharacter():
        return Character()


    class AbilityScore(System.Attribute):
        def __init__(self, name='Ability Score', abbrev='ABS', base_value=0):
            self.name = name
            self.abbrev = abbrev
            self.base_value = base_value

        @property
        def value(self):
            return self.base_value + sum(self.modifiers)

        @value.setter #TODO
        def value(self, val):
            pass

        @property
        def modifier(self):
            return (self.value() - 10) // 2


    class Skill(System.Attribute):
        def __init__(self, base_ability):
            self.base_ability = base_ability

        @property
        def modifier(self):
            return self.base_ability.modifier


    class Character(System.Character):
        def __init__(self, STR, DEX, CON, INT, WIS, CHA, race=None, classes=[]):
            self.ability_scores ={
                    'str': AbilityScore('Strength', 'STR', STR),
                    'dex': AbilityScore('Dexterity', 'DEX', DEX),
                    'con': AbilityScore('Constitution', 'CON', CON),
                    'int': AbilityScore('Intelligence', 'INT', INT),
                    'wis': AbilityScore('Wisdom', 'WIS', WIS),
                    'cha': AbilityScore('Charisma', 'CHA', CHA),
                }
            self.race = race
            self.classes = classes
            self.inventory = []

        def class(self):
            return "Test"


    class Race(System.Group):
        ability_score_bonuses = []
        languages = []
        proficienceis = []
        powers = []


    class Class(System.Group):
        def __init__(self):
            self.level = 1

    class Item(System.Item):
        pass


    class Power:
        pass


    class Feat:
        pass
