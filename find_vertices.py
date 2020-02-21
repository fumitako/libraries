def find_vertices(x,y):
	ind_x_r = np.searchsorted(XY[:,0], x)
	ind_x_l = np.searchsorted(XY[:,0], x, side='right')
	if ind_x_r == ind_x_l:
		return 0
	for i in range(ind_x_r, ind_x_l):
		if XY[i,1] == y:
			return 1
