# Node class (link list)
class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

# Link list class (for hash table)


class LList:
    def __init__(self):
        self.top = None

    def append(self, data):
        if self.top == None:
            self.top = node(data, None)
        else:
            itr = self.top
            while itr != None:
                global prev
                prev = itr
                itr = itr.next
            prev.next = node(data, None)

    def insert(self, data, index):
        itr = self.top
        count = 0
        prev = None
        while itr != None:
            if index == 0:
                self.top = node(data, itr)
                break
            elif count == index:
                e = itr
                prev.next = node(data, e)
                break
            count += 1
            prev = itr
            itr = itr.next

    def show_list(self):
        itr = self.top
        while itr != None:
            yield itr.data
            itr = itr.next

    def remove(self, element):
        itr = self.top
        prev = None
        while itr != None:
            if element == self.top.data:
                self.top = itr.next
            elif itr.data == element:
                prev.next = itr.next
                break
            prev = itr
            itr = itr.next

    def remove_by_index(self, index: int):
        itr = self.top
        count = 0
        prev = None
        while itr != None:
            if index == 0:
                self.head = itr.next
            elif count == index:
                prev.next = itr.next
            prev = itr
            count += 1
            itr = itr.next

    def reverse(self):
        prev = None
        hold = self.top
        hold_next = self.top.next
        itr = self.top
        while itr != None:
            hold.next = prev
            prev = hold
            if hold_next != None:
                hold = hold_next
                hold_next = hold_next.next
            else:
                break
        self.top = prev

    def __setitem__(self, index, new_data):
        itr = self.top
        count = 0
        prev = None
        while itr != None:
            if index == 0:
                self.top = node(new_data, itr)
                break
            elif count == index:
                e = itr
                prev.next = node(new_data, e)
                break
            count += 1
            prev = itr
            itr = itr.next

    def __delitem__(self, index):
        count = 0
        itr = self.top
        prev = None
        while itr != None:
            if index == 0:
                self.top = itr.next
            elif index == count:
                prev.next = itr.next
                break
            prev = itr
            itr = itr.next
            count += 1

    def __getitem__(self, index):
        count = 0
        itr = self.top
        while itr != None:
            if index == count:
                return itr.data
            count += 1
            itr = itr.next

# Hash table


class h_table:
    def __init__(self) -> None:
        self.max = 1000
        self.a_space = [LList() for i in range(1, self.max)]

    def get_hash(self, val: str):
        c = 0
        for i in val:
            c += ord(i)
        return c % self.max

    def setval(self, key, val):
        (self.a_space[self.get_hash(key)]).append([key, val])

    def get_t(self, key):
        for i in (self.a_space[self.get_hash(key)]).show_list():
            if key == i[0]:
                return i[1]
