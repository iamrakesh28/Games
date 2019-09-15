import queue

def cellNum(i,j,m):
	return i*m+j

def cellInv(num,m):
	return (num//m,num%m)

def valid(i,j,n,m):
	if i >= 0 and i < n and j >= 0 and j < m:
		return True
	return False

def BFS(mat,ghost,n,m,pac,f):
	visit = [m*[False] for i in range(n)]
	dist = [m*[0] for i in range(n)]
	par = [m*[0] for i in range(n)]
	dr = [-1,1,0,0]
	dc = [0,0,-1,1]
	for r in range(n):
		for c in range(m):
			if mat[r][c] == '#':
				visit[r][c] = True
	q = queue.Queue()
	q.put(cellNum(pac[0],pac[1],m))
	par[pac[0]][pac[1]] = cellNum(pac[0],pac[1],m)
	visit[pac[0]][pac[1]] = True
	while q.empty() == False:
		p = q.get()
		r,c = cellInv(p,m)
		for d in range(4):
			if valid(dr[d]+r,dc[d]+c,n,m) and visit[dr[d]+r][dc[d]+c] == False:
				visit[dr[d]+r][dc[d]+c] = True
				dist[dr[d]+r][dc[d]+c] = dist[r][c] + 1
				par[dr[d]+r][dc[d]+c] = cellNum(r,c,m)
				q.put(cellNum(dr[d]+r,dc[d]+c,m))
	gh = ()
	for r,c in ghost:
		i,j = cellInv(par[r][c],m)
		if (i,j) in gh:
			gh = gh + ((r,c),)
		else:
			gh = gh + ((i,j),)
	dg = 1e9
	df = 1e9
	for r,c in gh:
		dg = min(dg,dist[r][c])
	for r,c in f:
		df = min(dg,dist[r][c])
	return (gh,dg,df)
