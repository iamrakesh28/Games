import os

RED = '\033[41m'
GREEN = '\033[42m'
NC = '\033[0m'
WHITE = '\033[47m'
BLUE = '\033[44m'
G = '\U0001F608'
G_ = '\U0001F480'
P = '\U0001F47D'
F = '\U0001F353'

def display(row,col,mat,pac,ghost,time,f):
	#os.system('clear')
	if len(f):
		for i,j in f:
			mat[i][j] = 'f'
	mat[pac[0]][pac[1]] = 'p'
	for i,j in ghost:
		if (time and (i,j) == (pac[0],pac[1])) == False:
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
				if time:
					s += WHITE + G_ + NC
				else:	
					s += WHITE + G + NC
			elif(mat[x][y] == 'p') :
				s += WHITE + P + NC
			else:
				s += WHITE + F + NC
		print(s)
		i += 1
	os.system('sleep 0.3')
