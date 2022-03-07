class queue:

	def __init__(self):
		self.main = []
		self.max_c = 10

	def deque(self):
		del self.main[-1]

	def enque(self,val):
		if len(self.main) == self.max_c:
			self.deque()
			self.main.insert(0,val)
		else:
			self.main.insert(0,val)

	def show(self):
		return self.main
	
	def __getitem__(self,index):
		return self.main[index]
	
	def __setitem__(self,*args):
		raise AssertionError("Queue doesn't supports its assertion")
	
	def __delitem__(self,index):
		del self.main[index]