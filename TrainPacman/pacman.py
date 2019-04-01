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
ghost1 = ghost
pac1 = pac
forig = f
if __name__ == '__main__':
    atexit.register(set_normal_term)
    set_curses_term()
move = -1
r,c = pac
game = True
time = 10
delay = 2
score = 0
over = 0
os.system('clear')
while game:
	if kbhit():
		ch = getch()	
		if ch == '\x1b[D' and valid(pac[0],pac[1]-1,n,m,mat):
			move = 2
		elif ch == '\x1b[A' and valid(pac[0]-1,pac[1],n,m,mat):
			move = 0
		elif ch == '\x1b[C' and valid(pac[0],pac[1]+1,n,m,mat):
			move = 3
		elif ch == '\x1b[B' and valid(pac[0]+1,pac[1],n,m,mat):
			move = 1
		termios.tcflush(sys.stdin, termios.TCIFLUSH)
	if move == 2 and valid(pac[0],pac[1]-1,n,m,mat):
		c = max(c-1,1)
	elif move == 0 and valid(pac[0]-1,pac[1],n,m,mat):
		r = max(r-1,1)
	elif move == 3 and valid(pac[0],pac[1]+1,n,m,mat):
		c = min(c+1,m-2)
	elif move == 1 and valid(pac[0]+1,pac[1],n,m,mat):
		r = min(r+1,n-2)
	mat[pac[0]][pac[1]] = ' '
	for i,j in ghost:
		mat[i][j] = ' '
	pac1 = pac
	pac = (r,c)
	ghost = ghost1
	if delay % 2:
		if time:
			ghost1 = escape.esc(mat,pac,n,m,ghost)
		else:
			ghost1 = pacmanBFS.BFS(mat,ghost,n,m,pac)
	delay = (delay + 1)%2
	visualPac.display(n,m,mat,pac,ghost1,time,f)
	fg = ()
	for i,j in f:
		if (i,j) == pac:
			time = 40
		else:
			fg += ((i,j),)
	f = fg
	fg = ()
	score += 1
	for i,j in ghost1:
		if (i,j) == pac:
			if time == 0:
				print('Game Over')
				game = False
				over = -1
				fg += ((i,j),)
		else:
			fg += ((i,j),)
	ghost1 = fg
	if len(ghost1) == 0:
		print('You Won')
		over = 1
		print('Your time = ',score)
		game = False
	time = max(0,time-1)
	if len(f) == 0:
		f = forig
