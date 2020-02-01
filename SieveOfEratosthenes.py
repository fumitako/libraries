import numpy as np
limit = 10**5
def Eratosthenes(limit):
	is_prime = np.full(limit+1, True)
	is_prime[:2] = False
	for p in range(2,limit+1):
		if p**2 > limit:
			break
		if is_prime[p]:
			is_prime[p**2::p] = False

	return np.arange(limit+1)[is_prime]
