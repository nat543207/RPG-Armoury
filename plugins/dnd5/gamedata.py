import collections
import core.rpg as rpg
import core.containers as cnt
import sys

class Inventory(collections.OrderedDict):
    def __init__(self, data_dct):
        super().__init__(self)
        for iname in data_dct:
            item = data_dct[iname]
            item['name'] = iname
            self[iname] = Item(**item)
        # cnt.AutoAggregator.__init__(self, *self.contents)
    def __iter__(self):
        return iter(self.values())


class Item(rpg.Object):
    def __init__(self, **data):
        super().__init__(**data)
        try:
            self.contents = Inventory(self.contents)
        except AttributeError:
            pass

    def __iter__(self):
        try:
            return iter(self.contents)
        except AttributeError:
            return (i for i in [])





class DND5_Character(rpg.Character):
    name = 'No-Name McGee'
    race = None
    classes = []
    background = None
    scores = {'int':10, 'wis':10, 'str':10, 'con':10, 'dex':10, 'cha':10}
    inventory = []
    xp = 0
    hitdice = {'d4':0, 'd6':0, 'd8':0, 'd12':0}
    hp = 0
    hpmax = 1
    spellslots = (0, 0, 0, 0, 0, 0, 0, 0, 0)
    skills = {
        'Acrobatics' : 'dex',
        'Animal Handling' : 'wis',
        'Arcana' : 'int',
        'Athletics' : 'str',
        'Deception' : 'cha',
        'History' : 'int',
        'Insight' : 'wis',
        'Intimidation' : 'cha',
        'Investigation' : 'int',
        'Medicine' : 'wis',
        'Nature' : 'int',
        'Perception' : 'wis',
        'Performance' : 'cha',
        'Persuasion' : 'cha',
        'Religion' : 'int',
        'Sleight of Hand' : 'dex',
        'Stealth' : 'dex',
        'Survival' : 'wis'
            }
    spells_prepared = {}
    spellbook = {}
    speed = 0
    feats = {}
    ac = 0
    languages = {}
    proficiencies = {}
    powers = {}
    passive_powers = {}
    description = ''
    item_slots = {}


    def __init__(self, **kwargs):
        # Make ability scores into top-level attributes
        scores = {i : AbilityScore(j) for i,j in kwargs.pop('scores', {}).items()}
        rpg.Character.__init__(self, **scores, **kwargs)
        # self.plugin = sys.modules['plugins.%s' % self.plugin]
        self.skills = {i : Skill(getattr(self, j)) for i,j in self.skills.items()}
        self.inventory = Inventory(self.inventory)
        self.race = self.plugin.search(self.race)
        self.classes = [self.plugin.search(cls) for cls in self.classes]
        # cnt.AutoAggregator.__init__(self, self.race, *self.classes, self.background, self.inventory)



class AbilityScore(rpg.Attribute):
    def __init__(self, value):
        self.value = value

    @property
    def score(self):
        return self.value

    @score.setter
    def score(self, value):
        self.value = value

    @property
    def mod(self):
        return (self.value - 10) // 2



class Skill(rpg.Attribute):
    def __init__(self, ability, name=''):
        self.ability = ability



# class Container(rpg.Object, Inventory):
#     def __init__(self, **kwargs):
#         rpg.Object.__init__(self, **kwargs)
#         Inventory.__init__(self)
