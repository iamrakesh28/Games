import queue

def cellNum(i, j, m):
	return i * m + j

def cellInv(num, m):
	return (num // m,num % m)

def valid(i, j, n, m):
	if i >= 0 and i < n and j >= 0 and j < m:
		return True
	return False

def BFS(mat, ghost, n, m, pac):
	visit = [m * [False] for i in range(n)]
	dist = [m * [-1] for i in range(n)]
	dr = [-1, 1, 0, 0, 0]
	dc = [0, 0, -1, 1, 0]
	for r in range(n):
		for c in range(m):
			if mat[r][c] == '#':
				visit[r][c] = True
	q = queue.Queue()
	q.put(cellNum(pac[0], pac[1], m))
	dist[pac[0]][pac[1]] = 0
	visit[pac[0]][pac[1]] = True
	while q.empty() == False:
		p = q.get()
		r, c = cellInv(p,m)
		for d in range(4):
			if valid(dr[d] + r,dc[d] + c, n, m) and visit[dr[d] + r][dc[d] + c] == False:
				visit[dr[d] + r][dc[d] + c] = True
				dist[dr[d] + r][dc[d] + c] = dist[r][c] + 1;
				q.put(cellNum(dr[d] + r,dc[d] + c, m))
	gh = ()
	for r,c in ghost:
		ds = []
		if dist[r][c] == -1 :
			gh += ((r, c), )
			continue
		for d in range(5):
			ds += [(dist[r + dr[d]][c + dc[d]], r + dr[d], c + dc[d])]
		ds.sort()
		ds.reverse()
		found = 0
		for x in ds:
			i, j = (x[1], x[2])
			if (i, j) not in gh:
				gh = gh + ((i, j), )
				found = 1
				break
		if found == 0:
			gh = gh + ((r, c), )
	return gh
