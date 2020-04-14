def eratosthenes(N):
	is_prime = [True] * (N + 1)
	is_prime[0], is_prime[1] = False, False
	for i in range(2, int(N**(1/2)) + 1):
		if is_prime[i]:
			for j in range(i * 2, N + 1, i):
				is_prime[j] = False
	return [i for i in range(N+1) if is_prime[i]]
