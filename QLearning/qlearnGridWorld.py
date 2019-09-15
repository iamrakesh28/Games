import numpy as np
import matplotlib.pyplot as plt

'''
0 -> up
1 -> down
2 -> left
3 -> right
'''
dr = [-1,1,0,0]
dc = [0,0,-1,1]
gamma = 0.9
ep = 0.2
INF = -1e9
Q = None
def read(s):
	file1 = open(s,'r')
	data = file1.readlines()
	i = 0 
	arr = []
	for line in data:
		word = line.split()
		arr.append([])
		for w in word:
			arr[i].append(w)
		i += 1
	return arr


def printMat(mat):
	for r in mat:
		s = ''
		for c in r:
			s += ' ' + str(c)
		print(s)

def valid(i,j,n,m):
	if i >= 0 and j >= 0 and i < n and j < m:
		return True
	return False
class env:
	def __init__(self,p):
		self.mat = read('input')
		self.rew = read('reward')
		self.p = p
		self.n = n = len(self.rew)
		self.m = m = len(self.rew[0])
		for i in range(n):
			for j in range(m):
				self.rew[i][j] = float(self.rew[i][j])
	def nextState(self,i,j,a):
		prob = []
		for d in range(4):
			if d != a:
				prob += [(1-self.p)/3.0]
			else :
				prob += [self.p]
		return np.random.choice(4,1,p=prob)[0]
		
E = env(0.7)
def greedy(i,j):
	d = None
	st = None
	if np.random.random() < ep:
		d = np.random.randint(4)
		st = d
	else:
		d = np.argmax(Q[i][j])
		st = E.nextState(i,j,d)
	if valid(i+dr[st],j+dc[st],E.n,E.m) == False or E.mat[i+dr[st]][j+dc[st]] == '#':
		return (i,j,d)
	return (i+dr[st],j+dc[st],d)

def Bellman(t):
	n = len(Q)
	m = len(Q[0])
	alpha = (1.0/(1.0+t))
	for i in range(n):
		for j in range(m):
			r,c = (i,j)
			while E.mat[r][c] != 'g' and E.mat[r][c] != '#':
				si,sj,a = greedy(r,c)
				maxR = max(Q[si][sj])
				val = (1.0-alpha)*Q[r][c][a]
				val += alpha*(E.rew[r][c] + gamma*maxR)
				Q[r][c][a] =  val
				#print(Q[1][1],r,c,a,Q[r][c])
				r,c = (si,sj)
			#if E.mat[r][c] == 'g':
			#	for d in range(4):
			#		Q[r][c][d] = E.rew[r][c]
	return
def valueIter(num):
	for i in range(num):
		Bellman(i)
	n = len(Q)
	m = len(Q[0])
	V = [ m*[-1] for r in range(n)]
	act = [ m*[-1] for r in range(n)]
	#print(Q[1][1])
	for i in range(n):
		for j in range(m):
			V[i][j] = max(Q[i][j])
			act[i][j] = np.argmax(Q[i][j])
	return (V,act)
Q = [ E.m*[[0.0,0.0,0.0,0.0]] for r in range(E.n)]
Q = np.array(Q)
V,act = valueIter(20)
printMat(act)
V = np.array(V)
plt.imshow(V)
plt.show()
