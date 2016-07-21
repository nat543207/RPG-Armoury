import core.rpg as rpg


class Character():
    def __init__(self, race, cls, background=None, **stats):
        # print("%s, %s, %s" % (race.__dict__, cls.__dict__, background.__dict__))
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
        self.skills = {}
        # self.size = {}
