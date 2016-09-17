from numbers import Number as num

class AggregateValue():
    def __init__(self, prop, *srcs, start_val=None, validate=True):
        self.prop = prop
        self.start_val = start_val
        self.srcs = [s for s in srcs if hasattr(s, prop)] if validate else srcs
        # super().__init__(self.val)

    def __get__(self, obj=None, type=None):
        lst = [getattr(s, self.prop) for s in self.srcs]
        return self.combine(self.start_val, *lst)

    def __iter__(self):
        return (i for i in self.__get__())

    def combine(self, val, *vals):
        try:
            cmb = self.combine(vals[0], *vals[1:])
            if val is None or cmb is None:
                raise TypeError
            elif isinstance(val, set) and isinstance(cmb, set):
                return val | cmb
            elif isinstance(val, num) and isinstance(cmb, num):
                return val + cmb
            elif isinstance(val, list) and isinstance(cmb, list):
                return val + cmb
            else:
                raise TypeError("No rule for combining types %s and %s" % (type(val), type(cmb)))
        except IndexError:
            return val
        except TypeError:
            if val is None:
                return cmb
            elif cmb is None:
                return val
            else:
                raise

    def __str__(self):
        return str(self.__get__())


class AutoAggregator:
    def __init__(self, *srcs):
        self.sources = srcs

    def __getattribute__(self, attr):
        try:
            val = AggregateValue(attr, *super().__getattribute__('sources')).__get__()
        except AttributeError:
            val = super().__getattribute__(attr)
        return val
