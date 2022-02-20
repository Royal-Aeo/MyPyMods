# Node class (link list)
class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

# Link list class (main class)
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

    def remove_by_index(self, index:int):
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
        while itr!=None:
            hold.next = prev
            prev = hold
            if hold_next != None:
                hold = hold_next
                hold_next = hold_next.next
            else:
                break
        self.top = prev

# Node2 class (Double-link list)
class node2:
    def __init__(self,prev,data,next):
        self.prev = prev
        self.data = data
        self.next = next

# DoubleLList
class DoubleLList:
    def __init__(self):
        self.top = None
        self.tail = None

    def append(self,data):
        if self.top == None:
            self.top = node2(None,data,self.top)
            self.tail = self.top
        else:
            self.tail.next = node2(self.tail,data,None)
            self.tail = self.tail.next

    def remove_by_index(self,index:int):
        if index < 0:
            index = (abs(index))-1
            itr = self.tail
            count = 0
            prev = None
            while itr!=None:
                if count == index:
                    if prev!=None:
                        prev.prev = itr.next
                    itr.prev.next = prev
                prev = itr
                count+=1
                itr = itr.prev
        elif index == 0:
            self.top = self.top.next
        elif index > 0:
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

    def remove(self,element):
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

    def show_list(self):
        itr = self.top
        while itr!=None:
            yield itr.data
            itr = itr.next

    def reverse(self):
        prev = None
        hold = self.top
        itr = hold
        while itr is not None:
            prev = hold.prev
            hold.prev = hold.next
            hold.next = prev
            itr = itr.prev
        if prev is not None:
            self.top = prev.prev
