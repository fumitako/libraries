#単位元を設定
ide = float('inf')

class SegmentTree:
	def __init__(self,n):
		self.n = n
		tmp = 0
		while True:
			if 2 ** tmp >= self.n:
				break
			tmp += 1
		self.STtable = [ide] * (2*2**tmp)
		self.STtable_size = len(self.STtable)

	def update(self,i,a):
		i += self.STtable_size//2
		self.STtable[i] = a
		while i > 0:
			i //= 2
			self.STtable[i] = min(self.STtable[i*2], self.STtable[i*2+1])

	def find(self,a,b,k,l,r):
		#[a,b)の最小を返す。
		#[l,r)からです。
		if a >= r or b <= l:
			return ide
		elif a <= l and b >= r:
			return self.STtable[k]
		else:
			v1 = self.find(a,b,2*k,l,(l+r)/2)
			v2 = self.find(a,b,2*k+1,(l+r)/2,r)
			return min(v1,v2)
