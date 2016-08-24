import collections
import core.rpg as rpg
import sys

class Inventory(collections.OrderedDict):
    def __init__(self, data_dct):
        self.contents = []
        for iname in data_dct:
            item = data_dct[iname]
            item['name'] = iname
            self.contents.append(Item(**item))
    def __contains__(self, obj):
        return obj in self.contents
    def __iter__(self):
        return (item for item in self.contents)
    def store(self, item, quantity=1):
        self.contents.append(item)
    def remove(self, item):
        self.pop(item, None)
    # def __str__(self):
    #     return '\n'.join([str(i) for i in self.contents])
    # def __repr__(self):
    #     return str(self)


class Item(rpg.Object):
    def __init__(self, **data):
        super().__init__(**data)
        try:
            self.contents = Inventory(self.contents)
        except AttributeError:
            pass





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
    skills = {}
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

    def make_inventory(self, inv):
        constructed = []
        for item in inv:
            try:
                data = inv[item]
                data['name'] = item
                constructed.append(rpg.Object(**data))
            except KeyError:
                raise
        return Inventory(*constructed)


    def __init__(self, **kwargs):
        # Make ability scores into top-level attributes
        scores = kwargs.pop('scores', {})
        super().__init__(**scores, **kwargs)

        # self.plugin = sys.modules['plugins.%s' % self.plugin]
        self.inventory = Inventory(self.inventory)
        self.race = self.plugin.search(self.race)
        self.classes = [self.plugin.search(cls) for cls in self.classes]



    # def __getattr__(self, attr):
    #     if attr in {'wis', 'cha', 'int', 'dex', 'con', 'str'}:
    #         return self.scores[attr]
    #     raise AttributeError("Object of type %s has no attribute '%s'" % (self.__class__, attr))





# class AbilityScore(rpg.Attribute):
#     def __init__(self, value):
#         self.value = value

#     @property
#     def score(self):
#         return self.value

#     @score.setter
#     def score(self, value):
#         self.value = value

#     @property
#     def mod(self):
#         return (self.value - 10) // 2

# class Skill(rpg.Attribute):
#     def __init__(self, name, ability=None, proficient=False, expertise=False):
#         self.name = name
#         self.ability = ability

#     def __repr__(self):
#         return self.name



# class Container(rpg.Object, Inventory):
#     def __init__(self, **kwargs):
#         rpg.Object.__init__(self, **kwargs)
#         Inventory.__init__(self)

