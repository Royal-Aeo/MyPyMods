class TreeNode:
    def __init__(self, name, data, parent=None):
        self.name = name
        self.parent = parent
        self.data = data
        self.childs = {}

    def add_child(self, name, data):
        self.childs.update({name:(type(self))(name, data, self)})

    def rm_branch(self, name, ansistors_n: list = None,):
        focus = self.childs
        while True:
            if ansistors_n == None or ansistors_n == self.name:
                del focus[name]
                break
            elif ansistors_n[0] in focus:
                focus = (focus[ansistors_n[0]]).childs
                del ansistors_n[0]
            elif name in focus and ansistors_n is None:
                del focus[name]
                break
            else:
                print(focus)
                raise NameError(f"couldn't find branch {ansistors_n[0]}")
    def __getitem__(self, item):
        return self.childs[item]

    def __setitem__(self, key, value):
        self.childs[key] = value

    def __delitem__(self, key, ansistors_n: list = None):
        self.rm_branch(key, ansistors_n)

