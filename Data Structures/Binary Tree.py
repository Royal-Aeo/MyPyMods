class BTreeNode:
    def __init__(self,data,parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def add_child(self,data):
        if data  <  self.data:
            if self.left == None:
                self.left = (type(self))(data,self)
            elif self.left != None:
                self.left.add_child(data)
        elif data  >  self.data:
            if self.right == None:
                self.right = (type(self))(data,self)
            elif self.right != None:
                self.right.add_child(data)
        
    def show(self):
        focus = [self.left,self.right]
        focus_2 =  []
        elem = [self.data]
        while True:
            if focus == []:
                break
            for i in focus:
                if i == None:
                    continue
                focus_2.append(i.left)
                focus_2.append(i.right)
                elem.append(i.data)
            focus = focus_2
            focus_2 = []
        return elem


    def delchild(self, pos):
        if pos == "left":
            self.left = None
        elif pos == "right":
            self.right = None
        else:
            raise NameError(f"Please us 'left'/'right' not {pos}")
    
    def safe_del(self,pos):
        if pos == "left" and (self.left.left != None or self.left.right != None):
            max = self.left
            focus = self.left
            while focus != None and focus.right != None:
                if focus.data < focus.right.data:
                    max = focus.right
                focus = focus.right
        
            max.left,max.right,max.parent = self,self,self
            self.left = max