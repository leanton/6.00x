class Queue (object):
	def __init__(self):
		self.vals = []

	def insert(self, e):
		return self.vals.append(e)

	def remove(self):
		try:
			q = self.vals[0]
			self.vals = self.vals[1:]
			return q
		except:
			raise ValueError

s1 = Queue()
s1.insert(1)
s1.insert(23)
s1.insert(24)
s1.insert(14)
s1.remove()
s1.remove()
s1.remove()
s1.remove()