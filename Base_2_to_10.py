def Base_2_to_10(S):
	L = len(S)-1
	out = 0
	for i in reversed(range(L+1)):
		if S[i] == "1":
			out += 2 ** (L-i)
	return out
