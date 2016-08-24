import core.gui as gui

class InventoryTable(gui.TreeTable):
    def construct_node(self, item, data):
        class ItemNode(gui.TreeViewLabel):
            data = gui.kvprop.ObjectProperty()
            def __str__(self):
                return str(self.data)
            def __repr__(self):
                return repr(self.data)
        return ItemNode(data=item, text=str(item))
