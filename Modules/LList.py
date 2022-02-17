# Node class
class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


# Link list class (main class)
class llist:
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

    def remove_by_index(self, index):
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
    def

if __name__ == "__main__":
    ll = llist()
    ll.append(2)
    ll.append(6)
    print(list(ll.show_list()))
    ll.insert(4, 1)
    ll.insert("nothing", 0)
    print(list(ll.show_list()))
    ll.remove("nothing")
    print(list(ll.show_list()))
