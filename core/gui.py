from kivy.app import App
from kivy.lang import Builder
import kivy.properties as kvprop
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.label import Label
import yaml
import importlib

# To keep the rpgarmoury.kv file pure, any functionality not strictly
# related to UI appearance should be made here.  Most often, this will be
# implementation of custom Widgets that are not simply composite layouts of
# other widgets.

class RPGArmoury(App):
    character = kvprop.ObjectProperty()
    char_dict = kvprop.ObjectProperty()
    current_plugin = kvprop.ObjectProperty()
    plugins = kvprop.DictProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.char_dict = yaml.load(open('characters.yml'))

    def load_plugin(self, name):
        try:
            self.current_plugin = self.plugins[name]
        except KeyError:
            plugin = importlib.import_module('plugins.%s' % name)
            plugin.__name__ = name
            self.plugins[name] = plugin
            self.load_plugin(name)

    def construct_character(self, data):
        plugin_name = data['plugin']
        self.load_plugin(plugin_name)
        data['plugin'] = self.current_plugin
        character = self.current_plugin.construct_character(data)
        return character

    def on_character(self, *args):
        plugin_ui = Builder.load_file('plugins/{0}/{0}.kv'.format(self.current_plugin.__name__))
        self.root.add_widget(plugin_ui)
        self.root.current = plugin_ui.name






## Custom Widgets
class CharacterSelectionPanel(GridLayout):
    lst = kvprop.ObjectProperty()
    def on_lst(self, obj, lst):
        for l in lst:
            self.add_widget(CharacterButton(name=l, data=lst[l]))


class CharacterButton(Button):
    text = kvprop.StringProperty()
    name = kvprop.AliasProperty(text.get, text.set, bind=['text'])
    data = kvprop.DictProperty()






class CoercedStringProperty(kvprop.StringProperty):
    """Coerces the passed value into a string, allowing non-string values
       to be represented easily from within kv file.  Not for direct use;
       rather, should only be used through the Panel class."""
    def __set__(self, obj, val):
        super().__set__(obj, str(val))


class Panel(Label):
    text = CoercedStringProperty()


class Counter(Panel):
    value = kvprop.NumericProperty()


class CappedCounter(Counter):
    value = kvprop.BoundedNumericProperty(0, min=-1, max=1)
    min = kvprop.AliasProperty(value.get_min, value.set_min, bind=['value'])
    max = kvprop.AliasProperty(value.get_max, value.set_max, bind=['value'])


class Guage(CappedCounter):
    def decr(self, *args):
        try:
            self.value -= 1
        except ValueError:
            pass
    def incr(self, *args):
        try:
            self.value += 1
        except ValueError:
            pass


class TreeTable(TreeView):
    # node_cls = kvprop.ObjectProperty(TreeViewLabel)

    def clear_nodes(self):
        for node in self.root.nodes:
            self.remove_node(node)


    def populate(self):
        self.clear_nodes()
        self.construct_tree(self.data, self.root)


    def construct_tree(self, data, root_node):
        try:
            for node in data:
                new_node = self.construct_node(node, data)
                self.construct_tree(node, new_node)
                self.add_node(new_node, root_node)
        except TypeError:
            pass


    def construct_node(self, item, data):
        # return self.node_cls(text=str(data))
        return self.Node(text=str(item))


    class Node(TreeViewLabel):
        pass




Builder.load_file('core/gui_elements.kv', rulesonly=True)
