class stack:

	def __init__(self):
		self.main = []

	def pop(self):
		return self.main.pop(0)

	def push(self,val):
		self.main.insert(0,val)

	def show(self,val=None):
		if val == None:
			return self.main
		elif type(val) == int:
			return self.main[val]
	
	def __getitem__(self,index):
		return self.main[index]
	
	def __setitem__(self,*args):
		raise AssertionError("stack doesn't supports its assertion")
	
	def __delitem__(self):
		raise IndexError("stack elements doesn't supports these feature")
		
s = stack()
for i in range(1,11):
	s.push(i)
print(s.show())
print(s.pop(),"\n",s.show())
print(s.show(3))