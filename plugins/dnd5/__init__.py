import core.rpg as rpg


class DnD5_Character(rpg.Character):
    def __init__(self, race, cls, background=None, **stats):
        self.race = race
        self.cls = cls
        self.background = background
        self.inventory = []
        self.hp = 0
        # self.spellslots = (0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.spellsprepared = {}
        self.feats = {}
        self.itemslots = {}
        self.description = {}
        self.ac = 0

        self.scores = stats
        self.hitdice = {}
        self.spellbook = {}
        self.proficiencies = {}
        self.languages = {}
        self.powers = {}
        self.passivepowers = {}
        self.speed = {}
        self.skills = {'talking', 'walking', 'reading'}
        self.xp = 0
        # self.size = {}










import collections
import core.containers



class Inventory(collections.OrderedDict):
    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        try:
            for key in self:
                if other[key] != self[key]:
                    return False
            return True
        except KeyError:
            return False

    def store(self, item, quantity=1):
        self[item] = quantity

    def remove(self, item):
        self.pop(item, None)



class Container(rpg.Object, Inventory):
    def __init__(self, **kwargs):
        rpg.Object.__init__(self, **kwargs)
        Inventory.__init__(self)


class InventoryCharacter(DnD5_Character):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inventory = Inventory()

    def get(self, item):
        self.inventory.store(item)

class Skill:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Elf:
    powers = {Skill('Nightvision')} #TODO Being in a set hoses the representation in the interface
    skills = {Skill('Treeclimbing')}

class Wizard:
    skills = {Skill('Magic')}

class Fingon(InventoryCharacter):
    def __init__(self, **kwargs):
        self.inventory = Inventory()
        self.name = 'Fingon Anwamane'
        self.hp = 5
        self.hpmax = 7
        self.xp = 12
        self.ac = 0
        self.hitdice = '12d12'
        self.race = Elf
        self.classes = {Wizard}
        self.skills = core.containers.AggregateValue('skills', kwargs, self.race, *self.classes)
        self.languages = {}


