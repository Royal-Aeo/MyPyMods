class TreeNode:
	def __init__(self,name,data,parent=None):
		self.name = name
		self.parent = parent
		self.data = data
		self.childs = []
	def add_child(self,name,data):
		self.childs.append((type(self))(name,data,self))
	
	def rm_branch(self,ansistors_N,name,level):
		focus = self.childs
		while True:
			if ansistors_N[0] in focus:
				focus = focus[ansistors_N[0]]
		        del ansistors_N[0]
		    elif name in focus and ansistors == None:
		        del focus[name]
		        break

if __name__ == "__main__":
	ins = TreeNode("first","hi")
	ins.add_child("second","hello")
	ins.add_child("second"	,"hee")
	