import os
import visualPac
import pacmanBFS
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
			
		i += 1
	return (mat,n,m,ghost,pac)
def valid(i,j,n,m,mat):
	if i >= 0 and i < n and j >= 0 and j < m:
		if mat[i][j] != '#':
			return True
		return False
	return False

mat,n,m,ghost,pac = read()

if __name__ == '__main__':
    atexit.register(set_normal_term)
    set_curses_term()
move = -1
r,c = pac
game = True
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
	ghost = pacmanBFS.BFS(mat,ghost,n,m,pac)
	visualPac.display(n,m,mat,pac,ghost)
	for i,j in ghost:
		if (i,j) == pac:
			print('Game Over')
			game = False
