import os
import visualPac
import pacmanBFS
import escape
import sys, termios, atexit
from select import select

# save the terminal settings
fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)

# new terminal setting unbuffered
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

# switch to normal terminal
def set_normal_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

# switch to unbuffered terminal
def set_curses_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

def getch():
    return sys.stdin.read(3)

def kbhit():
    dr,dw,de = select([sys.stdin], [], [], 0)
    return dr != []

def read():
	file1 = open('pacmanMatrix','r')
	data = file1.readlines()
	mat = []
	i = 0
	n = len(data)
	ghost = ()
	pac = ()
	f = ()
	for line in data:
		m = len(line)-1
		mat.append([])
		j = 0
		for j in range(len(line)-1):
			mat[i].append(' ')
			if line[j] == 'p':
				pac = (i,j)
			elif line[j] == 'g':
				ghost += ((i,j),)
			elif line[j] == '#':
				mat[i][j] = '#'
			elif line[j] == 'f':
				mat[i][j] = 'f'
				f += ((i,j),)
			
		i += 1
	return (mat,n,m,ghost,pac,f)

def valid(i,j,n,m,mat):
	if i >= 0 and i < n and j >= 0 and j < m:
		if mat[i][j] != '#':
			return True
		return False
	return False

mat,n,m,ghost,pac,f = read()

def eat(pac,time):
	global ghost
	global f
	fg = ()
	win = 0
	game = True
	for i,j in f:
		if (i,j) == pac:
			time = 40
		else:
			fg += ((i,j),)
	f = fg
	fg = ()
	for i,j in ghost:
		if (i,j) == pac:
			if time == 0:
				win = -1
				game = False
				fg += ((i,j),)
		else:
			fg += ((i,j),)
	ghost = fg
	if len(ghost) == 0:
		win = 1
		game = False
	return (game,time,win)

def lose(win,score):
	if win == 1 : 
		print('You Won')
		print('Your time = ',score)
	elif win == -1:
		print('Game Over')

if __name__ == '__main__':
    atexit.register(set_normal_term)
    set_curses_term()
move = -1
r,c = pac
game = True
time = 10
delay = 2
score = 0
os.system('clear')
while game:
	if kbhit():
		ch = getch()	
		if ch == '\x1b[D' and valid(pac[0],pac[1]-1,n,m,mat):
			move = 0
		elif ch == '\x1b[A' and valid(pac[0]-1,pac[1],n,m,mat):
			move = 1
		elif ch == '\x1b[C' and valid(pac[0],pac[1]+1,n,m,mat):
			move = 2
		elif ch == '\x1b[B' and valid(pac[0]+1,pac[1],n,m,mat):
			move = 3
		termios.tcflush(sys.stdin, termios.TCIFLUSH)
	if move == 0 and valid(pac[0],pac[1]-1,n,m,mat):
		c = max(c-1,1)
	elif move == 1 and valid(pac[0]-1,pac[1],n,m,mat):
		r = max(r-1,1)
	elif move == 2 and valid(pac[0],pac[1]+1,n,m,mat):
		c = min(c+1,m-2)
	elif move == 3 and valid(pac[0]+1,pac[1],n,m,mat):
		r = min(r+1,n-2)
	mat[pac[0]][pac[1]] = ' '
	for i,j in ghost:
		mat[i][j] = ' '
	pac = (r,c)
	game,time,win = eat(pac,time)
	if game == False:
		visualPac.display(n,m,mat,pac,ghost,time,f)
		lose(win,score)
		break
	if delay % 2:
		if time:
			ghost = escape.esc(mat,pac,n,m,ghost)
		else:
			ghost = pacmanBFS.BFS(mat,ghost,n,m,pac)
	delay = (delay + 1)%2
	visualPac.display(n,m,mat,pac,ghost,time,f)
	game,time,win = eat(pac,time)
	lose(win,score)
	score += 1
	time = max(0,time-1)
