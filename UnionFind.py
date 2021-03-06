class UnionFind:
	def __init__(self, n):
		self.n = n
		self.root = [-1]*(n+1)
		self.rnk = [0]*(n+1)
		self.Maxroot = -1

	def Find_Root(self, x):
		if (self.root[x] < 0):
			return x
		else:
			self.root[x] = self.Find_Root(self.root[x])
			return self.root[x]

	def Unite(self, x, y):
		x = self.Find_Root(x)
		y = self.Find_Root(y)
		if x == y:
			return 
		elif self.rnk[x] > self.rnk[y]:
			self.root[x] += self.root[y]
			if self.root[x] < self.Maxroot:
				self.Maxroot = self.root[x]
			self.root[y] = x
		else:
			self.root[y] += self.root[x]
			if self.root[y] < self.Maxroot:
				self.Maxroot = self.root[y]
			self.root[x] = y
			if self.rnk[x] == self.rnk[y]:
				self.rnk[y] += 1

	def isSameGroup(self, x, y):
		return self.Find_Root(x) == self.Find_Root(y)

	def Count(self, x):
		return self.root[self.Find_Root(x)] * (-1)
