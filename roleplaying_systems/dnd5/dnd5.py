# from base_rpg import RPG_System
from yaml import YAMLObject

class GameData(YAMLObject):
    yaml_tag = '!Data'
    def __init__(self, **kwargs):
        for key,val in kwargs:
            setattr(self, key, val)


class dnd5:#(RPG_System):
    display_name = 'Dungeons and Dragons (5e)'


    # class AbilityScore:
    #     def __init__(self, name='Ability Score', abbrev='ABS', base_value=0):
    #         self.name = name
    #         self.abbrev = abbrev
    #         self.base_value = base_value
    #         self.base_modifiers = []

    #     @property
    #     def value(self):
    #         return self.base_value + sum(self.modifiers)

    #     @property
    #     def modifier(self):
    #         return (self.value() - 10) // 2

    #     def add_base_modifier(self, mod):
    #         self.base_modifiers = self.base_modifiers + [mod]



    # class Skill:
    #     def __init__(self, name, base_ability, proficient=False):
    #         self.name = name
    #         self.base_ability = base_ability
    #         self.proficient = proficient

    #     @property
    #     def modifier(self):
    #         return self.base_ability.modifier



    class Race:
        ability_score_increases = []
        languages = []
        proficienceis = []
        abilities = [] # Passives
        powers = [] # Actives



    # class Class:
    #     pass

    # class Creature:
    #     def __init__(self, **kw):
    #         super().__init__()
    #         self.hp = kw['hp']
    #         self.name = 'Creature Name'
    #         self.ac = 0
    #         self.ability_scores ={
    #                 'str': AbilityScore('Strength', 'STR', kw['str']),
    #                 'dex': AbilityScore('Dexterity', 'DEX', kw['dex']),
    #                 'con': AbilityScore('Constitution', 'CON', kw['con']),
    #                 'int': AbilityScore('Intelligence', 'INT', kw['int']),
    #                 'wis': AbilityScore('Wisdom', 'WIS', kw['wis']),
    #                 'cha': AbilityScore('Charisma', 'CHA', kw['cha']),
    #             }
    #         self.powers = []



    # class Character(Creature):
    #     def __init__(self, **kw):
    #         super().__init__(**kw)
    #         self.race = kw['race']
    #         self.classes = kw['classes']
    #         self.background = kw['background']
    #         self.inventory = []

    #     def role(self):
    #         return "Test"

    #     def __getattr__(self, name):
    #         if name in self.__dict__:
    #             return self.__dict__[name]
    #         elif name in self.stats:
    #             attr = self.stats[name]
    #         else:
    #             attr = []
    #         groups = self.groups.values()
    #         for group in groups:
    #             attr += getattr(group, name)
    #         self.setattr(name, attr)
    #         return attr


    #     def __setattr__(self, name, val):
    #         if isinstance(val, Group):
    #             self.groups[name] = val
    #         elif name in self.stats.keys():
    #             self.stats = val
    #         super().__setattr__(name, val)


class Power(YAMLObject):
    yaml_tag = '!Power'
    def __repr__(self):
        string = "Power("
        for key,val in self.__dict__.items():
            string += "%s=%s, " % (key, val.strip())
        return string + ')'




    # class Item:
    #     pass
    # class Feat:
    #     pass
