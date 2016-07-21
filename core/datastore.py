import yaml

class GameDataMeta(yaml.YAMLObjectMetaclass):
    dataclasses = {}
    reserved_tags = set()
    def __init__(cls, name, bases, kwds):
        super().__init__(name, bases, kwds)
        GameDataMeta.dataclasses[name] = cls
        GameDataMeta.reserved_tags |= {cls.yaml_tag}

    def __repr__(cls):
        """Print format:  ClassName(arg1=val1, arg2=val2, ... argn=valn)"""
        return "%s(%s)" % (cls.__name__ , ', '.join("%s=%s" % (k,v)
                for k,v in cls.__dict__.items() if k[:1] != '_'))



class GameDataType(yaml.YAMLObject, metaclass=GameDataMeta):
    yaml_tag = '!Data'

    @classmethod
    def from_yaml(cls, loader, node):
        data = loader.construct_mapping(node, deep=True, add_type=False)
        # print(node)
        return node

class RPGLoader(yaml.Loader):
    def construct_object(self, node, deep=False, add_type=True, parent=object):
        if node.tag == GameDataType.yaml_tag:
            #TODO necessarily construct_mapping?
            return self.construct_mapping(node, deep, add_type, parent)
        return super().construct_object(node, deep)



# Stand-in for the funcitonaltiy I eventually hope to implement through a
# specialization of the the standard YAML Loader class.  For now, though,
# this group of recursive functions does what I want.
def load(stream):
    l = yaml.Loader(stream)
    return load_node(l.get_single_node(), l)

def load_node(node, loader, parent=GameDataType):
    if isinstance(node, yaml.SequenceNode):
        return [load_node(v, loader) for v in node.value]
    elif isinstance(node, yaml.MappingNode):
        return dict([load_node_tuple(t, loader, parent) for t in node.value])
    else:
        return loader.construct_object(node)

def load_node_tuple(tpl, loader, parent):
    k, v = tpl
    # print("%s : %s" % tpl)
    try:
        if v.tag != GameDataType.yaml_tag:
            # print(v.tag)
            key = load_node(k, loader)
            if parent is not None:
                parent = type(key, (parent,), {})
            val = load_node(v, loader, parent)
            return (key, val)
        else:
            name = load_node(k, loader, None)
            data = load_node(v, loader, None)
            return (name, type(name, (parent,), data))
    except TypeError:
        print(tpl)
        raise












### Scratch space for implementing Loader with same functionality
  # as above load functions



# class GameType(yaml.YAMLObject, metaclass=GameDataMeta):
#     # yaml_tag = yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG
#     yaml_tag = '!Type'

#     # @classmethod
#     # def from_yaml(cls, loader, node):
#     #     name = loader.construct_scalar(node)
#     #     type(name, (cls,), {})
#     #     return name
#         # result = {}
#         # for keynode,valnode in node.value:
#         #     key = loader.construct_object(keynode)
#         #     val = loader.construct_object(valnode)
#         #     # print("%s : %s" % (key, val))
#         #     if valnode.tag in GameDataMeta.reserved_tags:
#         #         print("type(%s, (%s,), %s)" % (key, cls, val))
#         #         val = type(key, (cls,), val)
#         #     # else:
#         #     #     type(key, (cls,), {})
#         #     result[key] = val
#         # return result

#     def construct_mapping(self, node, deep=False, add_type=True, parent=object):
#         data = {}
#         for k,v in node.value:
#             key = self.construct_object(k)
#             if add_type:
#                 t = GameType(key, (parent,), {})
#             # if v.tag == GameDataType.yaml_tag:
#             #     val = self.construct_gamedata(v)
#             # else:
#                 # val = self.construct_object(v)
#             val = self.construct_object(v)
#             data[key] = val
#         return data


#     def construct_gamedata(self, node, name, parent):
#         data = self.construct_object(node, add_type=False)
#         return GameDataType(name, (parent,), data)
