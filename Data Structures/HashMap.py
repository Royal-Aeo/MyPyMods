
# Hash table

class h_table:
    def __init__(self) -> None:
        self.max = 100
        self.a_space = [None for i in range(1, self.max+1)]

    def get_hash(self, val: str):
        c = 0
        for i in val:
            c += ord(i)
        return c % self.max

    def setval(self, key, val):
        pos = self.get_hash(key)
        while True:
            if pos > self.max-1:
                pos = pos - self.max-1
            else:
                break
        count = 0
        while True:
            while True:
                if pos > self.max-1:
                    pos = pos - self.max-1
                else:
                    break
            if self.a_space[pos] != None:
                pos += 1
                count += 1
                if count == self.max+1:
                    raise   Exception("H table is full!")
            elif self.a_space[pos] == None:
                self.a_space[pos] = [key,val]
                break

    def __getitem__(self, item):
        if type(item) == int and item <= self.max-1:
            return self.a_space[item]
        elif type(item) == str and item in self.a_space:
            for i in self.a_space:
                if i[0] == item:
                    return i[1]
                break
            raise NameError(f"item '{item}' not in Hash table")