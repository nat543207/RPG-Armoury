from kivy.app import App
from kivy.lang import Builder
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.listadapter import ListAdapter


class Table(ListView):
    def __init__(self, **kwargs):
        super(Table, self).__init__(**kwargs)
        self.data = []
        self.adapter = ListAdapter(data=self.data, cls=ListItemButton)
    pass

class RPGArmoury(App):
    kv_directory = '../kv'


if __name__ == '__main__':
    RPGArmoury().run()
