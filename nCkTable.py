import numpy as np
MOD = 10**9+7
def cumprod(x, MOD = MOD):
	L = len(x)
	Lsq = int(L**.5 + 1)
	x = np.resize(x, Lsq ** 2).reshape(Lsq, Lsq)
	for n in range(1, Lsq):
		x[:,n] *= x[:,n-1]
		x[:,n] %= MOD
	for n in range(1,Lsq):
		x[n] *= x[n-1, -1]
		x[n] %= MOD
	return x.flatten()[:L]

def make_fact(U, MOD = MOD):
	x = np.arange(U, dtype = np.int64)
	x[0] = 1
	fact = cumprod(x, MOD)
	x = np.arange(U, 0, -1, dtype = np.int64)
	x[0] = pow(int(fact[-1]), MOD - 2, MOD)
	fact_inv = cumprod(x, MOD)[::-1]
	return fact, fact_inv
