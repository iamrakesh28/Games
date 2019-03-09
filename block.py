import queue
import os
import visual
'''
	col -> column size
	returns cell coordinates
'''
row = 4
col = 4
memo = {}
st = []
def cell(num):
	return (num//col,num%col)

def cellInv(i,j):
	return i*col + j
'''
	|0|1|2|
	|3|4|5|
	|6|7|8|
	(target block,obstacles...)
'''
def matrix(start):
	return (start,2,3)

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
			r,c = cell(p[x])
			if r >= 1:
				val = cellInv(r-1,c)
				state = p[0:x] + (val,) + p[x+1:len(p)]
				if state not in memo and val not in p:
					memo[state] = count
					st.append(state)
					parent.append(cnt)
					q.put(count)
					if(state[0] == end):
						return path(parent,count)
					count += 1
			if r < row-1:
				val = cellInv(r+1,c)
				state = p[0:x] + (val,) + p[x+1:len(p)]
				if state not in memo and val not in p:
					memo[state] = count
					st.append(state)
					parent.append(cnt)
					q.put(count)
					if(state[0] == end):
						return path(parent,count)
					count += 1
			if c >= 1:
				val = cellInv(r,c-1)
				state = p[0:x] + (val,) + p[x+1:len(p)]
				if state not in memo and val not in p:
					memo[state] = count
					st.append(state)
					parent.append(cnt)
					q.put(count)
					if(state[0] == end):
						return path(parent,count)
					count += 1
			if c < col-1:
				val = cellInv(r,c+1)
				state = p[0:x] + (val,) + p[x+1:len(p)]
				if state not in memo and val not in p:
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
	r,c = cell(q[len(q)-1])
	mat[r][c] = 'E'
	r,c = cell(q[0])
	mat[r][c] = 'S'
	for i in range(1,len(q)-1):
		r,c = cell(q[i])
		mat[r][c] = '#'
	visual.display(row,col,mat)
end = 15
os.system('clear')
obs = (0,10,11,13,14)
memo[obs] = 0
st.append(obs)
PrintPath(0,[])
p = solver(obs,end)
if p == []:
	print('No solution')
else:
	for x in p:
		PrintPath(x,p)
