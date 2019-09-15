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
ep = 0.1
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
def getState(pac,pac1,ghost,ghost1,f,time):
	st = (pac + (velocity(pac,pac1),),)
	st += (f,)
	for i in range(min(len(ghost),len(ghost1))):
		st += (ghost[i] + (velocity(ghost[i],ghost1[i]),),)
	if time:
		st += (1,)
	else:
		st += (0,)
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
		fp = open('t','rb')
		self.t = pickle.load(fp)
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
		fp = open('t','wb')
		pickle.dump(self.t,fp)
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
		self.t = 0
		fp = open('t','wb')
		pickle.dump(self.t,fp)
		fp.close()

E = env()
A = None
r = None
def reward(g,lg,f,over,time,dg,df):
	if over == 1:
		return 10000
	if over == -1:
		return -10000
	t = E.t
	rew = 500.0/t
	inv = max(0.5,abs(2-dg))
	if time:
		rew += -100.0*lg*dg + df + 500.0*g
	else:
		rew += 100.0*lg*inv + 200.0*f - 100.0*df
	return 0

def Qlearning(pac,pac1,ghost,ghost1,lf,f,over,dg,df,time):
	st = getState(pac,pac1,ghost,ghost1,f,time)
	global A
	global r
	if st not in E.memo:
		E.memo[st] = E.cnt
		E.cnt += 1
		E.act.append(np.random.randint(4)) 
		E.Q.append([0.0,0.0,0.0,0.0])
	s =  E.memo[st]
	a = None
	t = E.t
	if A != None:
		alpha = 1.0/(1.0+t)
		s_,a_ = A
		E.Q[s_][a_] = (1-alpha)*E.Q[s_][a_] + alpha*(r + gamma*max(E.Q[s]))
	if np.random.random() < ep and E.cnt < 10000 :
		a = np.random.randint(4)
	else:
		a = np.argmax(E.Q[s])
	A = (s,a)
	E.t += 1
	r = reward(len(ghost)-len(ghost1),len(ghost),lf-len(f),over,time,dg,df)
	return a

