import numpy as np
import pickle

'''
0 -> up
1 -> down
2 -> left
3 -> right
4 -> still
'''
gamma = 0.9
t = 0
ep = 0.3
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
	for i in range(min(len(ghost),len(ghost1))):
		st += (ghost[i] + (velocity(ghost[i],ghost1[i]),),)
	return st

class env:
	def __init__(self):
		fp = open('memo','rb')
		self.memo = pickle.load(fp)
		fp.close()
		fp = open('state','rb')
		self.state = pickle.load(fp)
		fp.close()
		fp = open('cnt','rb')
		self.cnt = pickle.load(fp)
		fp.close()
		fp = open('act','rb')
		self.act = pickle.load(fp)
		fp.close()
		fp = open('Q','rb')
		self.Q = pickle.load(fp)
		fp.close()
	def write(self):
		fp = open('memo','wb')
		pickle.dump(self.memo,fp)
		fp.close()
		fp = open('state','wb')
		pickle.dump(self.state,fp)
		fp.close()
		fp = open('cnt','wb')
		pickle.dump(self.cnt,fp)
		fp.close()
		fp = open('act','wb')
		pickle.dump(self.act,fp)
		fp.close()
		fp = open('Q','wb')
		pickle.dump(self.Q,fp)
		fp.close()
	def reinit(self):
		self.memo = {}
		fp = open('memo','wb')
		pickle.dump(self.memo,fp)
		fp.close()
		self.state = []
		fp = open('state','wb')
		pickle.dump(self.state,fp)
		fp.close()
		self.cnt = 0
		fp = open('cnt','wb')
		pickle.dump(self.cnt,fp)
		fp.close()
		self.act = []
		fp = open('act','wb')
		pickle.dump(self.act,fp)
		fp.close()
		self.Q = []
		fp = open('Q','wb')
		pickle.dump(self.Q,fp)
		fp.close()

E = env()
A = None
def reward(g,lg,f,over,time,dg,df):
	if over == 1:
		return 1000
	if over == -1:
		return -1000
	rew = 50.0/t
	if time:
		rew += -5*dg + df + 100.0*g
	else:
		rew += 5*lg*dg + -5*f*df
	return rew

def Qlearning(pac,pac1,ghost,ghost1,f,over,dg,df,time):
	st = getState(pac,pac1,ghost,ghost1,f)
	global A
	global t
	if st not in E.memo:
		E.memo[st] = E.cnt
		E.cnt += 1
		E.act.append(np.random.randint(5)) 
		E.Q.append([0.0,0.0,0.0,0.0,0.0])
	s =  E.memo[st]
	a = None
	if A != None:
		alpha = 1.0/(1.0+t)
		s_,a_ = A
		E.Q[s_][a_] = (1-alpha)*E.Q[s_][a_] + alpha*(reward(len(ghost)-len(ghost1),len(ghost),f,over,time,dg,df) + gamma*max(E.Q[s]))
	if np.random.random() < ep :
		a = np.random.randint(5)
	else:
		a = np.argmax(E.Q[s])
	A = (s,a)
	t += 1
	return a

