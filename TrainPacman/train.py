import numpy as np
import pacmanBFS

'''
0 -> up
1 -> down
2 -> left
3 -> right
4 -> still
'''
gamma = 0.9
t = 0
def velocity(v2,v1):
	dv = (v2[0]-v1[0],v2[1],v1[1])
	if dv[0] != 0:
		if dv[0] == 1:
			return 1
		return 0
	elif dv[1] != 0:
		if dv[1] == 1:
			return 3
		return 2
	return 4
def getState(pac,pac1,ghost,ghost1,f):
	st = (pac + (velocity(pac,pac1),),)
	st += ((f,),)
	for i in range(len(ghost)):
		st += (ghost[i] + (velocity(ghost[i],ghost1[i]),),)
	return st

class env:
	def __init__(self):
		self.memo = {}
		self.state = []
		self.cnt = 0
		self.act = []
		self.Q = []

E = env()
A = None
def reward(g,f,over):
	if over == 1:
		return 500
	if over == -1:
		return -500
	rew = 25.0/(g+1) + 10.0/(f+1) + 50.0/t
	return rew

def Qlearning(pac,pac1,ghost,ghost1,f,over):
	st = getState(pac,pac1,ghost,ghost1,f)
	if st not in E.memo:
		E.memo[st] = E.cnt
		E.cnt += 1
		E.act.append(np.random.randint(5)) 
		E.Q.append([0.0,0.0,0.0,0.0,0.0])
	s =  E.memo[st]
	if A != None:
		alpha = 1.0/(1.0+t)
		s_,a_ = A
		E.Q[s_][a_] = (1-alpha)*E.Q[s_][a_] + alpha*(reward(len(ghost),f,over) + gamma*max(E.Q[s]))
	a = np.argmax(E.Q[s])
	A = (s,a)
	t += 1
	return a

