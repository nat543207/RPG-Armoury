class Character():
    """Data representing the state of a single character:  its powers, stats,
    inventory, etc."""

    """ What makes a character?
        + 6 ability scores
        + 1 race
            + Subrace?
        + 1? background
        + 1+ class(es)
        + inventory

        Derrived values:
        + HP & Hit Dice
        - AC
        + Spell Slots
        + Spells Known
        + Prepared Spells
        - Skill Bonuses
        + Proficiencies
        - Speed
        - Size
        + Languages
        + Feats
        + Activated Powers
        - Passive Abilities

        Miscelaneous:
        + Equipment slots
        + Appearance
        + Personality and Behaviors
        + Personal History
        """
        def __init__(self, **kwargs):
            self.scores = {}    #Empty dict
            self.race = None    #Classref
            self.background = None #Classref
            self.classes = [()] #List of tuples, (level, classref).  Order matters for classing.
            self.inventory = [] #List of Item objects - instances of Item subclasses
            self.hp = None      #Property of some kind
            self.hitdice = {()} #Set of tuples, (number, die)
            self.spellslots = (0, 0, 0, 0, 0, 0, 0, 0) #9-tuple of ints
            self.spellbook = {} #Set of classrefs to known spells
            self.preparedspells = {} #Set of classrefs to prepared spells
            self.proficiencies = {} #Set - only chosen, not granted
            self.languages = {} #Dict of name:proficiency pairs - only chosen, not granted by race/class
            self.feats = {}     #Set of classrefs
            self.powers = {()}  #Set of tuples, (uses, classref)
            self.slots = {}     #Equipemnt slots
            self.description = {} #Dict to hold descriptions of character apperance, personality, etc.





            #Other accessible attributes, calculable from given data:
            # self.ac = 0
            # self.skills = {}
            # self.speed
            # self.size
            # self.passives

        def __getattribute__(self, attr):
            if attr in self.__dict__:
                return self.__dict__[attr]
