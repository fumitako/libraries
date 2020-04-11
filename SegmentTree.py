#単位元を設定
ide = float('inf')

class SegmentTree:
	def __init__(self,n):
        #セグ木の頂点はindex == 1から。index == 0は無視すること。
        #つまり、STtable[0]は無視。頂点はSTtable[1]。
		self.n = n
		tmp = 0
		while True:
			if 2 ** tmp >= self.n:
				break
			tmp += 1
		self.STtable = [ide] * (2*2**tmp)
		self.STtable_size = len(self.STtable)

	def update(self,i,a):
        #更新のためのインデックスの指定は0_indexedで。
		i += self.STtable_size//2
		self.STtable[i] = a
		while i > 0:
			i //= 2
			self.STtable[i] = min(self.STtable[i*2], self.STtable[i*2+1])

	def find(self,a,b,k=1,l=0,r=None):
        #kは頂点番号。初期値は1にすること。
		#[a,b)の最小を返す。
		#[l,r)からです。
        #初期値のrは、self.STtable_size//2にすると、ちょうど要素数と同じ値になって[l,r)のrになる。
        #問題に適するように範囲を指定するように注意。大体[l,r]で指定されている。
		if r == None:
			r = self.STtable_size//2        
		if a >= r or b <= l:
			return ide
		elif a <= l and b >= r:
			return self.STtable[k]
		else:
			v1 = self.find(a,b,2*k,l,(l+r)/2)
			v2 = self.find(a,b,2*k+1,(l+r)/2,r)
			return min(v1,v2)

n,q = map(int, input().split())
solve = SegmentTree(n)
ans = []
for _ in range(q):
	cond, x, y = map(int, input().split())
	if cond == 0:
		solve.update(x,y)
	else:
		ans.append(solve.find(x,y+1))

for a in ans:
	if a == ide:
		print(2147483647)
	else:
		print(a)
