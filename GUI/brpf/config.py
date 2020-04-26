
class DictConfig(dict):

    def __init__(self, *args, **kwargs):
        super(DictConfig, self).__init__()
        self.update(args[0])

    def update(self, item, **kwargs):
        for k, v in item.items():
            if isinstance(v, dict):
                self[k] = DictConfig(v)
            else:
                self[k] = v

    def __getitem__(self, item):
        paths = item.split("/")
        if len(paths) > 1:
            child = self.get(paths[0])
            child_path = "/".join(paths[1:])
            return child.__getitem__(child_path)
        else:
            return self.get(paths[0])


class ListConfig(list):

    def __init__(self, args):
        super(ListConfig, self).__init__()
        self.append(args)

    def append(self, obj):
        for o in obj:
            if isinstance(o, list):
                self.append(ListConfig(o))
            elif isinstance(o, dict):
                super(ListConfig, self).append(DictConfig(o))
            else:
                super(ListConfig, self).append(o)


if __name__ == "__main__":

    a = {"XML": {"List_of_Browses": [{"Browse": {"Id": 0}}, {"Browse": {"Id": 1}}], "Format": "KMZ"}}
    d = DictConfig(a)
    item = d['XML/List_of_Browses']

    l = ListConfig([{"Browse_Id": 0}, 2, 3])

    pass