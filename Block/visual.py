import os

RED = '\033[41m'
GREEN = '\033[42m'
NC = '\033[0m'
WHITE = '\033[47m'
BLUE = '\033[44m'
def display(row,col,mat):
	#os.system('clear')
	d1 = 'tput cup '
	d2 = ' 35'
	i = 8
	for x in range(row):
		s = ''
		d = d1 + str(i) + d2
		os.system(d)
		for y in range(col):
			if(mat[x][y] == '.'):
				s += WHITE + '  ' + NC
				#print(WHITE + '.' + NC),
			elif(mat[x][y] == '#'):
				s += GREEN + '  ' + NC
				#print(GREEN + '#' + NC),
			elif(mat[x][y] == 'S'):
				s += RED + '  ' + NC
				#print(RED + 'S' + NC),
			else :
				s += BLUE + '  ' + NC
		print(s)
		i += 1
	os.system('sleep 0.5')
