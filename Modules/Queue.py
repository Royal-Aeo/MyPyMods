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

if __name__ == '__main__':
	ie = queue()
	for i in range(1,200):
	   ie.enque(i)
	print(ie.show())