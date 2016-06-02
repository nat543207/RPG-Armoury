from kivy.app import App
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.listadapter import ListAdapter
from kivy.properties import ListProperty, ObjectProperty

# To keep the rpgarmoury.kv file pure, any functionality not strictly
# related to UI appearance should be made here.  Most often, this will be
# implementation of custom Widgets that are not simply composite layouts of
# other widgets.


class Table(ListView):
    # data = ListProperty(['Test2'])

    def __init__(self, **kwargs):
        # print(kwargs)
        super(Table, self).__init__(**kwargs)
        # TODO Figure out why self.adapter refuses to populate from the
        # values provided in rpgarmoury.kv when adapter initialized
        # in this method, instead of kv file
        # print(self.data)

class RPGArmoury(App):
    pass

def launch():
    RPGArmoury().run()
