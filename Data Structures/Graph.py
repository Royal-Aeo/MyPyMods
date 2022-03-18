# Graph Node
class GNode:

    def __init__(self, data):
        self.data = data
        self.bond = set()

    def add_bond(self, data):
        if data == self.data:
            return
        i = GNode(data)
        self.bond.add(i)
        i.bond.add(self)

    def del_bond(self,bond_data):
        for i in self.bond:
            if i.data == bond_data:
                self.bond.remove(i)
                i.bond.remove(self)

    def show_bonds_data(self):
        l = []
        for i in self.bond:
            l.append(i.data)
        return l

    def show_all_vals(self):
        collect = {self.data}
        focus = self.bond
        focus1 = set()
        while focus != set():
            for i in focus:
                if i.data not in collect:
                    collect.update({i.data})
                    focus1.update(i.bond)
            focus = focus1
            focus1 = set()
        return collect

    def safe_drop(self,data):
        focus = self.bond
        done = False
        e_var = set()
        focus2 = set()
        while done != True:
            for i in focus:
                if i.data == data:
                    for ie in i.bond:
                        e_var.update({ie})
                    for w in e_var:
                        if len(w.bond) > 1:
                            for ee in e_var:
                                if w == ee: pass
                                w.bond.update({ee})
                                ee.bond.update({w})
                            break
                    done = True
                    for ie in i.bond:
                        ie.bond.remove(i)
                    break
                focus2.update(i.bond)
            focus = focus2
            focus2 = set()

    def __getitem__(self,data):
        for i in self.bond:
            if i.data == data:
                return i

    def __setitem__(self,key_data,var):
        focus = self.bond
        done = False
        focus2 = set()
        while done != True:
            for i in focus:
                if i.data == key_data:
                    for ie in i.bond:
                        ie.bond.remove(i)
                        ie.bond.update({var})
                        var.bond.update({ie})
                    done = True
                    break
                focus2.update(i.bond)
            focus = focus2
            focus2 = set()

    def __delitem__(self,data):
        focus = self.bond
        done = False
        focus2 = set()
        while done != True:
            for i in focus:
                if i.data == data:
                    for ie in i.bond:
                        ie.bond.remove(i)
                    done = True
                    break
                focus2.update(i.bond)
            focus = focus2
            focus2 = set()