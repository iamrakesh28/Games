import os

RED = '\033[41m'
GREEN = '\033[42m'
NC = '\033[0m'
WHITE = '\033[47m'
BLUE = '\033[44m'
G = '\U0001F608'
P = '\U0001F47D'
def display(row,col,mat,pac,ghost):
	#os.system('clear')
	mat[pac[0]][pac[1]] = 'p'
	for i,j in ghost:
		mat[i][j] = 'g'
	d1 = 'tput cup '
	d2 = ' 30'
	i = 8
	for x in range(row):
		s = ''
		d = d1 + str(i) + d2
		os.system(d)
		for y in range(col):
			if(mat[x][y] == ' '):
				s += WHITE + '  ' + NC
				#print(WHITE + '.' + NC),
			elif(mat[x][y] == '#'):
				s += GREEN + '  ' + NC
				#print(GREEN + '#' + NC),
			elif(mat[x][y] == 'g'):
				#s += RED + '  ' + NC
				s += WHITE + G + NC
			else :
				s += WHITE + P + NC
		print(s)
		i += 1
	os.system('sleep 0.3')
