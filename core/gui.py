from plugins.dnd5 import Character
ext_character = Character('Elf', 'Wizard', 123, str=11, int=12, cha=13, wis=14, con=15, dex=16)

from kivy.app import App
from kivy.adapters.listadapter import ListAdapter
from kivy.properties import StringProperty
from kivy.uix.button import Button

# To keep the rpgarmoury.kv file pure, any functionality not strictly
# related to UI appearance should be made here.  Most often, this will be
# implementation of custom Widgets that are not simply composite layouts of
# other widgets.


class CoercedStringProperty(StringProperty):
    """Coerces the passed value into a string, allowing non-string values
       to be represented easily from within kv file.  Not for direct use;
       rather, should only be used through the OmniDisplay class."""
    def __set__(self, obj, val):
        super().__set__(obj, str(val))

class Panel(Button):
    text = CoercedStringProperty()

class RPGArmoury(App):
    pass

def launch():
    RPGArmoury().run()
