
class AbilityScore():
    def __init__(self, val):
        self.val = val

    @property
    def mod(self):
        return (self.val - 10) // 2



class Race():
    abilitybonus = {'ability':'val'}
    size = 'value'
    speed = 0
    languages = {'Language' : {'read', 'write', 'speak'}}
    proficiencies = {'weapons' : {}, 'skills' : {}, 'tools' : {}}
    powers = {}
    abilities = {} #Passive




class Aggregate():
    def __init__(self, kwd, *args):
        super().__init__()

    def __contains__(self, val):
        if val in self.__dict__:
            return True
        for item in self.__dict__:
            if val in item:
                return True
        return False

    def __getattr__(self, attr):
        if attr in self:
            sources = [src for src in self.__dict__ if attr in src]
            values = [src.attr for src in sources]
            return self.consolidate(values)
        else:
            raise AttributeError

    def consolidate(self, lst):
        val = lst.pop(0)
        for item in lst:
            if isinstance(item, list):
                item = self.consolidate(item)
            if isinstance(val, int):
                val += item
            elif isinstance(val, set):
                val = val | item

a = Aggregate('key')
print(a.__dict__)






## Keep for later:
#
#class Tracker():
#    """Values that are meant to be tracked, such as HP, charges, and
#    spell slots"""
#    def __init__(self, val, max = None):
#        self.val = val
#        self.max = max
#
#    def __repr__(self):
#        return "%d" % val + ("/%d" % maxval if max != None else "")
#
#    def __add__(self, val):
#        if val isinstance(int):
#            self.val = min(self.val + val, self.max)
#            return self
#        else:
#            return NotImplemented
#
#    def __sub__(self, val):
#        if val isinstance(int):
#            self.val = max(self.val - val, 0)
#            return self
#        else:
#            return NotImplemented
#
#    #Do I need these?
#    def __radd__(self, val):
#        pass
#    def __rsub__(self, val):
#        pass
