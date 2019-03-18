import queue
import os
import visual

row = 5
col = 5
memo = {}
st = []
dy = [-1,0,0,+1]
dx = [0,-1,1,0]

def cell(num):
	return (num//col,num%col)

def cellInv(i,j):
	return i*col + j

def isPossible(i,j):
	return (i >= 0 and j >= 0 and i < row and j < col)

def isValid(p,val,i):
	for x,y in p:
		if (x,y) != i :
			if val[0] in (x,y) or val[1] in (x,y):
				return False
	return True

def path(par,cur):
	p = []
	while cur != 0:
		p.append(cur)
		cur = par[cur]
	p.append(0)
	p.reverse()
	return p

def solver(start,end):
	count = 1
	q = queue.Queue()
	q.put(0)
	parent = []
	parent.append(0)
	if(start[0] == end):
		return True
	while(q.empty() == False):
		cnt = q.get()
		p = st[cnt]
		for x in range(0,len(p)):
			L,U = p[x]
			r1,c1 = cell(U)
			r2,c2 = cell(L)
			for d in range(4):
				if isPossible(r1+dy[d],c1+dx[d]) and isPossible(r2+dy[d],c2+dx[d]):
					L = cellInv(r2+dy[d],c2+dx[d])
					U = cellInv(r1+dy[d],c1+dx[d])
					state = p[0:x] + ((L,U),) + p[x+1:len(p)]
					if state not in memo and isValid(p,(L,U),p[x]):
						memo[state] = count
						st.append(state)
						parent.append(cnt)
						q.put(count)
						if(state[0] == end):
							return path(parent,count)
						count += 1
	return []

def PrintPath(x,p):
	q = st[x]
	q = q + (end,)
	mat = [col*['.'] for r in range(row)]
	L,U = q[len(q)-1]
	r1,c1 = cell(U)
	r2,c2 = cell(L)
	mat[r1][c1] = mat[r2][c2] = 'E'
	L,U = q[0]
	r1,c1 = cell(U)
	r2,c2 = cell(L)
	mat[r1][c1] = mat[r1][c2] = 'S'
	for i in range(1,len(q)-1):
		L,U = q[i]
		r1,c1 = cell(U)
		r2,c2 = cell(L)
		mat[r1][c1] = mat[r2][c2] = '#'
	visual.display(row,col,mat)
end = (23,24)
os.system('clear')
obs = ((0,1),(7,8),(16,17),(13,18),(15,20),(3,4),(5,10))
#obs = ((0,1),(2,3),(5,6),(7,8),(9,4),(10,11),(15,20),(16,17),(13,18),(21,22),(14,19))
memo[obs] = 0
st.append(obs)
PrintPath(0,[])
print('Solving...')
p = solver(obs,end)
if p == []:
	print('No solution')
else:
	os.system('clear')
	for x in p:
		PrintPath(x,p)
