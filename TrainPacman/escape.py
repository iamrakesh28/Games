def valid(i,j,n,m):
	if i >= 1 and i < n-1 and j >= 1 and j < m-1:
		return True
	return False

def euclid(i,j,r,c):
	return (i-r)**2 + (j-c)**2
def esc(mat,pac,n,m,ghost):
	gh = ()
	dr = [-1,1,0,0,0]
	dc = [0,0,-1,1,0]
	for r,c in ghost:
		dist = []
		for d in range(5):
			if valid(dr[d]+r,dc[d]+c,n,m) and mat[dr[d]+r][dc[d]+c] != '#' and (dr[d]+r,dc[d]+c) not in gh:
				dist += [(euclid(pac[0],pac[1],dr[d]+r,dc[d]+c),dr[d]+r,dc[d]+c)]
		dist.sort()	
		gh += ((dist[-1][1],dist[-1][2]),)
	return gh
