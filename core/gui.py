from kivy.app import App
import kivy.properties as kvprop
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeView, TreeViewNode, TreeViewLabel
from kivy.uix.label import Label
# To keep the rpgarmoury.kv file pure, any functionality not strictly
# related to UI appearance should be made here.  Most often, this will be
# implementation of custom Widgets that are not simply composite layouts of
# other widgets.

class RPGArmoury(App):
    player = kvprop.ObjectProperty()
    def __init__(self, player, **kwargs):
        super().__init__(**kwargs)
        self.player = player
class GUI_Elements(App):
    player = kvprop.ObjectProperty()
def launch(character):
    RPGArmoury(character).run()





class CoercedStringProperty(kvprop.StringProperty):
    """Coerces the passed value into a string, allowing non-string values
       to be represented easily from within kv file.  Not for direct use;
       rather, should only be used through the Panel class."""
    def __set__(self, obj, val):
        super().__set__(obj, str(val))

class Panel(Button):
    text = CoercedStringProperty()
    background_color = kvprop.ListProperty([0, 0, 0, 0])



class Tracker(Panel):
    value = kvprop.NumericProperty()

class Guage(Tracker):
    max = kvprop.NumericProperty(1)
    def decr(self, *args):
        self.value -= 1

class TreeTableView(TreeView):
    columns = kvprop.ListProperty()
    data = kvprop.ListProperty()
    hide_root = kvprop.BooleanProperty(True)
    current_item = kvprop.ObjectProperty()

    class Row(TreeViewLabel):
        text = CoercedStringProperty()
        def on_is_selected(self, node, selected):
            if(selected):
                pass

    def clear_nodes(self):
        for node in self.root.nodes:
            self.remove_node(node)

    def populate(self):
        self.clear_nodes()
        for item in self.data:
            self.add_node(self.construct_node(item))

    def construct_node(self, data, deep=True):
        node = TreeTableView.Row(text=data)
        if deep:
            try:
                for subdata in data:
                    self.add_node(self.construct_node(subdata), node)
            except TypeError:
                pass
        return node

    def on_data(self, *args):
        self.populate()


























class TreeLayout(TreeView):
    class Node(BoxLayout, TreeViewNode):
        def __init__(self, **kwargs):
            BoxLayout.__init__(self, **kwargs)
            TreeViewNode.__init__(self, **kwargs)
            self.add_widget(Panel(text='Hi'))
            self.add_widget(Panel(text='Bye'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_node(TreeLayout.Node())
        self.add_node(TreeLayout.Node())

